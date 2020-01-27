import datetime
from django.utils import timezone
from django.db import models
from django.forms import ModelForm

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1)<=self.pub_date<=now

    was_published_recently.admin_order_field = 'pub_date' # admin页面列表页面排序规则
    was_published_recently.boolean = True # 图标显示，False则是文字显示，很丑
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'