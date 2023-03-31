from django.contrib import admin
from .models import Score

class ScoreAdmin(admin.ModelAdmin): 
    fieldsets =  [
        (None, {'fields': ['user_id','score']}),
    ]
    search_fields = ['user_id']

admin.site.register(Score, ScoreAdmin)