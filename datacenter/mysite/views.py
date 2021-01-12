from django.shortcuts import render, redirect
import random , json
from django.http import HttpResponse
from mysite.models import Post
from datetime import datetime
from mysite.models import AccessInfo,Branch,StoreIncome,Covid

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

def mychart(request,bid=0):
	branches=Branch.objects.all()
	if bid == 0:
		data = StoreIncome.objects.all().order_by('income_month')
	else:
		data=StoreIncome.objects.filter(branch=bid).order_by('income_month')
	return render(request, 'mychart.html' , locals())

def mychart1(request,bid=0):
	branches1=Branch.objects.all()
	if bid == 0:
		data1 = StoreIncome.objects.all().order_by('income_month')
	else:
		data1=StoreIncome.objects.filter(branch=bid).order_by('income_month')
	return render(request, 'mychart.html' , locals())

def mychart2(request,bid=0):
	branches2=Branch.objects.all()
	if bid == 0:
		data2 = StoreIncome.objects.all().order_by('income_month')
	else:
		data2=StoreIncome.objects.filter(branch=bid).order_by('income_month')
	return render(request, 'mychart.html' , locals())

def chart(request,year=0,month=0):
	branches=Branch.objects.all()
	if year == 0 :
		data = StoreIncome.objects.all().order_by('income_month')
	else:
		data=StoreIncome.objects.filter(income_year=year).order_by('income_month')
		if month > 0 :
			data = data.filter(income_month=month)
	if year > 0 and  month > 0 :
		title = "()年()月各分店營收情形".format(year, month)
	elif year > 0 :
		title = "()年各分店營收情形".format(year)
	else:
		title = "各分店營收情形"
	return render(request, 'mychart.html' , locals())

def test(request):
	fp = open("stock.json", "r" ,encoding="utf-8")
	data =fp.read()
	data = json.loads(data)
	target_data = [ (stock["證券名稱"] , stock["收盤價"]) for stock in data ]
	number_data = [ (stock["證券名稱"]) for stock in data ]
	price_data = [ (stock["收盤價"]) for stock in data ]
	return render(request,'test.html',locals())

def money(request):
	fp = open("money.json", "r" ,encoding="utf-8")
	data =fp.read()
	data = json.loads(data)
	
	return render(request,'money.html',locals())

def CHexport(request):
	fp = open("chinaexport.json", "r" ,encoding="utf-8")
	data =fp.read()
	data = json.loads(data)
	
	return render(request,'CHexport.html',locals())


	