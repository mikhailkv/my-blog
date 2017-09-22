from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from mysite.blog import views

from mysite.blog import views as blog_views

urlpatterns = [
    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.post_list, name='post_list'),
   # url(r'', include('blog.urls')),
    #url(r'', include('social_auth.urls')),
    url(r'^$', blog_views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', blog_views.signup, name='signup'),
    url(r'^settings/$', blog_views.settings, name='settings'),
    url(r'^settings/password/$', blog_views.password, name='password'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
]
