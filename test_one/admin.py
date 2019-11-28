from django.contrib import admin

# Register your models here.

from test_one.models import user


# class Dz_user(admin.ModelAdmin):
#     list_display = ('id', 'user_id', 'name', 'mobile')
#
#     date_hierarchy = 'create_time'
#     readonly_fields = ('create_time', 'modify_time')
#
#
# admin.site.register(user_info, Dz_user)
