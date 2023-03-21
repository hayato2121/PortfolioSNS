from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .forms import ImageUploadForm, CommentCreateForm
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.models import User

from django.shortcuts import redirect, get_object_or_404

from .models import Post, Follow, Comment 
# Create your views here.



#自分以外の投稿を表示
class Home(LoginRequiredMixin, ListView):
    #HOMEページで、自分以外のユーザー投稿をリスト表示
    model = Post
    template_name = 'list.html'

    def get_queryset(self):
        #リクエストユーザーのみ除外
        return Post.objects.exclude(user=self.request.user)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        #get_or_createにしないとサインアップ時オブジェクトがないためエラーになる
        context['follow'] = Follow.objects.get_or_create(user=self.request.user)
        return context
    

class MyPost(LoginRequiredMixin, ListView):
    #自分の投稿のみ表示
    model = Post
    template_name = 'mypost.html'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

    
    
    
#投稿詳細ページ
class DetailPost(LoginRequiredMixin, DetailView):
   
   model = Post
   template_name = 'detail.html'

   
   def get_context_data(self, *args, **kwargs):
    #フォローに関するオブジェクト情報をコンテクストに追加
        context = super().get_context_data(*args, **kwargs)
        context['follow'] = Follow.objects.get_or_create(user = self.request.user)
        context['comment_list'] = self.object.comment_set.filter(parent__isnull=True)
        # テンプレートにコメント作成フォームを渡す
        context['comment_form'] = CommentCreateForm

        return context
   
   
   #コメント
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form_class = CommentCreateForm
    form = form_class(request.POST,request.FILES or None)

    if request.method == 'POST':
        form.instance.user = request.user
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('detail', pk=post.pk)

    context = {
        'form': form,
        'post': post
    }

    return render(request, 'comment_form.html', context)

#コメント返信
def reply_create(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    form_class = CommentCreateForm
    post = comment.post
    form = form_class(request.POST,request.FILES or None)

    if request.method == 'POST':
        form.instance.user = request.user
        reply = form.save(commit=False)
        reply.parent = comment
        reply.post = post
        reply.save()
        return redirect('detail', pk=post.pk)
        
    
    context = {
        'form': form,
        'post': post,
        'comment': comment,
    }
    return render(request, 'comment_form.html', context)


   


#投稿フォーム
class EditPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'edit.html'
    form_class = ImageUploadForm
    success_url = "/"


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    


#投稿編集
class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post 
    template_name = 'update.html'
    form_class = ImageUploadForm

    def get_success_url(self, **kwargs):
        pk = self.kwargs["pk"]
        return reverse_lazy('detail', kwargs={"pk": pk})
    
    def test_func(self, **kwargs):
        #アクセスできるものを制限
        pk = self.kwargs["pk"]
        post = Post.objects.get(pk = pk)
        return(post.user == self.request.user)
    
    


#post投稿削除
class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Post
   template_name = 'delete.html'
   success_url = reverse_lazy('mypost')

   def test_func(self, **kwargs):
       pk = self.kwargs["pk"]
       post = Post.objects.get(pk=pk)
       return (post.user == self.request.user)
   
#comment投稿削除
class DeleteComment(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Comment
   template_name = 'commentdelete.html'
   success_url = reverse_lazy('mypost')

   def test_func(self, **kwargs):
       pk = self.kwargs["pk"]
       comment = Comment.objects.get(pk=pk)
       return (comment.user == self.request.user)
   

#いいね機能
class LikeBase(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        #記事の特定
        pk = self.kwargs['pk']
        related_post = Post.objects.get(pk = pk )
        #いいねテーブルにすでに名前がある場合は、ユーザー名を消す。なかったら追加する
        if self.request.user in related_post.like.all():
            obj = related_post.like.remove(self.request.user)

        else :
            obj = related_post.like.add(self.request.user)

        return obj

    
# 画面遷移先　HOMEでいいねした場合。
class LikeHome(LikeBase):
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return redirect('home')
    
# 画面遷移先　詳細ページでいいねした場合
class LikeDetail(LikeBase):
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        pk = self.kwargs['pk']
        return redirect('detail', pk)
    



#Follor機能
class FollowBase(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        #ユーザーの特定
        pk = self.kwargs['pk']
        target_user = Post.objects.get(pk=pk).user

        #ユーザー情報によりフォローリスト作成
        my_follow = Follow.objects.get_or_create(user=self.request.user)

        #フォローリスト内にすでにユーザーがいる場合は削除、いない場合は追加
        if target_user in my_follow[0].following.all():
            obj = my_follow[0].following.remove(target_user)
        else:
            obj = my_follow[0].following.add(target_user)
        retrun : obj

#フォローした後の遷移先
class FollowHome(FollowBase):
    #homeでフォローした場合
    def get(self, request, *args, **kwargs):
        super().get(request, *args, *kwargs)
        return redirect('home')
    
class FollowDetail(FollowBase):
    #詳細画面ででフォローした場合"
    def get(self, request, *args, **kwargs):
        super().get(request, *args, *kwargs)
        pk = self.kwargs['pk']
        return redirect('detail', pk)
    
    
#フォローリスト
class FollowList(LoginRequiredMixin, ListView):
    
    model = Post
    template_name = 'list.html'

    def get_queryset(self):
        #フォローリスト内にユーザーが含まれている場合のみクエリセット返す
        my_follow = Follow.objects.get_or_create(user=self.request.user)
        all_follow = my_follow[0].following.all()
        return Post.objects.filter(user__in=all_follow)




