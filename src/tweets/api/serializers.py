from rest_framework import serializers

from tweets.models import Tweet
from accounts.api.serializers import UserDisplaySerializer

class TweetModelSerializer(serializers.ModelSerializer):
	follower_count = serializers.SerializerMethodField()
	user = UserDisplaySerializer(read_only=True) #write_only
	class Meta:
		model = Tweet
		fields = [
			'user',
			'content',
			'follower_count',
		]
	def get_follower_count(self, obj):
		return 0