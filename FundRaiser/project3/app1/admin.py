from django.contrib import admin
from app1.models import UserProfileCore
from app1.models import Donate, OrganizationName

# Register your models here.
admin.site.register(UserProfileCore)
admin.site.register(Donate)
admin.site.register(OrganizationName)