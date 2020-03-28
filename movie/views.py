from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Movie,MovieLink
# Create your views here.


def index(request):
    return render(request,'movie/index.html')

class MovieList (ListView):
    model = Movie
    paginate_by = 2

class MovieDetails(DetailView):
    model = Movie
    GET_OBJECT_CALL = 0

    def get_object(self, queryset=None):
        movie =super(MovieDetails,self).get_object()
        self.GET_OBJECT_CALL +=1
        if self.GET_OBJECT_CALL==1:
            movie.viewcount +=1
        movie.save()
        return movie

    def get_context_data(self, **kwargs):
        context= super(MovieDetails,self).get_context_data(**kwargs)
        context['links'] = MovieLink.objects.filter(movie=self.get_object())
        return context
class MovieCategory(ListView):
    model = Movie
    def get_queryset(self):
        self.category=self.kwargs['category']
        return Movie.objects.filter(category=self.category)
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(MovieCategory,self).get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context

class MovieLanguage(ListView):
    model = Movie
    def get_queryset(self):
        self.language=self.kwargs['language']
        print(self.language)
        return Movie.objects.filter(language=self.language)
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(MovieLanguage,self).get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context

class MovieSearch(ListView):
    model = Movie
    def get_queryset(self):
        query= self.request.GET.get("query")
        if query:
            return Movie.objects.filter(title__icontains=query)
        else:
            return Movie.objects.none()
