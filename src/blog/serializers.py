from rest_framework import serializers
from .models import Category, Like, Post, PostView, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =(
            "id",
            "name",
            "post_count"
        )

class PostDetailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "category",
            "author",   
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostView
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "user",
            "post",
            "content",

        )
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields =(
            "user",
            "post",
        )