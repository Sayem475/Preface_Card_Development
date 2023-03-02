from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.CardUser)
@admin.register(models.CardUser)
class CardUserAdmin(admin.ModelAdmin):
    list_display = ("name", "card_linked", "url")

    def url(self, obj):
        return f"http://127.0.0.1:8000/profile/{models.CardUser.objects.get(id=obj.id).id}"