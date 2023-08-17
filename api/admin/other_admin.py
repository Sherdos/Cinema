from django.contrib import admin

from api.models.models_other import Rating, RatingStar, Reviews

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star",)



admin.site.register(RatingStar)