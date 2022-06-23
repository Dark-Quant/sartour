from django.db import models

from tour.utils import *


class Tour(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    photo = models.ImageField(upload_to=upload_photo_to)
    is_restored = models.BooleanField(default=False)
    video = models.FileField(upload_to=upload_video_to, null=True, blank=True)
    video_vr = models.FileField(upload_to=upload_video_to, null=True, blank=True)
    virtual_tour = models.URLField(null=True, blank=True)
