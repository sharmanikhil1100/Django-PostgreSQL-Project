from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author
from .serializers import AuthorSerializer, BookSerializer
import json

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
        #TODO: Get
        return HttpResponse("Author Get.")    
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
        # inputdata[authodid]
        # x= book.get(authid=ahtbid)
        # if x==none return httpresp (autho nt foudn)
        # TODO:

    if request.method=="GET":
        """
        Author GET Request. Returns all the Authors present in the database.
        """
        #TODO: Get
        return HttpResponse("Author Get.")
    return HttpResponse("Invalid Request", status=400)
