# Rest API Application

Following is an application in Django, having REST APIs with PostgreSQL Database.

### Database Schemas

- Author model Schema :\
  author_id (text, primary key)\
  name (text)\
  phone (text)\
  address (text)\
  email (Email)

- Book model Schema :\
  book_id (text, primary key)\
  name (text)\
  author_id (text, foreign key)\
  published_date (Date)\
  rating (Int)\
  price (Int)

### APIs

> GET request -
> Returns all entries of database.

> POST request -
> Add an entry into database.

> PUT request -
> Update rows in database.

a) Author Model-

> Request body format :
> {

    "author_id" : "author1",
    "name" : "chetan bhagat",
    "phone" : "1234568091",
    "address" : "iim a",
    "email" : "chetan@bhagat.com"

}

b) Book Model :

> Request body format :
> {

    "book_id": "b1",
    "name": "2 states",
    "author_id":"author1",
    "published_date":"2019-02-01",
    "rating":5,
    "price": 100

}

### Steps to run Code

For installing python libraries:

```
$ pip install requirements.txt
```

Run these set of commands for setting up the PostegreSQL on your system using docker...
Define proper user name, password and database name:

```
$ sudo docker run --name postgres_library -d -p 5432:5432 -e POSTGRES_USER=nik -e POSTGRES_PASSWORD=nikgreat -e POSTGRES_DB=library postgres
```

Do migrations for setting up database schema on your system.

```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

Start server

```
$ python3 manage.py runserver
```

Application is now running on localhost(127.0.0.1:8000/)

### Test APIs

- Used Postman application for testing CRUD operations on my application from localhost (127.0.0.1:8000/)
- Find the postman collection file: api_collection.json.
  Import it in your postman app.

### Code Standards

Code written in VS Code with using Sonarlint extension.
