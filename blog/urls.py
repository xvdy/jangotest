__author__ = 'xdy'

from django.conf.urls.defaults import url, patterns
import views

urlpatterns = patterns('',
    url(r"^index/$", views.index)
)