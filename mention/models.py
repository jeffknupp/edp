from django.db import models
from django.contrib.auth.models import User


class Query(models.Model):
    user = models.ForeignKey(User)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Source(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=None, null=True)


class Mention(models.Model):
    source = models.ForeignKey(Source)
    query = models.ForeignKey(Query)
    occurred_at = models.DateTimeField()
    referrer_name = models.CharField(max_length=100)
    content = models.TextField()


class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    mention = models.ForeignKey(Mention)
    referring_page = models.URLField()
