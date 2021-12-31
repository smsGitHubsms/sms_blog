from . models import blog
from django import forms

class blogforms(forms.ModelForm):
    class Meta:
        model=blog
        fields=['heading','date','desc','img']
# the name field not given as the name should not be edited because the name is taken from request.user


class Blogpostform(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['heading','date','desc','name','img']
