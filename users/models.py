from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    username = models.TextField(default=False, verbose_name="username")
    gender = models.TextField(default=False, verbose_name ="gender")
    age = models.IntegerField(default=False, verbose_name ="age")
    introduction = models.TextField(default=False, verbose_name ="introduction")

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# class TodoList(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="유저")
#     title = models.CharField(max_length=100, verbose_name="제목")
#     created_at = models.DateField(auto_now_add=True, verbose_name="생성시간")
#     updated_at = models.DateField(auto_now=True, verbose_name="업데이트시간")
#     is_complete = models.BooleanField(default=False, verbose_name="완료여부")
#     completion_at = models.DateField(null=True, blank=True, verbose_name="완료시간")

#     def save(self,*args, **kwargs):
#         if self.is_complete and not self.completion_at:
#             self.completion_at = timezone.now()
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.title