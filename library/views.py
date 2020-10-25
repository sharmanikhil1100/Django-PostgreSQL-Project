from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author
from .serializers import AuthorSerializer, BookSerializer
import json
from django.core.serializers import serialize

def index(request):
    return HttpResponse("Ssup bro")    

def author(request):
    
    if request.method=="POST":
        input_data=json.loads(request.body)      
        author_serializer = AuthorSerializer(data=input_data)
        if not author_serializer.is_valid():
            return HttpResponse(json.dumps(author_serializer.errors), status=400)
        author_serializer.save()

        return HttpResponse(json.dumps({"message":"Author added to Database"}), status=201)

    if request.method=="GET":
       return HttpResponse(serialize('json',Author.objects.all()))

    return HttpResponse("Invalid Request", status=400)

def book(request):
    
    if request.method=="POST": 
        input_data=json.loads(request.body)      
        book_serializer = BookSerializer(data=input_data)
        if not book_serializer.is_valid():
            return HttpResponse(json.dumps(book_serializer.errors), status=400)
        book_serializer.save()
        return HttpResponse(json.dumps({"message":"Book added to Database"}), status=201)
    
    if request.method=="PUT":

        input_data = json.loads(request.body)        
        try :
            book = Book.objects.get(book_id=input_data['book_id'])
            book.published_date=input_data['published_date']
            book.name=input_data['name']            
            # book.author_id=input_data['author_id']
            book.rating=input_data['rating']                        
            book.price=input_data['price']
            book.save()
            return HttpResponse(json.dumps({"message":"Book updated in Database"}))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({'message':'Given book not found in Database'}))           


    if request.method=="GET":
        """
        Author GET Request. Returns all the Authors present in the Database.
        """
        return HttpResponse(serialize('json',Book.objects.all()))
    return HttpResponse("Invalid Request", status=400)
