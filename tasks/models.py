from django.db import models 
from django.contrib.auth.models import User  # Using Django's built-in User model

from django.db.models.signals import post_save,post_delete # automatic triggers
from django.dispatch import receiver           # automatic triggers

# Create your models here.

# we do not need to modify the teams 
class Team(models.Model): # One user can be a team
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='teams')

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    
    private = models.BooleanField(blank=False,default=False) # if it is false every one can see it , users & teams associated 
    creator = models.ForeignKey(User,on_delete=models.CASCADE, related_name='created_tasks')

    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    description = models.TextField(blank=True)
    
    users = models.ManyToManyField(User, related_name='tasks')  # Users assigned to the task
    teams = models.ManyToManyField(Team, related_name='tasks' , blank=True)  # Teams related to the task
    subtasks = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='parent_tasks')  # Optional sub-task linkage

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    

class UserProfile(models.Model):
    #one-to-one relation ship 
    user = models.OneToOneField(User, on_delete=models.CASCADE)# if we delete user we delete theri profile too
    description = models.TextField(blank=True)
    image = models.ImageField(max_length=500,default="profile_pictures/placeholder.png",upload_to="profile_pictures")
    
    def __str__(self):
        return self.user.username




# Automatically create a UserProfile whenever a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


 
# when user is deleted it Automatically cuts of all the relations user had.
@receiver(post_delete, sender=User) 
def remove_user_from_related(sender, instance, **kwargs):
    instance.tasks.clear()
    instance.teams.clear()
    
# when team is deleted program automatically cuts of all the relations team had.
@receiver(post_delete, sender=Team)
def remove_team_related(sender, instance, **kwargs):
    instance.tasks.clear()
    
# when task is deleted program automatically cuts of all the relations task had.
@receiver(post_delete, sender=Task)
def remove_tasks_related(sender, instance, **kwargs):
    instance.teams.clear()
    instance.users.clear()