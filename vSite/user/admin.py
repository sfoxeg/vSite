from django.contrib import admin
from user.models import User, UserProfile, Climbing


class UserClimbingDocAdmin(admin.StackedInline):
    model = Climbing
    fields = list_display = ['leading', 'where_leading', 'bouldering', 'where_bouldering', 'alpinism', 'belay',
                             'belay_description']
    extra = 0


class UserProfileDocAdmin(admin.StackedInline):
    model = UserProfile
    fields = list_display = ['goal', 'first_name', 'last_name', 'description', 'city', 'height', 'weight', 'avatar']
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'profile__first_name', 'profile__last_name', 'is_active', 'sex', 'age', 'date_of_birth']
    list_filter = ['is_active', 'sex', 'is_superuser']
    inlines = [UserProfileDocAdmin]


@admin.register(Climbing)
class UserAdmin(admin.ModelAdmin):
    list_display = ['profile__first_name', 'profile__last_name', 'leading', 'where_leading', 'bouldering',
                    'where_bouldering', 'alpinism', 'belay', 'belay_description']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'goal', 'city', 'height', 'weight']
    list_filter = ['goal', 'city', 'height', 'weight']
    inlines = [UserClimbingDocAdmin]

    # def name(self, obj):
    #     return f'{obj.first_name} {obj.last_name}'
