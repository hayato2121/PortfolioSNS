from django import forms
from .models import Post, Comment

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','image')


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'image')