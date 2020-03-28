from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ("action","Action"),
    ("comedy","Comedy"),
    ("drama","Drama"),
    ("romance","Romance"),
)

LANGUAGE_CHOICES=(
    ("english","English"),
    ("germany","Germany")
)

STATUS_CHOICES=(
    ("RA","Recently added"),
    ("MW","Most Watched"),
    ("TR","Top reted"),
)
TYPELINK_CHOICES=(
    ("D","download"),
    ("W","watch")
)
class Movie(models.Model):

    title= models.CharField(max_length=80)
    description = models.CharField(max_length=400)
    viewcount =models.IntegerField(default=0)
    image= models.ImageField(upload_to='moviePic',blank=True)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=15,blank=True)
    language=models.CharField(choices=LANGUAGE_CHOICES,max_length=15)
    yearOfProduction=models.DateField()
    status = models.CharField(choices=STATUS_CHOICES,max_length=2,blank=True)
    cast= models.CharField(max_length=100)

    def __str__(self):
        return self.title

class MovieLink(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name="movie_link")
    type= models.CharField(choices=TYPELINK_CHOICES,max_length=1)
    link= models.URLField()
    def __str__(self):
        return self.movie.title