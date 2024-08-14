from django.contrib import admin
from .models import PreInstalledDeck, PreInstalledCard

@admin.register(PreInstalledDeck)
class PreInstalledDeckAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author')
    search_fields = ('title', 'author')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'author')
    fieldsets = (
        ('Group Information', {
            'fields': ('title', 'author')
        }),
        ('Date Information', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    


@admin.register(PreInstalledCard)
class PreInstalledCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author', 'group')
    search_fields = ('title', 'author')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'author')
    fieldsets = (
        ('Card Information', {
            'fields': ('title', 'content', 'group', 'author', )
        }),
        ('Date Information', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )