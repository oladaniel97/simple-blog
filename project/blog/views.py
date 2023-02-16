from django.shortcuts import render,redirect
from .models import Post
from .forms import CommentForm

# Create your views here.
def index(request):
    posts = Post.objects.all()

# remeember to add custom variables to context
    context={
        'posts': posts
    }
    return render(request, 'blog/index.html',context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail',slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post':post,'form':form})