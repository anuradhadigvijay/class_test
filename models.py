from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    description=models.TextField(blank=True,null=True)
    location=models.CharField(max_length=30,blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    is_organizer=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


from django.contrib.auth.models import AbstractUser

TEACHER = 'Teacher'
STUDENT = 'Student'
SUPERADMIN = 'SUPERADMIN'

ROLES = [(TEACHER, 'Teacher'), (STUDENT, 'Student'),(SUPERADMIN, 'SUPERADMIN')]

class UserAccount(AbstractUser):
    role = models.CharField(max_length=10,choices=ROLES, default=STUDENT)



from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TeacherProfile(models.Model):
    user=models.OneToOne(User,limit_choices_to={'role':'Teacher'}, on_delete=models.CASCADE,related_name="teacher_profile")
    # your custom fields for teacher model

    def __str__(self):
        return self.user.username

class StudentProfile(models.Model):
    user=models.OneToOne(User,limit_choices_to={'role':'Student'}, on_delete=models.CASCADE,related_name="student_profile", read_only=True)
    # write your custom fields for student profile from here.

    def __str__(self):
        return self.user.username

class SuperadminProfile(models.Model):
    user=models.OneToOne(User,limit_choices_to={'role':'Superadmin'}, on_delete=models.CASCADE,related_name="superadmin_profile")
    # write your custom fields for student profile from here.

    def __str__(self):
        return self.user.username