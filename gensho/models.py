from django.db import models
from django.utils import timezone
import pytz
import datetime


class Post(models.Model):
    '''投稿される現象'''

    title = models.CharField('現象', max_length=50, default='Gensho #')
    text = models.TextField('本文')
    post_user = models.CharField('投稿ユーザー名', max_length=50)
    star = models.IntegerField('獲得スター数', default=0)
    created_at = models.DateTimeField('投稿日', auto_now_add=True)

    def __str__(self):
        return self.title + str(self.pk) + ' ' + self.text[:10]

    def get_days_ago(self):
        now = datetime.datetime.now()
        timezones = pytz.timezone('Asia/Tokyo')
        now = timezones.localize(now)
        delta = now - self.created_at
        if (delta.days >= 1):
            return True
        else:
            return False


class Comment(models.Model):
    '''現象に対してつけられるコメント'''

    comment_user = models.CharField('投稿ユーザー名', max_length=50)
    text = models.TextField('本文')
    vote_star = models.IntegerField('獲得スター数', default=0)
    created_at = models.DateTimeField('コメント作成日', auto_now_add=True)
    post = models.ForeignKey(
        Post,
        verbose_name='紐づく現象',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.comment_user
