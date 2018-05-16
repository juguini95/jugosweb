from django.contrib import admin

# Register your models here.
from .models import Choice, Question

#quitado en part 7
#admin.site.register(Question)

from django.contrib import admin

from .models import Choice, Question


#con este y el de abajo, las choices las agrega a la vista de la question
#dando 3 extra espacios para nuevas choices.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    #esto es lo que se ve en admin/polls/question/
    list_display = ('question_text', 'pub_date','was_published_recently')
    #crea un filtro por dias (relacion a pub_date)
    list_filter =['pub_date']
    #crea un buscador
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)



#con esto generaba unas nuevas pestañas para agregar los choices
'''
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
'''