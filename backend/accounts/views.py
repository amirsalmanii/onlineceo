from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.authtoken.models import Token
from kavenegar import *
from .models import User
from . import serializers
from config import secret
from otp.models import UserOtp


class UserVerifyOtp(APIView):
    """
    By receiving the mobile number and checking it in Serlizer (this user is exist or not and ...),
    we store the phonenumber in userotp model and send password to the user and check
    it in the bottom view the password entered is correct or not.
    """
    def post(self, request):
        serializer = serializers.OtpVerifySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            otp_obj = UserOtp.objects.save_data_otp(data)
            try:
                api = KavenegarAPI(secret.K_API_KEY)
                msg = str(otp_obj.password)
                params = {
                    'receptor': otp_obj.phone_number,
                    'template': 'sendotponlineceo',
                    'token': msg,
                    'type': 'sms',
                }   
                response = api.verify_lookup(params)
            except APIException as e:
                pass
            except HTTPException as e:
                pass
            return Response({"key": otp_obj.key}, status=200)

        return Response(serializer.errors, status=404)


class UserConfirmOtp(APIView):
    """
    check passwored entered is correct with model userotp or not if true:
    we send token to frontend if not we send 404
    """
    def post(self, request):
        serializer = serializers.OtpConfirmSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user = User.objects.get(username=data['phone_number'])
            if user.is_admin:
                admin=True
            else:
                admin=False
            token = Token.objects.filter(user=user)
            otps = UserOtp.objects.filter(phone_number=user).delete()
            if token:
                token = token.first()
            else:
                token = Token.objects.create(user=user)
            return Response({"token": token.key, 'admin': admin}, status=200)
        else:
            return Response(serializer.errors, status=404)


class UserListAndCreateView(ListCreateAPIView):
    """
    request get ==> users list
    request post ==> user create
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailAndUpdateANdDelete(RetrieveUpdateDestroyAPIView):
    """
    request get ==> user detail
    request put ==> user update
    request delete ==> user delete
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
