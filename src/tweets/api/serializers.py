from django.utils.timesince import timesince
from rest_framework import serializers

from tweets.models import Tweet
from accounts.api.serializers import UserDisplaySerializer

class TweetModelSerializer(serializers.ModelSerializer):
	# follower_count = serializers.SerializerMethodField()
	user = UserDisplaySerializer(read_only=True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	class Meta:
		model = Tweet
		fields = [
			'user',
			'content',
			'timestamp',
			'date_display',
			'timesince',
			# 'follower_count',
		]

	def get_date_display(self,obj):
		return obj.timestamp.strftime("%b %d %Y at %I:%M %p")

	def get_timesince(self,obj):
		return timesince(obj.timestamp) + " ago"

	# def get_follower_count(self, obj):
	# 	return 0