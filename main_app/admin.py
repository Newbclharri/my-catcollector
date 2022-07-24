from django.contrib import admin
# import models below:
from . models import Cat, Feeding, Photo

# Register models here:
admin.site.register(Cat)
admin.site.register(Feeding)
admin.site.register(Photo)
