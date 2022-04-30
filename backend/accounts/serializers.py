from rest_framework import serializers
from datetime import timedelta
from django.utils import timezone
from . import models
from otp.models import UserOtp, UserEmailOtp


class OtpVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11, allow_null=False)

    def validate_phone_number(self, value):
        """
        check we have this number in system.
        """
        is_exists = models.User.objects.filter(username=value).exists()
        if is_exists:
            return value
        else:
            raise serializers.ValidationError("این شماره موبایل در سیستم ثبت نشده است")


class OtpConfirmSerializer(serializers.Serializer):
    key = serializers.UUIDField(allow_null=False)
    password = serializers.CharField(max_length=4, allow_null=False, allow_blank=False)

    def validate(self, data):
        """
        Check that password is correct . or time is valid (less then 2 min) and delete it
        """
        otp_obj = UserOtp.objects.filter(key=data['key'])
        if otp_obj:
            otp_obj = otp_obj.first()

            # compute the (datatime created + 2 min) is lower than when requested password now
            create_time = otp_obj.created_at
            create_time_plus_2_min = timedelta(minutes=3) + create_time
            now = timezone.now()
            if now > create_time_plus_2_min:
                otp_obj.delete()
                raise serializers.ValidationError('بیشتر از دو دقیقه از ارسال این کد گذشته است لطفا دوباره امتحان کنید')
            if data['password'] == otp_obj.password:
                data['phone_number'] = otp_obj.phone_number
                return data
            else:
                raise serializers.ValidationError('رمز وارد شده اشتباه می باشد')
        else:
            raise serializers.ValidationError('کلیدی نیست')  # alwase we have key because backend sent to front end correctly.


class OtpEmailVerifySerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=200, allow_null=False)

    def validate_email(self, value):
        """
        check we have this number in system.
        """
        is_exists = models.User.objects.filter(email=value).exists()
        if is_exists:
            return value
        else:
            raise serializers.ValidationError("ایمیل یا رمز اشتباه می باشد")


class OtpEmailConfirmSerializer(serializers.Serializer):
    key = serializers.UUIDField(allow_null=False)
    password = serializers.CharField(max_length=4, allow_null=False, allow_blank=False)

    def validate(self, data):
        """
        Check that password is correct . or time is valid (less then 2 min) and delete it
        """
        otp_obj = UserEmailOtp.objects.filter(key=data['key'])
        if otp_obj:
            otp_obj = otp_obj.first()

            # compute the (datatime created + 2 min) is lower than when requested password now
            create_time = otp_obj.created_at
            create_time_plus_2_min = timedelta(minutes=3) + create_time
            now = timezone.now()
            if now > create_time_plus_2_min:
                otp_obj.delete()
                raise serializers.ValidationError('بیشتر از دو دقیقه از ارسال این کد گذشته است لطفا دوباره امتحان کنید')
            if data['password'] == otp_obj.password:
                data['email'] = otp_obj.email
                return data
            else:
                raise serializers.ValidationError('رمز وارد شده اشتباه می باشد')
        else:
            raise serializers.ValidationError('کلیدی نیست') 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ('password', 'last_login')


class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'first_name', 'last_name')


class UserSerializer3(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ('id', 'username', 'is_admin', 'is_active', 'is_operator', 'password')

