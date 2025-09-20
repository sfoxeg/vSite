from django.contrib import admin
from user.models import User, UserProfile, Climbing


class UserProfileDocAdmin(admin.TabularInline):
    model = UserProfile
    fields = list_display = ['goal', 'first_name', 'last_name', 'description', 'city', 'height', 'weight', 'avatar']
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'profile__first_name', 'profile__last_name','is_active', 'sex', 'age', 'date_of_birth']
    list_filter = ['is_active', 'sex', 'is_superuser']
    inlines = [UserProfileDocAdmin]

@admin.register(Climbing)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id',]
    # list_filter = ['is_active', 'sex', 'is_superuser']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'goal', 'user__sex', 'city']
    list_filter = ['goal', 'city', 'height', 'weight']

    # def age(self, obj):
    #     return str(obj.user.age)
