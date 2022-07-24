from django.forms import ModelForm
from . models import Feeding
from django.contrib.auth.models import User

class FeedingForm(ModelForm):
    # I don't understand why I have to use class Meta
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']