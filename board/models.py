from django.db import models
from user.models import User
from proj import settings

# Create your models here.

#  
class Board(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, related_name="write")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    # writer = models.ForeignKey('user.User', on_delete = models.CASCADE)

    def __str__(self):
        return self.title
        # 제목으로 표시되게


class Comment(models.Model):
    objects = models.Manager()
    board = models.ForeignKey('Board', on_delete=models.CASCADE, related_name='comments')
    comment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name="comments")
    comment_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.comment_user
        # 제목으로 표시되게
    #approved_comment = models.BooleanField(default=False)
    # class Meta:
    # ordering=['id'] # 정렬기준

    # def approve(self):
    #     self.approved_comment = True
    #     self.save()

    # def __str__(self):
    #     return self.comment_body
