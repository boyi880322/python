from django.shortcuts import render, redirect
import random
from django.http import HttpResponse
from onesite.models import foreign

# Create your views here.
def index (request):
	name = "CHEN"
	lucky = random.randint(1,7)
	lottos= list()
	for i in range(6):
		lottos.append(random.randint(1,42))
	return render(request, 'index.html', locals())