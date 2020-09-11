from django.db import models
import uuid
from user.models import User
from groups.models import Group

# Create your models here.


def get_image_path(filename, instance):
    ext = filename.split('.')[-1]
    filename = '/{}/{}/{}.{}'.format(instance.group.id,
                                     instance.post.id, uuid.uuid4(), ext)
    return filename


class Post(models.Model):
    def __str__(self):
        return self.title

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post")
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="post")
    title = models.CharField(max_length=200)
    content = models.TextField()


class Image(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="image")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="image")
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to=get_image_path, verbose_name="Image")

    def __str__(self):
        return self.post.title + "image"
