'''
you need to run this command to update the database after working in this file
> python manage.py makemigrations
> python manage.py migrate
'''
from django.db import models
from django.utils import timezone

#import user model cz the user and the post will have a relationship
#since users r going to author posts
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    #here we write the 'now' without '()' like now(), we just want to
    #pass the function as argument, we dont want to execute it at this moment
    date_posted = models.DateTimeField(default=timezone.now)


    #the user can have multiple posts, but the post must have only one user
    #we do this here by use the foreignkey
    '''
    In Django, a ForeignKey is used to create a many-to-one relationship between two models. 
    In this case, the author field is a foreign key to the User model, which represents the
    user who created the current model instance
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    '''
    The 'on_delete' argument specifies the behavior to adopt when the referenced object is deleted.
    In this case, 'models.CASCADE' means that when a User instance is deleted, 
    all instances of the current model that have that User instance as their 
    author field will also be deleted.
    '''

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})