from django.contrib import admin
from .models import outro,income,User,rootin,debt
# Register your models here.
admin.site.register(outro)
admin.site.register(User)
admin.site.register(income)
admin.site.register(debt)
admin.site.register(rootin)
