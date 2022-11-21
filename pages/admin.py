from django.contrib import admin
from .models import Team
from .models import Client
from django.utils.html import format_html

# Registered Team and Client models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 10px;" />'.format(object.photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_date')
    list_display_links = ('id', 'thumbnail','first_name',)
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin) # Registered model of Team members of Blizzard

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'phone', 'message')
    list_display_links = ('name', 'email', 'message')
    search_fields = ('name', 'subject', 'email')
    list_per_page = 10
    list_filter = ('name', 'email', 'subject')

admin.site.register(Client, ClientAdmin) #Registered client and admin model 

