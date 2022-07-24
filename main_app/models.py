from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)


########################
## Add Class Toy Model
########################

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

###############
## Add Class Cat Model
################

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "Name: " + self.name + " | Breed: " + self.breed + " | Age: " + str(self.age)
    
    #Add this method
    # I need to research this function more.  I'm not understanding
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    

    
#############################
## Add class Feeding Model
#############################
# SQL models have attributes (columns)
# Django uses python classes to interface SQL models and attributes
# The model will become the new table/relation in the database catcollector
# specified in the DATABASES object in settings.py


#  A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
# new code above

class Feeding(models.Model):
    # django Meta class allows for adding
    # configuration to a Model        
    # instantiate SQL Model attributes below:
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )    
    # The line below connects the Cat relation and will delete instances of Feeding
    # when a related instance of Cat is deleted
    # to prevent bloating the Feeding relation with data of cat instances that no longer exist
    ########################
    # models.ForeignKey() field type creates 
    # a 1:M relationship 
    # btwn 2 models/relations
    ########################
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'    
    
    class Meta:
        ordering = ['-date']

#######################
## Add Class Photo Model
#######################

class Photo(models.Model):
    url = models.CharField(max_length=200)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Photo for cat_id: ' + str(self.cat_id) + '@' + self.url
