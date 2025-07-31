from django.contrib import admin
from .models import Articles, Comments
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                  return qs
            return qs.filter(author=request.user)
    



admin.site.register(Articles)
admin.site.register(Comments)