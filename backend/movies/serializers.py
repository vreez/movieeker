from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = ('title', 'popularity', 'vote_average', 'overview', 'genres', 'poster_path', 'rank')
        fields = '__all__'
        # exclude = 'id'