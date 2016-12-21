from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def imgProc(request):
	
	theUrl =  request.GET.get('url');
		# your custom method or you can go ahead here itself to process your text
	
		# do your magic using theUrl Variable





		
		# your magic is done here - now return response


	return HttpResponse(theUrl)
	

