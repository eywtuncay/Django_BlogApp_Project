from django.contrib import admin
from blog.forms import BlogForm
from .models import Blog, Category
from django.utils.safestring import mark_safe

class BlogAdmin(admin.ModelAdmin):
    form = BlogForm  # Blog modelinde kullanılacak form olarak BlogForm'u ayarla
    list_display = ("title","is_active","is_home","slug","selected_categories",)
    list_editable = ("is_active","is_home")
    search_fields = ("title","description")
    readonly_fields = ("slug",)
    list_filter = ("is_active","is_home","categories",)

    def selected_categories(sefl, obj):
        html = "<ul>"

        for category in obj.categories.all():
            html += "<li>" + category.name + "</li>"
        html += "</ul>"

        return mark_safe(html)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug")
    readonly_fields = ("slug",)

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)

