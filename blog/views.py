from django.shortcuts import render

from django.utils import timezone

#our own Post model being imported
from .models import Post

# Create your views here.
def post_list(request):
	#posts is the variable name of the QuerySet
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html',{'posts':posts})
	
