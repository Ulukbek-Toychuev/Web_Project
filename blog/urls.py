from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from blog import views

urlpatterns = [
    url(r'^countries/$', views.snippet_list),
    url(r'^countries/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
