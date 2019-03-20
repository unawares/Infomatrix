from django.db import models

import uuid
from functools import partial

from django.db.models.signals import post_delete
from django.dispatch import receiver


# Utils

def make_filepath(field_name, instance, filename):
    new_filename = "%s.%s" % (uuid.uuid4().hex, filename.split('.')[-1])
    return '/'.join([
        instance.__class__.__name__.lower(),
        field_name,
        new_filename
    ])


# Create your models here.

class Food(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
       ordering = ('-date',)

    def __str__(self):
        return "{} ({})".format(self.title, self.date)


class FoodBackgroundImage(models.Model):

    food = models.OneToOneField(
        Food,
        on_delete=models.CASCADE,
        related_name='food_background_image'
    )
    image = models.ImageField(upload_to=partial(make_filepath, 'image'))
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} [{}]".format(self.description, self.food)


@receiver(post_delete, sender=FoodBackgroundImage)
def food_bakground_image_post_delete_handler(sender, instance, **kwargs):
    storage, path = instance.image.storage, instance.image.path
    storage.delete(path)