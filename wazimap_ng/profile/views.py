from django.shortcuts import get_object_or_404
from django.views.decorators.http import condition


from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view


from . import models
from . import serializers
from ..cache import etag_profile_updated, last_modified_profile_updated

from wazimap_ng.datasets.models import Geography

class ProfileDetail(generics.RetrieveAPIView):
    queryset = models.Profile
    serializer_class = serializers.FullProfileSerializer

class ProfileList(generics.ListAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


@condition(etag_func=etag_profile_updated, last_modified_func=last_modified_profile_updated)
@api_view()
def profile_geography_data(request, profile_id, geography_code):
    profile = get_object_or_404(models.Profile, pk=profile_id)
    version = profile.geography_hierarchy.root_geography.version
    geography = get_object_or_404(Geography, code=geography_code, version=version)

    js = serializers.ExtendedProfileSerializer(profile, geography)
    return Response(js)

class ProfileCategoriesList(generics.ListAPIView):
    queryset = models.IndicatorCategory.objects.all()
    serializer_class = serializers.IndicatorCategorySerializer

    def get(self, request, profile_id):
        profile = get_object_or_404(models.Profile, pk=profile_id)
        queryset = self.get_queryset().filter(profile=profile)

        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)

class ProfileSubcategoriesList(generics.ListAPIView):
    queryset = models.IndicatorSubcategory.objects.all()
    serializer_class = serializers.IndicatorSubcategorySerializer

    def get(self, request, profile_id, category_id):
        profile = get_object_or_404(models.Profile, pk=profile_id)
        category = get_object_or_404(models.IndicatorCategory, pk=category_id)
        queryset = self.get_queryset().filter(category__profile=profile, category=category)

        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)
