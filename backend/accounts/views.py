import random
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
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
from otp.models import UserOtp, UserEmailOtp


class MyPagination(PageNumberPagination):
    page_size = 20


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
            if user.is_admin or user.is_operator:
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


class UserVerifyOtpEmail(APIView):
    """
    like UserVerifyOtp but use email
    """
    def post(self, request):
        serializer = serializers.OtpEmailVerifySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            otp_obj = UserEmailOtp.objects.save_data_email_otp(data)
            msg = f'{otp_obj.password} ???? ???? ???? ???????????? ???????? ????????'
            client_email = otp_obj.email
            send_mail('vetnow auth', msg, settings.DEFAULT_FROM_EMAIL, [client_email])
            return Response({"key": otp_obj.key}, status=200)
        return Response(serializer.errors, status=400)


class UserConfirmOtpEmail(APIView):
    """
    like UserConfirmOtp but use email
    """
    def post(self, request):
        serializer = serializers.OtpEmailConfirmSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user = User.objects.get(email=data['email'])
            if user.is_admin or user.is_operator:
                admin=True
            else:
                admin=False
            token = Token.objects.filter(user=user)
            otps = UserEmailOtp.objects.filter(email=user.email).delete()
            if token:
                token = token.first()
            else:
                token = Token.objects.create(user=user)
            return Response({"token": token.key, 'admin': admin}, status=200)
        else:
            return Response(serializer.errors, status=404)


class UserRegisterView(APIView):
    def post(self, request):
        print(request.data)
        serializer = serializers.UserRegisterSerilizer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            username = data.get('phone_number')
            email = data.get('email')
            if username:
                usr = User.objects.filter(username = username)
                if not usr:
                    user = User(username=username)
                    user.save()
                else:
                    return Response('?????????? ???????? ?????? ?????? ??????', status=404)
            elif email:
                user_e = User.objects.filter(email = email)
                if not user_e:
                    user_name=random.randint(1, 11000000)
                    user = User(username=user_name, email=email)
                    user.save()
                else:
                    return Response('?????????? ???????? ?????? ?????? ??????', status=404)
            token = Token.objects.create(user=user)
            return Response({"token": token.key}, status=200)
        else:
            return Response(serializer.errors, status=401)


class UserListAndCreateView(ListCreateAPIView):
    """
    request get ==> users list
    request post ==> user create
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'first_name', 'last_name']


class UserDetailAndUpdateANdDelete(RetrieveUpdateDestroyAPIView):
    """
    request get ==> user detail
    request put ==> user update
    request delete ==> user delete
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserListAdminOrOprator(ListAPIView):
    queryset = User.objects.filter(Q(is_admin=True) | Q(is_operator=True))
    serializer_class = serializers.UserSerializer2


class UserProfile(APIView):
    def get(self, request):
        user = request.user
        serializer = serializers.UserSerializer(user, context={'request': request})
        return Response(serializer.data, status=200)
    
    def put(self, request):
        user = request.user
        serializer = serializers.UserSerializer3(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        return Response(serializer.errors, status=400)


class ShowUserWallet(APIView):
    def get(self, request):
        user = request.user
        user_wallet = user.wallet
        return Response(user_wallet, status=200)


class ShowUserData(APIView):
    def get(self, request):

        user = request.user
        if user.is_anonymous:
            return Response(status=404)
        else:
            serializer = serializers.UserSerializer(user, context={'request': request})
            return Response(serializer.data, status=200)
