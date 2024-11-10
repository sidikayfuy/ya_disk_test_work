import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from urllib.parse import quote
from disk.serializers import RegisterSerializer, UserSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user,    context=self.get_serializer_context()).data)


class UserData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = {
            'email': user.email,
        }
        return Response(user_data)


class GetData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        public_key = request.GET.get('public_key')
        api_url = f"https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_key}"
        response = requests.get(api_url, timeout=5,
                                headers={'Authorization': 'OAuth ' + settings.YANDEX_API_KEY})
        if response.status_code == 200:
            return Response(response.json()['_embedded']['items'], status=200)
        else:
            return Response({'error': response.text}, status=400)


class Download(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        links = []
        for key in request.data:
            api_url = f'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={quote(key["public_key"])}&path={quote(key["path"])}'
            response = requests.get(api_url, timeout=5, headers={'Authorization': 'OAuth ' + settings.YANDEX_API_KEY})
            links.append(response.json().get('href'))
        return Response({'links': links}, status=200)

