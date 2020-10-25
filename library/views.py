from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author
from .serializers import AuthorSerializer, BookSerializer
from django.core.serializers import serialize
import json

def index(request):
    return HttpResponse("School Library.")    

def author(request):
    
    if request.method=="POST":
        """
        Author POST Request. Add author entry into database.
        """
        input_data=json.loads(request.body)      
        author_serializer = AuthorSerializer(data=input_data)
        if not author_serializer.is_valid():
            return HttpResponse(json.dumps(author_serializer.errors), status=400)
        author_serializer.save()

        return HttpResponse(json.dumps({"message":"Author added to Database"}), status=201)
    
    if request.method=="PUT":

        input_data = json.loads(request.body)
        """
        Author PUT Request. Update rows in database.
        """     
        try :
            author = Author.objects.get(author_id=input_data['author_id'])
            author_serializer = AuthorSerializer(author, data= input_data)
            if not author_serializer.is_valid():
                return HttpResponse(json.dumps(author_serializer.errors), status=400)
            author_serializer.save()
            return HttpResponse(json.dumps({"message":"Author updated in Database"}))
        except Author.DoesNotExist as e:
            print(e)            
            return HttpResponse(json.dumps({'message':'Given author not found in Database'}), status=400)           
        except Exception as e: 
            print(e)           
            return HttpResponse(json.dumps({'message':'Internal Error'}), status=500)

    if request.method=="GET":
        """
        Author GET Request. Returns all authors present in the database.
        """
       return HttpResponse(serialize('json',Author.objects.all()))

    return HttpResponse("Invalid Request", status=400)

def book(request):
    
    if request.method=="POST": 
        """
        Book POST Request. Add book entry into database.
        """
        input_data=json.loads(request.body)      
        book_serializer = BookSerializer(data=input_data)
        if not book_serializer.is_valid():
            return HttpResponse(json.dumps(book_serializer.errors), status=400)
        book_serializer.save()
        return HttpResponse(json.dumps({"message":"Book added to Database"}), status=201)
    
    if request.method=="PUT":
        """
        Book PUT Request. Update rows in Book database.
        """
        input_data = json.loads(request.body)        
        try :
            book = Book.objects.get(book_id=input_data['book_id'])
            book_serializer = BookSerializer(book, data= input_data)
            if not book_serializer.is_valid():
                return HttpResponse(json.dumps(book_serializer.errors), status=400)
            book_serializer.save()
            return HttpResponse(json.dumps({"message":"Book updated in Database"}))
        except Book.DoesNotExist as e:
            print(e)            
            return HttpResponse(json.dumps({'message':'Given book not found in Database'}), status=400)           
        except Exception as e: 
            print(e)           
            return HttpResponse(json.dumps({'message':'Internal Error'}), status=500)

    if request.method=="GET":
        """
        Book GET Request. Returns all the Books present in the database.
        """
        return HttpResponse(serialize('json',Book.objects.all()))
    return HttpResponse("Invalid Request", status=400)
