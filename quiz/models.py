from django.db import models
import uuid
from authentication.models import User, BaseModel
# Create your models here.


class QnaCategory(BaseModel):

    category_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.category_name)


class Question(BaseModel):

    question = models.CharField(max_length=100, null=True, blank=True)
    category_type = models.ForeignKey(
        QnaCategory, on_delete=models.CASCADE, related_name="question_set_category")
    is_multiple_choice = models.BooleanField(default=True)
    is_mandatory = models.BooleanField(default=True)
    marks = models.IntegerField()
    answer = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'question'


class AnsMarked(BaseModel):

    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="question_ans_marked")
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="user_ans_marked")
    answer_marked = models.CharField(max_length=100, null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    marks_got = models.IntegerField(default=0)


class Choices(BaseModel):

    question = models.OneToOneField(
        Question, on_delete=models.CASCADE, related_name="choice_set_question")
    choice_1 = models.CharField(max_length=100, null=True, blank=True)
    choice_2 = models.CharField(max_length=100, null=True, blank=True)
    choice_3 = models.CharField(max_length=100, null=True, blank=True)
    choice_4 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.question.question)

    class Meta:
        db_table = 'choice'


class SelectedQue(BaseModel):

    ques_sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="select_que_sender")
    question = models.ManyToManyField(
        Question, related_name="select_set_question", blank=True)
    ques_receiver = models.ForeignKey(User, on_delete=models.CASCADE,
                                      related_name="select_que_receiver",
                                      null=True,
                                      blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.ques_receiver.first_name)

    class Meta:
        db_table = 'selected_que'
