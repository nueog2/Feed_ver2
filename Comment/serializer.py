from rest_framework import serializers

from .models import Feed_Post, Comment

class Feed_PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed_Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'