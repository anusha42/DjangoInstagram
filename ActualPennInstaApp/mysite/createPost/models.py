from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_text = models.TextField(blank=True, null=True)
    # pub_date = models.DateTimeField('date published')
    # usernm = models.TextField(default = 'anusha')
    usernm = models.ForeignKey(User, on_delete=models.CASCADE)