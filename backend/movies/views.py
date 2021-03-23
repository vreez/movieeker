from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes
)
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_403_FORBIDDEN
)
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Movie
from .serializers import MovieSerializer
import requests
import json

# Create your views here.

API_KEY = '46121df91ceeaf70b4337f8759116b64'
BASE_URL = 'https://api.themoviedb.org/3'
@api_view(['GET', 'POST'])
def index(request):
    # res = requests.get(f'https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=ko-KR&page=1')
    # now_playing_movies = res.json().get('results')
    # print(now_playing_movies)
    # # movies = Movie.objects.all()

    # if request.method == 'GET':
    #     # movies = request.user.movies
    #     # serializer = MovieSerializer(movies, many=True)
    #     return Response(now_playing_movies)

    ##########
    # movies = Movie.objects.all()[:60]
    # serializer = MovieSerializer(movies, many=True)
    # return Response(serializer.data)


    data = []
    for k in range(1, 4):
        res = requests.get(f'https://api.themoviedb.org/3/movie/now_playing?api_key=46121df91ceeaf70b4337f8759116b64&language=ko-KR&page={k}')
        now_playing_movies = res.json().get('results')
        
        for i in now_playing_movies:
            temp = {
                # 이 movie id랑 NowPlyaing.vue에 getMovieId함수에 movieId랑일치시켜줘야해
                    "movie_id": i.get("id"), 
                    "title": i.get('title'),
                    "release_date": i.get('release_date'),
                    "popularity": i.get('popularity'),
                    "vote_count": i.get('vote_count'),
                    "vote_average": i.get('vote_average'),
                    "overview": i.get('overview'),
                    "poster_path": i.get('poster_path'),
                    "genres": i.get('genre_ids')
                
            }
            data.append(temp)
    return Response(data)        


    

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication]) # token이 유효한지 검사
@permission_classes([IsAuthenticated])
def nowplaying(request):
    movies = Movie.objects.filter(vote_average__gt = 0).order_by('-release_date')[:12]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication]) # token이 유효한지 검사
@permission_classes([IsAuthenticated])
def popular(request):
    movies = Movie.objects.filter(vote_average__gt = 0).order_by('-popularity')[:12]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication]) # token이 유효한지 검사
@permission_classes([IsAuthenticated])
def voteaverage(request):
    movies = Movie.objects.filter(vote_average__gt = 0).order_by('-vote_average')[:12]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication]) # token이 유효한지 검사
@permission_classes([IsAuthenticated])
def detail(request, movie_id):
    if request.method == 'GET':
        res = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=46121df91ceeaf70b4337f8759116b64&language=ko-KR')
        movie = res.json()
        movie_data = Movie.objects.get(movie_id=movie_id)
        return Response(movie)
    else:
        
        movie = Movie.objects.filter(movie_id=movie_id)[0]
        movie.rank = request.data.get('rank')
        movie.save()
        return Response(movie.rank)
    
@api_view(['GET'])

def rank(request, movie_id):
    movie = Movie.objects.filter(movie_id=movie_id)[0]
    return Response(movie.rank)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication]) # token이 유효한지 검사
@permission_classes([IsAuthenticated])
def recommended(request):
    movies = Movie.objects.filter(vote_average__gte = 7).order_by('-popularity')[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication]) # token이 유효한지 검사
@permission_classes([IsAuthenticated])
def random(request):
    movies = Movie.objects.filter(vote_average__gte = 7).order_by('-popularity')[:50]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
