from django.conf.urls import url
from .views import TweetListAPIView
from django.views.generic.base import RedirectView

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url='/')),
    url(r'^$', TweetListAPIView.as_view(), name='list'),   #/api/tweet/
    # url(r'^create/$', TweetCreateView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]