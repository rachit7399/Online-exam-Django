from django.contrib import admin
from quiz.models import *
# Register your models here.
myModels = [QnaCategory, Question, AnsMarked, Choices, SelectedQue]

admin.site.register(myModels)
