from django.shortcuts import render
from rest_framework import generics
from .models import Category, Comment, Post, Like, PostView
from .forms import CommentForm, PostForm
from .serializers import CategorySerializer, PostSerializer, PostViewSerializer, CommentSerializer, LikeSerializer
from rest_framework.permissions import IsAuthenticated


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset =Post.objects.all()
    permission_classes = [IsAuthenticated]

class PostViewList(generics.ListAPIView):
    serializer_class = PostViewSerializer
    queryset = PostView.objects.all()
    permission_classes = [IsAuthenticated]

class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

class LikeList(generics.ListAPIView):
    serializer_class =LikeSerializer
    queryset= Like.objects.all()
    permission_classes = [IsAuthenticated]
















# def post_list(request):
#     qs = Post.objects.all()
#     context ={
#         "object_list" :qs
#     }
#     return render(request, "blog/post_list.html", context)

# @login_required()
# def post_create(request):

#     form = PostForm()
#     if request.method =="POST":
#         form =PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             messages.success(request, "Post Created Succesfully")
#             return redirect("blog:list")
#     context ={
#         "form" : form
#     }
#     return render(request, "blog/post_create.html", context)

# def post_detail(request, slug):
#     form = CommentForm()
#     obj = get_object_or_404(Post, slug=slug)
#     if request.user.is_authenticated:
#         PostView.objects.create(user = request.user, post = obj)
#     if request.method =="POST":
#         form = CommentForm(request.POST)
#         if form.is_valid:
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.post = obj
#             comment.save()
#             return redirect("blog:detail",slug=slug)

#     context ={
#         "object" :obj,
#         "form" : form
#     }
#     return render(request, "blog/post_detail.html", context)

# @login_required()
# def post_update(request,slug):
#     obj = get_object_or_404(Post, slug=slug)
#     form =PostForm(request.POST or None, request.FILES or None, instance=obj)
#     if request.user != obj.author:
#         messages.warning(request, "You are not a writer of this comment")
#         return redirect("blog:list")
#     if form.is_valid():
#         form.save()
#         messages.success(request, "Post Updated!")
#         return redirect("blog:list")

#     context ={
#         "object" : obj,
#         "form" : form
#     }
#     return render(request, "blog/post_update.htm", context)

# @login_required
# def post_delete(request, slug):
#     obj = get_object_or_404(Post, slug=slug)

#     if request.user.id != obj.author.id:
#         messages.warning(request, "You are not a writer of this post")
#         return redirect("blog:list")
#     if request.method == "POST":
#         obj.delete()
#         messages.success(request, "Post deleted succesfully")
#         return redirect("blog:list")
#     context ={
#         "object": obj
#     }
#     return render(request, "blog/post_delete.html", context)

# @login_required()
# def like(request, slug):
#     if request.method =="POST":
#         obj = get_object_or_404(Post, slug=slug)
#         like_qs = Like.objects.filter(user =request.user, post=obj)
#         if like_qs:
#             like_qs.delete()
#         else:
#             Like.objects.create(user=request.user, post=obj)
#         return redirect("blog:detail", slug=slug)
#     return redirect("blog:detail", slug=slug)
