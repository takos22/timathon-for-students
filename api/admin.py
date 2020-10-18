from django.contrib import admin
from .models import Homework

# Register your models here.


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "subject", "name", "finished")


admin.site.register(Homework, HomeworkAdmin)
