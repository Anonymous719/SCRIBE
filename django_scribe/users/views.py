from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response

from Books.serializer import BookSerializer
from SCRIBE.django_scribe import users
from .models import  User
from .serializer import UserSerializer
from Books.models import Book
from django.http import Http404
from rest_framework import status
# Create your views here.

class UserAPI(APIView):
    def get(self, request):
        users = users.objects.all()
        serializer = UserSerializer(users, many=True)
        print(serializer.data)
        return Response(serializer.data)
        
class UserInfoAPI(APIView):
    def get(self, request, pk):
        user = User.objects.get(id = pk)
        serializer = UserSerializer(user)
        print(serializer.data)
        return Response(serializer.data)
    

class UserPurchasedBooksAPI(APIView):
    def get(self, request, pk):
        user = User.objects.get(id = pk)
        books = Book.objects.filter(user = user)
        print(books)
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)

class UserWishlist(APIView):
    def get(self, request, pk):
        user = User.objects.get(id = pk)
        books = Book.objects.filter(user = user)
        print(books)
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        user = User.objects.get(id = pk)
        user.rating += request.data
        user.ratedUsersNo += 1
        return Response({'rating':float(user.rating)/user.ratedUsersNo})
    
