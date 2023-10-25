from django.urls import path
from . import views

urlpatterns = [
    path('api/Articles', views.ArticleListCreate.as_view()),
    path('api/Articles/<int:pk>', views.ArticleAction.as_view()),

    path('api/Authors', views.AuthorListCreate.as_view()),
    path('api/Authors/<int:pk>', views.AuthorAction.as_view()),

    path('api/Comments', views.CommentListCreate.as_view()),
    path('api/Comments/<int:pk>', views.CommentAction.as_view()),
]
