from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import post
def post_list(request):
    posts=post.objects.all()
    return render(request,'blog/post_list.html',{'posts':posts})
# Create your views here.
def post_detail(request,pk):
     posts= get_object_or_404(post, pk=pk)
     return render(request, 'blog/post_detail.html', {'posts': posts})
