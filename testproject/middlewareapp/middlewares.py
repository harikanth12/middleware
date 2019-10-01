from django.http import HttpResponse 
from django.template.response import TemplateResponse
import requests

class ExcuationFlow:
	def __init__(self,get_response):
		self.get_response = get_response
		# print(self.get_response,"getresponse")

	def __call__(self,request):
		# url = 'http://127.0.0.1:8000/index/'
		# a = requests.request('GET',url)
		# print(a)
		response = self.get_response(request)
		# print("This line is excuted after the view function is called")

		# return HttpResponse("<h1>Currently Application in under Maintainace</h1>")
		return response

	def process_view(self,request,view_fun,view_args,view_kwargs):
		request.role = "Admin"


	def process_template_response(self,request,response):
		context = {}
		response.context_data['data'] = "I changed the data from the middleware"

		context['data'] = response.context_data['data']
		context['title'] = response.context_data['title']

		return TemplateResponse(request,'base.html',context)
		# response.context['title'] = 'We changed the title'
  #       return TemplateResponse(request,'base.html',context)

	def process_exception(self,request,exception):
		s="<h1> Currently we are having some technical issues plz wait for some time</h1><hr>"
		s1 = f"<h2>EXception {exception.__class__.__name__}</h2>"
		s2 = f"<h2>Message{exception}</h2>"
		return HttpResponse(s+s1+s2)
