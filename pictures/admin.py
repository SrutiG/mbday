from django.contrib import admin

from .models import Picture
from .models import picture_people
from .models import picture_tag

admin.site.register(Picture)
admin.site.register(picture_people)
admin.site.register(picture_tag)