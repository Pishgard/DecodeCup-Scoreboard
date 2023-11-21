from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit/", views.submit_form, name="submit"),
    path("board/<int:id>/", views.board, name="board"),
    path('submit-list/', views.submit_list, name='submit-list'),
]