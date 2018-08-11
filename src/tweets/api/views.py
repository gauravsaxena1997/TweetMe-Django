from rest_framework import generics
from django.db.models import Q
from .serializers import TweetModelSerializer
from rest_framework import permissions

from tweets.models import Tweet


class TweetCreateAPIView(generics.CreateAPIView):
	serializer_class = TweetModelSerializer
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self,serializer):                                               #handle NULL string
		serializer.save(user=self.request.user)

class TweetListAPIView(generics.ListAPIView):
	serializer_class = TweetModelSerializer
	
	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all().order_by('-timestamp')                                #sort by new to old
		# print (self.request.GET)
		query = self.request.GET.get('q',None)
		if query is not None:
			qs = qs.filter(Q(content__icontains=query) |
						   Q(user__username__icontains=query) )
		return qs