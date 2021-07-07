#importing models
from django.contrib import admin
from .models import Code,Groups



# Registering the models to the admin site
admin.site.register(Code)
admin.site.register(Groups)