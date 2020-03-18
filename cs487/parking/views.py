from django.shortcuts import render

# Create your views here.
'''chang: ->'''
from django.http import HttpResponse

def index(request):
        return HttpResponse("Hello, this is cs487 parking lot.")

'''<- chang'''

