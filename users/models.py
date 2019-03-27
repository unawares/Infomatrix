from django.db import models

import uuid

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext, ugettext_lazy as _


# Utils

def generate_code():
    return uuid.uuid4().hex


# Create your models here.

class CustomUser(AbstractUser):

    email = models.EmailField(_('Email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.email
    
    class Meta(AbstractUser.Meta):

        permissions = (
            ('manager', _('Can access the manager features')),
        )


class UserCode(models.Model):

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='user_codes'
    )
    code = models.CharField(max_length=256, default=generate_code, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.code
    