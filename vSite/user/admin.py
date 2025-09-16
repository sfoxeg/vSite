from django.contrib import admin
from user.models import User, UserProfile


class UserProfileDocAdmin(admin.TabularInline):
    model = UserProfile
    fields = list_display = ['acting', 'first_name', 'last_name', 'description', 'city', 'height', 'weight', 'avatar']
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'sex', 'age', 'date_of_birth']
    list_filter = ['is_active', 'sex', 'is_superuser']
    inlines = [UserProfileDocAdmin]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'acting', 'user__sex', 'city']
    list_filter = ['acting', 'city', 'height', 'weight']

    # def age(self, obj):
    #     return str(obj.user.age)
