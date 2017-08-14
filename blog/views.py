from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  form = CommentForm()
  return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

def post_comment(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.save()
      return redirect('post_detail', pk=post.pk)
  else:
    return redirect('post_detail', pk=post.pk)


@login_required
def comment_delete(request, pk):
  comment = get_object_or_404(Comment, pk=pk)
  post_pk = comment.post.pk
  comment.delete()
  return redirect('post_detail', pk=post_pk)


@login_required
def comment_approve(request, pk):
  comment = get_object_or_404(Comment, pk=pk)
  comment.approve()
  post_pk = comment.post.pk
  return redirect('post_detail', pk=post_pk)

@login_required
def add_new(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == 'POST':
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm(instance=post)
  return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def draft_posts(request):
  posts = Post.objects.filter(published_date__isnull=True)
  return render(request, 'blog/draft_posts.html', {'posts': posts})


@login_required
def post_publish(request, pk):
  post = get_object_or_404(Post, pk=pk)
  post.publish()
  return redirect('post_detail', pk=post.pk,)


@login_required
def post_delete(request, pk):
  post = get_object_or_404(Post, pk=pk)
  post.delete()
  return redirect('post_list')

