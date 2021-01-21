from django import forms
from django.db.models import fields
from .models import Post, Comment, Category

class PostForm(forms.ModelForm):
    # status = 
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label= "Select")

    class Meta:
        model =Post
        fields =(
            "title",
            "content",
            
            "category",
           

        )

class CommentForm(forms.ModelForm):
    class Meta:
            model =Comment
            fields = ("content",)

   