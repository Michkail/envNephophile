from django.db import models

class Post(models.Model):
    created_on  = models.DateTimeField(auto_now_add=True)
    updated_on  = models.DateField(auto_now=True)
    title       = models.CharField(max_length=100, blank=True, default='')
    body        = models.TextField(blank=True, default='')
    owner       = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

class Comment(models.Model):
    created_on  = models.DateTimeField(auto_now_add=True)
    updated_on  = models.DateField(auto_now=True)
    body        = models.TextField(blank=False)
    owner       = models.ForeignKey(
        'auth.User',
        related_name='comments',
        on_delete=models.CASCADE
    )
    post        = models.ForeignKey(
        'Post',
        related_name='comments',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['id']

"""
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class SampleModel(DjangoCassandraModel):
    sample_id   = columns.UUID(primary_key=True, default=uuid.uuid4)
    sample_type = columns.Integer(index=True)
    created_at  = columns.DateTime()
    sample_desc = columns.Text(required=False)
"""