from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    pst_img = models.ImageField(blank=True, null=True, upload_to='uploads', verbose_name='Post Image')
    post_content = models.TextField(blank=True)
    post_content_a = models.TextField(blank=True)
    post_content_b = models.TextField(blank=True)
    post_content_c = models.TextField(blank=True)
    post_content_d = models.TextField(blank=True)
    post_content_e = models.TextField(blank=True)
    post_content_f = models.TextField(blank=True)
    post_content_g = models.TextField(blank=True)
    user_id = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title

class Event(models.Model):
    post_title = models.CharField(max_length=100)
    pst_img = models.ImageField(blank=True, null=True, upload_to='uploads', verbose_name='Post Image')
    post_content = models.TextField(blank=True)
    post_phone = models.TextField(blank=True, max_length=10)
    user_id = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title
