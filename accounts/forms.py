from django import forms
from .models import CustomUser


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'content','image','bg_image')
        widgets = {
            'username': forms.TextInput(attrs={
            'class': 'w-full p-1 sm:p-2 border-2 shadow-lg focus:outline-none hover:border-green-400 text-gray-500 rounded-lg '
            }),
            'content': forms.Textarea(attrs={
            'class': 'w-full p-1 sm:p-2 border-2 shadow-lg focus:outline-none hover:border-green-400 text-gray-500 rounded-lg '
            }),
            'image': forms.FileInput(attrs={
            'class': 'mt-3 w-4/5  rounded-2xl bg-white py-1 px-2 sm:py-2 sm:px-4 text-black border-2 shadow-lg hover:border-green-400 '
            }),
            'bg_image': forms.FileInput(attrs={
            'class': 'w-full p-1 sm:p-2 border-2 shadow-lg focus:outline-none hover:border-green-400 text-gray-500 rounded-lg '
            }),
        }
        labels = {
            'username' : 'ユーザーネーム',
            'content' : '自己紹介',
            'image' : 'アイコン画像',
            'bg_image' : 'メイン画像',
        }