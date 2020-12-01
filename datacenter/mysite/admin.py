from django.contrib import admin
from .models import Post
from .models import Branch,AccessInfo,Branch,StoreIncome

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post, PostAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('Name', 'manager')

admin.site.register(Branch, BranchAdmin)

class StoreIncomeAdmin(admin.ModelAdmin):
    list_display = ('branch','income_year', 'income_month','income')

admin.site.register(StoreIncome, StoreIncomeAdmin)

admin.site.register(AccessInfo)