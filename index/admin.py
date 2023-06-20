from django.contrib import admin
from .models import About
from .models import Education
from .models import Experience
from .models import Project

# Register your models here.

admin.site.register(About)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)
