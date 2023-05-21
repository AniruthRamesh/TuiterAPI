from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    cover_picture = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(default='',max_length=255)
    email = models.EmailField(default='')
    password = models.CharField(default='',max_length=255)

    class Meta:
        db_table = 'users'
