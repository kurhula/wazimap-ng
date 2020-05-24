from django.db import models

from .. import permissions
from wazimap_ng.profile.models import Profile
from wazimap_ng.datasets.models import Dataset, Indicator
from wazimap_ng.points.models import Category, ProfileCategory

class CustomQuerySet(models.QuerySet):

	# Profile
	def get_profile_profileindicator_queryset(self, user):
		profiles = permissions.get_objects_for_user(
			user, Profile, include_public=False
		)
		return self.filter(profile__in=profiles)

	def get_profile_profilekeymetrics_queryset(self, user):
		profiles = permissions.get_objects_for_user(
			user, Profile, include_public=False
		)
		return self.filter(profile__in=profiles)

	def get_profile_profilehighlight_queryset(self, user):
		profiles = permissions.get_objects_for_user(
			user, Profile, include_public=False
		)
		return self.filter(profile__in=profiles)

	def get_profile_logo_queryset(self, user):
		profiles = permissions.get_objects_for_user(
			user, Profile, include_public=False
		)
		return self.filter(profile__in=profiles)

	def get_profile_indicatorcategory_queryset(self, user):
		profiles = permissions.get_objects_for_user(
			user, Profile, include_public=False
		)
		return self.filter(profile__in=profiles)

	def get_profile_indicatorsubcategory_queryset(self, user):
		profiles = permissions.get_objects_for_user(
			user, Profile, include_public=False
		)
		return self.filter(category__profile__in=profiles)


	# Dataset
	def get_datasets_indicator_queryset(self, user):
		datasets = permissions.get_custom_queryset(Dataset, user)
		return self.filter(dataset__in=datasets)

	def get_datasets_dataset_queryset(self, user):
		profiles = permissions.get_objects_for_user(user, Profile)
		return permissions.get_objects_for_user(
			user, Dataset, queryset=Dataset.objects.filter(profile__in=profiles)
		)

	def get_datasets_indicatordata_queryset(self, user):
		indicators = permissions.get_custom_queryset(Indicator, user)
		return self.filter(indicator__in=indicators)


	# Points
	def get_points_category_queryset(self, user):
		profiles = permissions.get_objects_for_user(user, Profile)

		return permissions.get_objects_for_user(
			user, Category, queryset=self.filter(profile__in=profiles)
		)

	def get_points_location_queryset(self, user):
		profiles = permissions.get_objects_for_user(
			user, Profile, include_public=False
		)
		collections = permissions.get_objects_for_user(
			user, Category, include_public=False
		).filter(profile__in=profiles)
		return self.filter(category__in=collections)

	def get_points_theme_queryset(self, user):
		profiles = permissions.get_objects_for_user(
			user, Profile, include_public=False
		)
		return self.filter(profile__in=profiles)

	def get_points_profilecategory_queryset(self, user):

		return permissions.get_objects_for_user(
			user, ProfileCategory, include_public=False
		)