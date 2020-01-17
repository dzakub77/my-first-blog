from django import forms

from .models import Post

class PostForm(forms.ModelForm): #nazwa naszego formularza, i informujermy ze ten formularz
    #jest formularzem module "ModelForm"

    class Meta:  # tutaj przekazujemy informacje o tym jaki model powinien byc wykorzystany do
        # stworzzenia tego formularza (model=Post)
        model = Post
        fields = ('title', 'text',) # wskazujemy które pola powinny pojawic sie w naszym formularzu