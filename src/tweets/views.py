from django.contrib.auth.mixins import LoginRequiredMixin
#To apply add LoginRequiredMixin as a parameter and login_url in the function
from django.shortcuts import render , get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django import forms
from django.db.models import Q

from .forms import TweetModelForm
from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin


class TweetCreateView ( FormUserNeededMixin,CreateView ):
	form_class  = TweetModelForm
	template_name = 'tweets/tweet_create.html'

class TweetUpdateView(UserOwnerMixin,UpdateView):
	form_class  = TweetModelForm
	queryset = Tweet.objects.all()
	# success_url = '/tweet/'

class TweetDeleteView(LoginRequiredMixin,DeleteView):
	model = Tweet
	success_url = reverse_lazy('tweet:list')

class TweetDetailView ( DetailView ):
	queryset = Tweet.objects.all()

class TweetListView ( ListView ):
	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		query = self.request.GET.get('q',None)
		if query is not None:
			qs = qs.filter(Q(content__icontains=query) |
						   Q(user__username__icontains=query) )
		return qs

	def get_context_data(self, *args, **kwargs):
		context = super (TweetListView,self).get_context_data(*args, **kwargs)
		context['create_form'] = TweetModelForm()
		context['create_url'] = reverse_lazy("tweet:create")
		return context

