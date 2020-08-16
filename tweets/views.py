from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class Index(View):
    def get(self, request,*args, **kwargs):
        #return HttpResponse('Hello, World!')
         params = {}
         params["name"] = "Django"
         return render(request, 'base.html', params)