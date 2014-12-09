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

class Edit(forms.Form):

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

  def __init__(self, *args, **kwargs):  
    article = kwargs.pop("article")  
    super(Edit, self).__init__(*args, **kwargs)  
    self.fields["title"].initial = article.title 
    self.fields["author"].initial = article.author 
    self.fields["email"].initial = article.email
    self.fields["content"].initial = article.content  