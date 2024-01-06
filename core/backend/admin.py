from django.contrib import admin

# Register your models here.
from .models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'experience', 'job', 'phone')  # Displayed columns
    list_filter = ('age', 'experience', 'job')  # Filter options

admin.site.register(Users, UsersAdmin)