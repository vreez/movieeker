from rest_framework import serializers
from .models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'user')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'created_at',)