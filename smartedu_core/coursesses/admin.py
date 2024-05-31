from django.contrib import admin
from . models import Course, Category, Tag


# Register your models here.
@admin.register(Course)
class CouurseAdmin(admin.ModelAdmin):
    list_display = ('name','available','teacher')  # admin arayüzündeki görünen column ile ilgi görmek istediğin özellikleri ekleyebilirsin
    list_filter = ('available',)
    search_fields = ('name', 'description')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}     