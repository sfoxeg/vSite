from django.contrib import admin
from chat.models import Chat, ChatUser, Message


@admin.register(Chat)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', ]
    list_filter = ['name', 'created_at', ]


@admin.register(ChatUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['chat', 'user', 'joined', ]


@admin.register(Message)
class UserAdmin(admin.ModelAdmin):
    list_display = ['chat', 'sender', 'is_Read', 'created_at', 'text', ]
    list_filter = ['chat', 'sender', 'is_Read', 'created_at',]
