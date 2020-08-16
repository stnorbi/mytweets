from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from tweets.models import Tweet
from user_profile.models import User

class Index(View):
    def get(self, request,*args, **kwargs):
        #return HttpResponse('Hello, World!')
         params = {}
         params["name"] = "Django"
         return render(request, 'base.html', params)


class Profile(View):
    """User Profile page reachable from /user/<username> URL"""
    def get(self, request, username):
        params = dict()
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user=user)
        params["tweets"] = tweets
        params["user"] = user
        return render(request, 'profile.html', params)

