from django.contrib import admin

# Register your models here.
from .models import Person
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'roll_no', 'password']

admin.site.register(Person, PersonAdmin)
