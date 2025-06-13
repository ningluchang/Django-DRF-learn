# from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics,status
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import RegisterSerializer
# Create your views here.

'''
@RestController
'''

class RegisterController(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"detail":"注册成功! "},status=status.HTTP_201_CREATED)


class CustomObtainAuthToken(ObtainAuthToken):
    # 登录接口,返回token和用户信息
    permission_classes = [AllowAny]
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self,request,*args,**kwargs):
        response  = super().post(request,*args,**kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({
            'token':token.key,
            'user_id':user.id,
            'username':user.username,
            'email':user.email
        })