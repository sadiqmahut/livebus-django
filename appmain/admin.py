from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(BStop)
admin.site.register(Stops)
admin.site.register(Route)
admin.site.register(Buses)