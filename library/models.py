from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator

class Author(models.Model):
    author_id = models.TextField(primary_key = True)
    name = models.TextField(max_length=50)
    phone = models.TextField(max_length=10, validators=[MinLengthValidator(10)])
    address = models.TextField(max_length=100)
    email = models.EmailField(max_length=50)

class Book(models.Model):
    book_id = models.TextField(primary_key = True)
    name = models.TextField(max_length=50)
    author_id = models.ForeignKey(Author, on_delete = models.CASCADE)
    published_date = models.DateField()
    rating = models.IntegerField(        
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    price = models.IntegerField(
        # default=0,
        validators=[            
            MinValueValidator(0)
        ]
    )