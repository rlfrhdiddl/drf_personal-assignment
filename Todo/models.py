from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.


class TodoList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="유저")
    title = models.CharField(max_length=100, verbose_name="제목")
    created_at = models.DateField(auto_now_add=True, verbose_name="생성시간")
    updated_at = models.DateField(auto_now=True, verbose_name="업데이트시간")
    is_complete = models.BooleanField(default=False, verbose_name="완료여부")
    completion_at = models.DateField(null=True, blank=True, verbose_name="완료시간")

    def save(self,*args, **kwargs):
        if self.is_complete and not self.completion_at:
            self.completion_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title