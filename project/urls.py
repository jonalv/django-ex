from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health, secure

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^secure$', secure),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r'openid/', include('djangooidc.urls')),
]
