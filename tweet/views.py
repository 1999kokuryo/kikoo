from django.shortcuts import render
from django.views.generic import ListView
from .models import Post    #.modelsは同じフォルダの中のmodels、という意味。
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "tweet/index.html"  #htmlの場所、またはファイルの名前を指定してあげる。
    context_object_name = 'posts'   #一つ一つの名前をpostsにする。
    ordering = ['-date_posted']     #表示する順番
    paginate_by = 5   #1ページに何個表示するか。