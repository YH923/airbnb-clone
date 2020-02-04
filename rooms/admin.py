from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "bed",
        "bedrooms",
        "bath",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = ("instant_book", "city", "country")

    search_fields = ("=city", "host__username")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass

