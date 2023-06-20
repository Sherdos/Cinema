from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    '''Admin View for Movie'''

    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)