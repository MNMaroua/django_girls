from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md'}),
            'text': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded-md'}),
        }