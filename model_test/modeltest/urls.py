from django.conf.urls import patterns, url
from modeltest.views import TestView

urlpatterns = patterns('',

    url(r'^test/$', TestView.as_view()),

    )

