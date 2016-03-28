from __future__ import unicode_literals

from django.db import models


class Album(models.Model):
    album_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date released')

    def __str__(self):
        return self.album_name
