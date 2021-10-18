from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):   #models.pyはそもそも、データベースを作るときに使う
    content = models.TextField()    #ツイート内容について
    author = models.ForeignKey(User, on_delete=models.CASCADE)    #データベースの関係性についてのもの。一人が何回も投稿できる。
    #必ずon_deleteを設定する必要がある。User登録を消したときに投稿をどうするか。
    date_posted = models.DateTimeField(default=timezone.now)    #よくある時間の設定の仕方。
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):  #投稿一覧を管理者が見られるようにするためのもの。これがないとただの数字しか表示されない。
        return self.content()