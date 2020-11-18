from django.contrib import admin
from .models import Quiz, QuizUser, Image, Question, Answer

# Register your models here.

admin.site.register(Quiz)
admin.site.register(QuizUser)
admin.site.register(Image)
admin.site.register(Question)
admin.site.register(Answer)

