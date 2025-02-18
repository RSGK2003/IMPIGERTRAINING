from rest_framework import serializers
from .models import BlogPost,Comment
class BlogPostSerializer(serializers.ModelSerializer):
    comments=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=BlogPost
        fields=['id','title','content','author','created_at','comments']
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']
