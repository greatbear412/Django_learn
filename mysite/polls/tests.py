import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Question

# Create your tests here.

class QuestionMethodTest(TestCase):
    def test_was_published_question_with_future_time(self):
        """
            在将来发布的应该返回False
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time,question_text="qweqweqwe")
        self.assertIs(future_question.was_published_recently(), False)
