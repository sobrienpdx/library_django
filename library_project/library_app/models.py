from django.db import models

# Create your models here.

class Author(models.Model):
    author = models.CharField(max_length=250)#unique makes it so that you can't repeat them
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    # once you have set up a class you have to run a migrations with python \manage.py makemigrations doDoApp. Once this is successful you should have a 0001_initial in yoru omigrations folder. After any changes to models you must make another migration. this creates instructions for migrating. python manage.py migrate then actually migrates things to the app.

    def __str__(self):
        return self.author





class Book(models.Model):
    title = models.CharField(max_length=250)#unique makes it so that you can't repeat them
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # pub_date = models.DateTimeField(default=datetime.now())
    # once you have set up a class you have to run a migrations with python \manage.py makemigrations doDoApp. Once this is successful you should have a 0001_initial in yoru omigrations folder. After any changes to models you must make another migration. this creates instructions for migrating. python manage.py migrate then actually migrates things to the app.

    def __str__(self):
        return self.title
