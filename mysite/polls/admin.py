from django.contrib import admin

# Register your models here.

from .models import Question,Choice


class ChoiceInline(admin.TabularInline):
    model = Choice # 使用的模型
    extra = 0 # 额外的关联项


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}), # admin页面的显示顺序
        ('Date information', {'fields': ['pub_date']}), # 标题栏
    ]
    inlines = [ChoiceInline] # 关联的模型
    list_display = ('question_text', 'pub_date', 'was_published_recently') # 列表显示内容
    list_filter = ['pub_date'] # 列表排序规则
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
