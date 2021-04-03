from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import userProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer

# Create your views here.

class UserProfileListCreateView(ListCreateAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]

@api_view(['POST'])
def login(request) : 
    data = JSONParser().parse(request)
    email = data['email']
    password = data['password']

    if (email is None) or (password is None) :
        return JsonResponse({"message":"Email and Password must be filled","status":500,"response":[]})

    checkUSer = Users.objects.filter(email=email).first()
    if checkUSer is None :
        return JsonResponse({"messgae":"Check your email and password", "status":500 , "response":[]})
    if not checkUSer.check_password(password) :
        return JsonResponse({"messgae":"Check your email and password", "status":500 , "response":[]})

    token = generate_access_token(checkUSer)
    update = Users.objects.filter(email=email).update(token=token)
    serializer = LoginSerializer(checkUSer).data 
    res = {
        'id' : serializer['id'],
        'user_type' : serializer['user_type'] ,
        'email' : serializer['email'] ,
        'token' : token
    }

    return JsonResponse({"message":"success","status":200,"response":res})