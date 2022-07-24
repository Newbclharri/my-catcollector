# main route controller file

from django.shortcuts import redirect, render
from django.http import HttpResponse # Built in Django method for sending http responses
from .models import Cat, Toy, Photo
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'catcollector-cj'



# Faux Cat Data - Database simulation

# class Cat:
#     #constructor fxn | 'self' is like 'this' in JS
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age
        
# cats = [
#     Cat('Karis', 'tabby', 'foul little demon', 3),
#     Cat('Thor', 'tom cat', 'attention seeker', 15),
#     Cat('Sky', 'black cat', 'saver of spirits', 4)
# ]


# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ </h1>')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('cats') # I'm pretty sure the passed argument should be 'cats' instead of 'index'.  We'll see
        else:
            error_message = 'Invalid sign up - try again'
    # The only other case is that a GET request was made or the POST went wrong.
    # In this case, render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    # use HttpResponse to send back raw text or an html string
    # return HttpResponse('About Page')
    # use render fxn to send a .html template file as a response:
    return render(request, 'about.html')
    # Django knows after running the render function to look in the templates folder
    # found in main_app/templates to locate a .html template file

@login_required
def cats_index(request):
    # The cats object below is the third argument of the render fxn that is sent
    # to the cats/index.html template to iterate over
    # cats = Cat.objects.all()
    
    # only display cats pertaining to a user
    cats = Cat.objects.filter(user=request.user)
    # Alternatively:
    # cats = request.user.cat_set.all()
    return render(request, 'cats/index.html', {'cats': cats})

@login_required
def cats_detail(request, cat_id):
    # Get the individual cat
    cat = Cat.objects.get(id=cat_id)
    toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
    print('toys_not_owned:',toys_cat_doesnt_have)
    # Instantiate FeedingForm
    feeding_form = FeedingForm()
    # Render template, pass the cat to the template
    return render(request, 'cats/detail.html', 
        {
            'cat': cat, 
            'feeding_form': feeding_form,
            'toys_not_owned': toys_cat_doesnt_have
         })

@login_required
def add_feeding(request, cat_id):
    # FeedingForm is a class that will create an instance of the 
    # dictionary request.POST containing the key value pairs
    # obtain after the user completed and submitted the form
    form = FeedingForm(request.POST)
    # native django function that returns true false boolean if 
    # the user correctly complted the form
    if form.is_valid():
        # I don't know why .save(commit=False) is required
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('detail', cat_id=cat_id)

@login_required
def add_photo(request, cat_id):
    #photo-file will be the 'name' attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for s3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):] # In python, the symbol '[]' also refers to a substring w'in a string. The ': + a number' tells who many characters to extract. Ommitting a number means extract all remaining chars
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET,key)
            #build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, cat_id=cat_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', cat_id=cat_id)

@login_required
def assoc_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('detail', cat_id=cat_id)

##################
## Class Based Views
#####################
# This is an example of inheritance in python
# the class below 'CatCreate' inherits parameters and methods from the class 'CreateView'
# that was imported above

class CatCreate(LoginRequiredMixin, CreateView):
    # I still have to identify the model I'm working with
    # the Cat model is imported in this file, therefore,
    # I can specify it as the model to use for this class
    model =  Cat
    # '__all__' is a special value that specifies wo use all of the 
    # Cat model attributes
    # Alternatively, I could have written fields = ['name', 'breed', 'description', 'age']
    fields = ['name', 'breed', 'description','age']
    # The line below specifies where to send the user after submitting the form data
    # It's similar to a redirect
    
    # This inherited method is call when a 
    # valid cat form is submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)
    
class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    #exclude name field to prevent renaming a cat
    fields = ['breed', 'description', 'age']
    
class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = '/cats/'   

class ToyList(LoginRequiredMixin, ListView):
    model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy
    success_url = '/toys/'
    
class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields= '__all__'
    success_url = '/toys/'

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'