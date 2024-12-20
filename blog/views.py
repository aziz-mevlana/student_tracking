from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages

def post(request): 
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})

def post_detail(request, id): 
    post = get_object_or_404(Post, id=id)  # get_list_or_404 yerine get_object_or_404
    comments = post.comments.all()  # comments doğru şekilde alınıyor

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', id=post.id)
    else: 
        comment_form = CommentForm()
    
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

def post_new(request): 
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated!')
            return redirect('post')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, id): 
    post = get_object_or_404(Post, id=id)  # Bu kısım doğru
    if request.method == "POST": 
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, 'Post has been deleted successfully!')
    return redirect('post')
