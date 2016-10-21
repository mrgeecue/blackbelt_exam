from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User(models.Model):
    # def validatereg(self, request):
    #     errors = self.validate_inputs(request)
    #
    #     if len(errors) > 0:
    #         return (False, errors)
    #
    #     pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    #
    #     user = self.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], pw_hash=pw_hash), dob=request.POST['dob']
    #     return (True, user)

    name = models.CharField(max_length = 45)
    alias = models.CharField(max_length = 45)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Pokes(models.Model):
    poke = models.CharField(max_length = 45)
    user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
