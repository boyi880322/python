import csv,sys,os
project_dir = "/Users/johnny170889/django/python-course/datacenter/datacenter"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()
from mysite.models import Covid
data = csv.reader(open("/Users/johnny170889/django/python-course/datacenter/covid.csv"),delimiter=",")
for row in data:
	if row[0] != 'year':
		post = Covid()
		post.year = row[0]
		post.numb = row[1]
		
		post.save()