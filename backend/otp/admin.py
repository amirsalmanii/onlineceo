from django.contrib import admin
from .models import UserOtp, UserEmailOtp

admin.site.register(UserOtp)
admin.site.register(UserEmailOtp)
