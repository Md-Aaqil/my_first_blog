from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import post
from .forms import PostForm
from django.shortcuts import redirect
def post_list(request):
    posts=post.objects.all()
    return render(request,'blog/post_list.html',{'posts':posts})
# Create your views here.
def post_detail(request,pk):
     posts= get_object_or_404(post, pk=pk)
     return render(request, 'blog/post_detail.html', {'posts': posts})
def post_new(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post_detail', pk=post.pk)
    else:
        form =PostForm()
    return render(request,'blog/post_edit.html',{'form':form})
def post_edit(request, pk):
    posts = get_object_or_404(post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=posts)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.author = request.user
            posts.save()
            return redirect('post_detail', pk=posts.pk)
    else:
        form = PostForm(instance=posts)
    return render(request, 'blog/post_edit.html', {'form': form})
def post_draft_list(request):
    posts=post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request,'blog/post_draft_list.html',{'posts':posts})

def post_publish(request, pk):
    posts= get_object_or_404(post, pk=pk)
    posts.save()
    return redirect('post_detail', pk=pk)
def post_remove(request, pk):
    posts=get_object_or_404(post, pk=pk)
    posts.delete()
    return redirect('post_list')
