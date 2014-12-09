from django import forms

class Submit(forms.Form):

  title = forms.CharField(
      label="Title",
      help_text="Title of the article."
  )
  author = forms.CharField(
      label="Author",
      help_text="The name that will be displayed as the author."
  )
  email = forms.EmailField(
      label="Email",
      help_text="Your email address for additional corrispondance."
  )
  content = forms.CharField(
      label="Content",
      help_text="The article text.",
      widget=forms.Textarea(attrs={'class' : 'pagedownBootstrap'})
  )

