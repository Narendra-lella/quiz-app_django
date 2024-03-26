from django.contrib import admin

from .models import Question,Answer,Category


class Answeradmin(admin.StackedInline):
    model = Answer

class Questionadmin(admin.ModelAdmin):
    inlines = [Answeradmin]


admin.site.register(Question, Questionadmin)

admin.site.register(Category)

    
admin.site.register(Answer)