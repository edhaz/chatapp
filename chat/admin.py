from django.contrib import admin

from .models import Chatter, Message

admin.site.register(Chatter)
admin.site.register(Message)

