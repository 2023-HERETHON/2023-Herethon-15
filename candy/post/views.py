from django.shortcuts import render, get_object_or_404
from post.models import Posting

def Post(request):
    posts=Posting.objects.all()
    return render(request, 'post.html', {'post':posts})

def Post_detail(request, pk):
    post_detail=get_object_or_404(Posting, pk=pk)
    return render(request, 'post_detail.html', {'post_detail':post_detail})
def sounds(request):
    return render(request, 'sounds.html', {})
