from django.shortcuts import render
from onesite.models import zone,foreign,weekcase,monthcase,info 

# Create your views here.
def index(request):
    mapinfo = zone.objects.all()
    topinfo = zone.objects.order_by('-count')[:5]
    print(topinfo)
    return render(request,'index.html',locals())

def mychart1(request):
	country = foreign.objects.all()
	
	data = foreign.objects.all().order_by('count')
	
	return render(request, 'chart.html' , locals())

def mychart(request):
	country = foreign.objects.all()
	
	data = foreign.objects.all().order_by('count')
	
	return render(request, 'chart2.html' , locals())