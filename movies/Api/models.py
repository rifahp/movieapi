from django.db import models

# Create your models here.
movies=[
    
    {"id":1,"name":"iron man","year":2008,"director":"john Favreau","genre":"action"},
    {"id":2,"name":"captian america","year":2011,"director":"joe johnston","genre":"action"},
    {"id":3,"name":"lucifer","year":2019,"director":"prithiraj","genre":"action"},
    {"id":4,"name":"spiderman no way home","year":2021,"director":"john watts","genre":"action"},
    
    
    
]

class Movielist(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField()
    director=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)