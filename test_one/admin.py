from django.contrib import admin

# Register your models here.

from test_one.models.user import User_info


class Dz_user(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'mobile')

    date_hierarchy = 'create_time'
    readonly_fields = ('create_time', 'modify_time')


admin.site.register(User_info, Dz_user)


"""创建admin用户 python3 manage createsuperuser"""