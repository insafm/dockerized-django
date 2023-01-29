from django.db import models
from django.utils import timezone

# Create your models here.
class AbstractBaseModel(models.Model):
	"""AbstractBaseModel contains common fields between models.
	All models should extend this class.
	"""
	status = models.BooleanField(default=True, blank=True)
	deleted = models.BooleanField(default=False, blank=True)
	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(default=timezone.now)

	class Meta:
		abstract = True