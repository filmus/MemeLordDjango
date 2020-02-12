from django import forms

from memelordapp.models import Post


class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddPostForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        obj = super(AddPostForm, self).save(*args, **kwargs)
        if self.request:
            obj.author = self.request.user
        obj.save()
        return obj

    class Meta:
        model = Post
        fields = ['title', 'content']
