from django.contrib import admin

from test_movie.models import Manga, Type, Comment, Genre

# Register your models here.

admin.site.register(Manga)
admin.site.register(Type)
admin.site.register(Genre)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['user', 'manga']

    def get_form(self, request, obj=None, **kwargs):
        form = super(CommentAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user

        if str(request.user) != 'admin':
            form.base_fields['user'].initial = request.user

        return form
