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

    fieldsets = fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Space", {"fields": ("guests", "bed", "bedrooms", "bath")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )
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
        "count_amenities",
    )
    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("=city", "host__username")

    filter_horizontal = ("amenities", "facilities", "house_rules")

    def count_amenities(self, obj):
        return "potato"

    count_amenities.short_description = "hello"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass

