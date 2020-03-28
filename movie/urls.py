from django.urls import path
from . import views

app_name = "movie"
urlpatterns = [
    path('', views.MovieList.as_view(), name="movie_list"),
    path('category/<str:category>', views.MovieCategory.as_view(), name="movie_category"),
    path('language/<str:language>', views.MovieLanguage.as_view(), name="movie_language"),
    path('search/', views.MovieSearch.as_view(), name="movie_search"),
    path('<int:pk>', views.MovieDetails.as_view(), name="movie_detail")
]
