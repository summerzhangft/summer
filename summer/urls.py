"""summer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
#from django.contrib import admin

#urlpatterns = [
 #   url(r'^admin/', admin.site.urls),
#]



from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from article import views
#from author import views
#from tag import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^article/', include('article.urls',namespace='article')),
    url(r'^author/', include('author.urls',namespace='author')),
    url(r'^tag/', include('tag.urls',namespace='tag')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
handler404 = 'summer.views.page404'
