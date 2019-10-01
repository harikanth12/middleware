

from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.

def demo(request):
	print("This line is printed from the view function")
	return HttpResponse("<h1>Custom midddleware demo </h1>")

def home(request):
	if request.role == "HR":
		print("This is a demo1 application")
		return HttpResponse("<h2>Demo1 application</h2>")

	a = f"<h1>Hello {request.role} </h1>"
	return HttpResponse(a)

def index(request):
	print("index function")
	print(12/0)
	return HttpResponse("THis is index function")

def example_template(request):
	context = {}
	context['title'] = "Middleware Template"
	context['data'] = ""
	return TemplateResponse(request,'base.html',context)