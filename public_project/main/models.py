from typing import Set

from django.contrib.auth.models import User
from django.db import models
from django.db.models import IntegerField


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='id_user_my', primary_key=True)
    face_auth = models.IntegerField(default=0)
    true_auth = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

    def user_info(self) -> set[int]:
        return {int(self.face_auth), int(self.true_auth)}
