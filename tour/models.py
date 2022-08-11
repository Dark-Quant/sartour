from django.db import models
import video_stream

from tour.utils import *


class Tour(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    photo = models.ImageField(upload_to=upload_photo_to)
    is_restored = models.BooleanField(default=False)
    video = models.ForeignKey(video_stream.models.Video, on_delete=models.PROTECT, null=True, blank=True)
    virtual_tour = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title