"""mytweets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from tweets.views import Index, Profile, PostTweet, HashTagCloud, Search, SearchHashTag, HashTagJson, UserRedirect
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings 
from django.views.decorators.cache import cache_page
from django.contrib.auth.views import LoginView, LogoutView


admin.autodiscover()


urlpatterns = [
    re_path(r'^$', Index.as_view(), name='index'),
    re_path(r'^user/(\w+)/$', Profile.as_view(),name='profile'),
    path('admin/', admin.site.urls),
    re_path(r'^user/(\w+)/post/$', PostTweet.as_view(), name='posts'),
    re_path(r'^hashTag/(\w+)/$', HashTagCloud.as_view()),
    re_path(r'^search/$', Search.as_view()),
    re_path(r'^search/hashTag$',  cache_page(60 * 15)(SearchHashTag.as_view())),
    re_path(r'^hashtag.json$', HashTagJson.as_view()),
    re_path(r'^login$', LoginView.as_view()),
    re_path(r'^logout/$', LogoutView.as_view()),
    re_path(r'^profile/$', UserRedirect.as_view())
]
