from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        #안에 들어오는 변수값들을 다양화하고 유연하게 만들기 위해서 extra_fields를 사용한다.
        """Create and saves a new user """
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)


        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of name"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
        
