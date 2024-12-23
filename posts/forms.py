from django import forms

class Post_Form(forms.Form):
    image =forms.ImageField()
    title = forms.CharField()
    content = forms.CharField()
    rate = forms.CharField()
    
    def clean(self):
        data = super().clean()
        title = data.get("title")
        content = data.get("content")
        if title.lower() == content.lower():
            raise forms.ValidationError("Title and content must be different")
        return data