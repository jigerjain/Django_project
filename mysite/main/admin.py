from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
# "fields" in Class used for fields setting
# "fieldsets" in Class in used for making different heading in site

class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["tutorial_title","tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Tutorial, TutorialAdmin)