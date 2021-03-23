from django.urls import path
from . import views


urlpatterns = [
    # ~/movies/
    path('', views.index),
    path('nowplaying/', views.nowplaying),
    path('popular/', views.popular),
    path('voteaverage/', views.voteaverage),
    # ~/movies/<movie_id>/
    path('<int:movie_id>/', views.detail),
    path('<int:movie_id>/rank/', views.rank),
    path('recommend/', views.recommended),
    path('random/', views.random)
]
