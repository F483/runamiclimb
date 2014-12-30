from django import forms
from captcha.fields import CaptchaField

class Comment(forms.Form):

  alias = forms.CharField(
      label="Name",
  )

  content = forms.CharField(
      label="Content",
      widget=forms.Textarea(attrs={'rows' : '3'})
  )

  captcha = CaptchaField()

