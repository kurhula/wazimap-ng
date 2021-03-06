from django.views.decorators.http import condition
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from collections import defaultdict
from django.db.models import Count
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework import generics

from . import models
from . import serializers
from ..cache import etag_point_updated, last_modified_point_updated
from ..boundaries.models import GeographyBoundary
from ..general.serializers import MetaDataSerializer
from wazimap_ng.profile.models import Profile

class CategoryList(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def list(self, request, profile_id, theme_id=None):
        profile = Profile.objects.get(id=profile_id)

        queryset = self.get_queryset()
        queryset = queryset.filter(theme__profile=profile_id)

        if theme_id is not None:
            theme = models.Theme.objects.get(id=theme_id)
            queryset = queryset.filter(theme=theme)

        serializer = self.get_serializer_class()(queryset, many=True)
        data = serializer.data

        return Response(data)

@api_view()
def theme_view(request, profile_id):
    themes = defaultdict(list)
    profile = Profile.objects.get(id=profile_id)
    qs = models.ProfileCategory.objects.filter(profile=profile)

    for pc in qs:
        theme = pc.category.theme
        themes[theme].append(pc)

    js = []
    for theme in themes:
        js_theme = {
            "id": theme.id,
            "name": theme.name,
            "icon": theme.icon,
            "categories": []
        }

        for pc in themes[theme]:
            js_theme["categories"].append({
                "id": pc.category.id,
                "name": pc.label,
                "metadata": MetaDataSerializer(pc.category.metadata).data
            })
            
        js.append(js_theme)

    return Response({
        "results" : js
    })

class LocationList(generics.ListAPIView):
    pagination_class = GeoJsonPagination
    serializer_class = serializers.LocationSerializer
    queryset = models.Location.objects.all().select_related("category")

    def list(self, request, profile_id, category_id=None):
        profile = Profile.objects.get(pk=profile_id)
        category = models.Category.objects.get(pk=category_id)

        queryset = self.get_queryset()
        if category_id is not None:
            queryset = queryset.filter(category__pk=category_id)

        serializer = self.get_serializer_class()(queryset, many=True)
        data = serializer.data
        return Response(data)

    @method_decorator(condition(etag_func=etag_point_updated, last_modified_func=last_modified_point_updated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

def boundary_point_count_helper(profile, geography):
    boundary = GeographyBoundary.objects.get_unique_boundary(geography)
    locations = models.Location.objects.filter(coordinates__contained=boundary.geom) 
    location_count = (
        locations
            .filter(category__profilecategory__profile=profile)
            .values(
                "category__id", "category__profilecategory__label",
                "category__theme__name", "category__theme__icon", "category__theme__id",
                "category__metadata__source", "category__metadata__description",
                "category__metadata__licence"
            )
            .annotate(count_category=Count("category"))
    )

    theme_dict = {}

    res = []

    for lc in location_count:
        id = lc["category__theme__id"]
        if id not in theme_dict:
            theme = {
                "name": lc["category__theme__name"],
                "id": lc["category__theme__id"],
                "icon": lc["category__theme__icon"],
                "subthemes": []
            }
            theme_dict[id] = theme
            res.append(theme)
        theme = theme_dict[id]
        theme["subthemes"].append({
            "label": lc["category__profilecategory__label"],
            "id": lc["category__id"],
            "count": lc["count_category"],
            "metadata": {
                "source": lc["category__metadata__source"],
                "description": lc["category__metadata__description"],
                "licence": lc["category__metadata__licence"],
            }
        })

    return res

