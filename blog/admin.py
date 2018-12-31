from django.contrib import admin
from .models import Post, Comment, Question, Choice, Todo

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Todo)



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['created_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

