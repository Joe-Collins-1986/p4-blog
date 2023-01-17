from django.contrib import admin
from .models import Post, Comment, Box
from map.models import Country, Visit

# class CountryAdmin(admin.ModelAdmin):
    
#     prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Box)

admin.site.register(Country)
admin.site.register(Visit)