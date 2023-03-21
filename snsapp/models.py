from django.db import models
from django.contrib.auth.models import User



# Create your models here.
#投稿機能
class Post(models.Model):
    content = models.TextField('本文')
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    #いいね機能
    like = models.ManyToManyField(User, related_name='related_post', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reversed('detail', kwargs={'pk: self.pk'})

#フォロー機能
class Follow(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return self.user.username
    
#コメント機能
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('本文')
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='対象投稿')
    parent = models.ForeignKey('self', verbose_name='親コメント', null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.content[:20]

    class Meta:
        ordering = ["-created_at"]

