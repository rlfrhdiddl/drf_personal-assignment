from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.


class TdList(models.Model): #verbose_name은 지정 안해주면 변수이름으로 자동 지정
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user_id")
    title = models.CharField(max_length=100, verbose_name="title")
    created_at = models.DateField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateField(auto_now=True, verbose_name="updated_at")
    is_complete = models.BooleanField(default=False, verbose_name="is_complete")
    completion_at = models.DateField(null=True, blank=True, verbose_name="completion_at")

    def save(self,*args, **kwargs):
        if self.is_complete and not self.completion_at: #완료여부가 True이면서 완료시간이 없으면
            self.completion_at = timezone.now() # 완료시간을 기록
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title