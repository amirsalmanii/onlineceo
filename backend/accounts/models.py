from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.urls import reverse
from .managers import MyUserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=150, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True, default="")
    last_name = models.CharField(max_length=150, null=True, blank=True, default="")
    avatar = models.ImageField(
        upload_to="users/%Y/", null=True, blank=True, default=""
    )
    wallet = models.PositiveBigIntegerField(default=0)
    # for address
    state = models.CharField(max_length=200, null=True, blank=True, default="")
    city = models.CharField(max_length=200, null=True, blank=True, default="")
    address = models.TextField(null=True, blank=True, default="")
    plate = models.CharField(
        max_length=5, null=True, blank=True, default=""
    )  # pelak khane
    zip_code = models.CharField(max_length=10, null=True, blank=True, default="")

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    objects = MyUserManager()

    is_admin = models.BooleanField(default=False)
    is_operator = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_lable):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_absolute_url(self):
        return reverse("accounts:user_update", args=[self.id])
    
    class Meta:
        ordering = ('-id',)