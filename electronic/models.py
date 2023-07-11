from django.db import models
from django.urls import reverse


class Singer(models.Model):
    nickname = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)
    photo = models.ImageField(
        upload_to='electronic/singers/%Y/%m/%d', default='defaults/singer-default.png')
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    about = models.TextField(blank=True, default="")

    class Meta:
        indexes = [models.Index(fields=['slug',])]

    def __str__(self) -> str:
        return self.nickname

    @property
    def fullname(self):
        return f"{self.name} {self.surname}"

    def get_absolute_url(self):
        return reverse("electronic:singer", kwargs={"slug": self.slug})


class Song(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(
        upload_to='electronic/songs/%Y/%m/%d', default='defaults/song-default.jpg')
    release_date = models.DateField()
    authors = models.ManyToManyField(Singer)

    def __str__(self) -> str:
        return f"{self.name}:{self.release_date}"
