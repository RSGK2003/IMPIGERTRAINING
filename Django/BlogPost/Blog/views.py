from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import BlogPost,Comment
from .serializers import BlogPostSerializer,CommentSerializer
# Create your views here.
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
