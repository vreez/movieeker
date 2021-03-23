from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list_create),
    path('<int:review_id>/', views.review_update_delete),
    path('<int:review_id>/comments/', views.comment_list_create),
    path('<int:review_id>/comments/delete/<int:comment_id>/', views.comment_update_delete),

]
