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

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "category",
            "author",
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "user",
            "post",
            "content",

        )
class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostView
        fields = (
            "user",
            "post",
        )
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields =(
            "user",
            "post",
        )