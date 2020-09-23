from django.db import models
from django_countries.fields import CountryField

gender = (
    ('Male' , 'Male') , 
    ('Female' , 'Female')
)
class Profile(models.Model):
    f_name = models.CharField(max_length = 50 , verbose_name = 'First name')
    last_Name = models.CharField(max_length = 50 , verbose_name = 'Last name')
    image = models.ImageField(upload_to = 'Profile/')
    student_id = models.AutoField(primary_key=True , verbose_name = 'Student ID')
    birthday =  models.DateField(blank=True, null=True)
    current_age = models.CharField(max_length=50 , verbose_name = 'Current age')
    gender = models.CharField(max_length = 50 , choices = gender , verbose_name = 'Gender')
    state = CountryField()
    city_street =  models.CharField(max_length=100, blank=True)
    postal_code = models.IntegerField()
    email =models.EmailField(max_length=100)
    telephone_number = models.IntegerField()
    mother_tonque = models.CharField(max_length = 70)
    payment_method = models.CharField(max_length = 50)
    created_at = models.DateTimeField()
    message = models.TextField(max_length = 500)
    def __str__(self):
        return self.f_name 
    



    

