from .models import User
# from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import RegisterSerializer
# Create your views here.

'''
@RestController
'''
# class UserViewSet(viewsets.ModelViewSet):
#     # 实体类
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

class RegisterController(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"detail":"注册成功! "},status=status.HTTP_201_CREATED)
