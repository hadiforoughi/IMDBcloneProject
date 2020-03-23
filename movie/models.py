from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ("A","Action"),
    ("C","Comedy"),
    ("D","Drama"),
    ("R","Romance"),
)

LANGUAGE_CHOICES=(
    ("EN","English"),
    ("Ge","Germany")
)

STATUS_CHOICES=(
    ("RA","Recently added"),
    ("MW","Most Watched"),
    ("TR","Top reted"),
)
class Movie(models.Model):

    title= models.CharField(max_length=80)
    description = models.CharField(max_length=400)
    viewcount =models.IntegerField(default=0)
    image= models.ImageField(upload_to='movie',blank=True)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=1,blank=True)
    language=models.CharField(choices=LANGUAGE_CHOICES,max_length=2)
    yearOfProduction=models.DateField()
    status = models.CharField(choices=STATUS_CHOICES,max_length=2,blank=True)

    def __str__(self):
        return self.title
