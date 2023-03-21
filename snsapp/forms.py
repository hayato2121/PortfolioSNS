from django import forms
from .models import Post, Comment

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content','image')
        widgets = {
            'content': forms.Textarea(attrs={
            'class': 'w-full p-1 sm:p-2 border-2 shadow-lg focus:outline-none hover:border-green-400 text-gray-500 rounded-lg '
            }),
            'image': forms.FileInput(attrs={
            'class': 'mt-3 w-4/5  rounded-2xl bg-white py-1 px-2 sm:py-2 sm:px-4 text-black border-2 shadow-lg hover:border-green-400 '
            }),
        }
        labels = {
            'image' : 'image'
        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'image')
        widgets = {
            'content': forms.Textarea(attrs={
            'class': 'w-full p-1 sm:p-2 border-2 shadow-lg focus:outline-none hover:border-green-400 text-gray-500 rounded-lg '
            }),
            'image': forms.FileInput(attrs={
            'class': 'mt-3 w-4/5  rounded-2xl bg-white py-1 px-2 sm:py-2 sm:px-4 text-black border-2 shadow-lg hover:border-green-400 '
            }),
        }
        labels = {
            'image' : 'image'
        }
