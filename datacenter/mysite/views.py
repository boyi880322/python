from django.shortcuts import render, redirect
import random
from django.http import HttpResponse
from mysite.models import Post
from datetime import datetime
from mysite.models import AccessInfo

def index (request):
	name = "CHEN"
	lucky = random.randint(1,7)
	lottos= list()
	for i in range(6):
		lottos.append(random.randint(1,42))
	return render(request, 'index.html', locals())

def homepage(request):
	rec = AccessInfo()
	rec.save()
	visit_count = len(AccessInfo.objects.all())
	posts = Post.objects.all()
	now = datetime.now()
	return render(request, 'index.html' , locals())

def showpost(request, slug):
	try:
		post = Post.objects.get(slug = slug)
		if post != None:
			return render(request, 'post.html', locals())
	except:
		return redirect('/')
		
def lotto(request):
	lucky = random.randint(1,7)
	lottos= list()
	for i in range(6):
		lottos.append(random.randint(1,42))
	return render(request, 'lotto.html' , locals())

def mychart(request):
	return render(request, 'mychart.html' , locals())