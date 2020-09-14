from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import View, RedirectView
from tweets.models import Tweet, HashTag
from user_profile.models import User
from tweets.forms import TweetForm, SearchForm, SearchHashTagForm
from django.template.loader import render_to_string
from django.template import Context
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime


class Index(View):
    @login_required
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
        # return HttpResponse('Hello, World!')
            params = {}
            params["name"] = "Django"
            return render(request, 'base.html', params)
        else:
            return HttpResponseRedirect('/login/')

class Profile(LoginRequiredMixin, View):
    """User Profile page reachable from /user/<username> URL"""
    def get(self, request, username):
        params = dict()
        userProfile = User.objects.get(username=username)
        userFollower = UserFollower.objects.get(user=userProfile)
        if userFollower.followers.filter(username=request.user.username).exists():
            params["following"] = True
        else:
            params["following"] = False
            form = TweetForm(initial={'country': 'Global'})
            search_form = SearchForm()
            tweets = Tweet.objects.filter(user=userProfile).order_by('-created_date')
            params["tweets"] = tweets
            params["profile"] = userProfile
            params["form"] = form
            params["search"] = search_form
        return render(request, 'profile.html', params)

class PostTweet(RedirectView):
    """Tweet Post form available on page /user/<username> URL"""

    def post(self, request, username):
        form=TweetForm(self.request.POST)
        print(form.is_valid())
        # print(form.cleaned_data['country'])
        if form.is_valid():
            user=User.objects.get(username = username)
            tweet=Tweet(text = form.cleaned_data['text'],
                          user = user,
                          country = form.cleaned_data['country']
                          )
            tweet.save()
            words=form.cleaned_data['text'].split(" ")
            tweets=Tweet.objects.filter(user = user)

            for word in words:
                if word[0] == "#":
                    hashtag, created=HashTag.objects.get_or_create(
                        name=word[1:])
                    hashtag.tweet.add(tweet)
            return HttpResponseRedirect('/user/' + username)


class HashTagCloud(View):
    """Hash Tag page reachable from /hastag/<hashtag> URL"""

    def get(self, request, hashtag):
        params = dict()
        hashtag = HashTag.objects.get(name=hashtag)
        params["tweets"] = hashtag.tweet
        return render(request, 'hashtag.html', params)


class Search(View):
    """Search all tweets with query /search/?query=<query> URL"""

    def get(self, request):
        form = SearchForm()
        params = dict()
        params["search"] = form
        return render(request, 'search.html', params)

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            tweets = Tweet.objects.filter(text__icontains=query)
            context = {"query": query, "tweets": tweets}
            return_str = render_to_string(
                'partials/_tweet_search.html', context=context)
            return HttpResponse(json.dumps(return_str), content_type="application/json")
        else:
            return HttpResponseRedirect("/search")


class SearchHashTag(View):
    """Search a hashTag with auto complete feature"""

    def get(self, request):
        form = SearchHashTagForm()
        params = dict()
        params["search"] = form
        return render(request, 'search_hashtag.html', params)

    def post(self, request):
        params = dict()
        query = request.POST['query']
        form = SearchHashTagForm()
        hashtags = HashTag.objects.filter(name__contains=query)
        params["hashtags"] = hashtags
        params["search"] = form
        return render(request, 'search_hashtag.html', params)


class HashTagJson(View):
    """Search a hashTag with auto complete feature"""

    def get(self, request):
        query = request.GET['query']
        hashtaglist = []
        hashtags = HashTag.objects.filter(name__icontains=query)
        print(query)
        for hashtag in hashtags:
            temp = dict()
            temp["query"] = (hashtag.name)
            hashtaglist.append(temp)
        return HttpResponse(json.dumps(hashtaglist), content_type="application/json")

class UserRedirect(View):
    def get(self, request):
        return HttpResponseRedirect('/user/'+request.user.username)
