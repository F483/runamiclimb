from django import forms
from article.models import Issue
from article.models import Category
from captcha.fields import CaptchaField


class Submit(forms.Form):

  # Article content
  title = forms.CharField(
      label="Title",
      help_text="Title of the article"
  )
  content = forms.CharField(
      label="Article",
      widget=forms.Textarea(attrs={'rows' : '10'})
  )

  # Author info
  author = forms.CharField(
      label="Author",
      help_text="Author's name"
  )
  email = forms.EmailField(
      label="Email"
  )
  coverletter = forms.CharField(
      label="Cover Letter",
      help_text="Author bio and previous publications",
      widget=forms.Textarea(attrs={'rows' : '5'})
  )

  captcha = CaptchaField()


class Edit(forms.Form):

  # Article content
  title = forms.CharField(
      label="Title",
      help_text="Title of the article."
  )
  preview = forms.CharField(
      label="Preview",
      help_text="The article preview.",
      widget=forms.Textarea(attrs={
          'class' : 'pagedownBootstrap',
          'rows' : '5'
      })
  )
  content = forms.CharField(
      label="Content",
      help_text="The article text.",
      widget=forms.Textarea(attrs={
          'class' : 'pagedownBootstrap',
          'rows' : '10'
      })
  )

  # Author info
  author = forms.CharField(
      label="Author",
      help_text="The name that will be displayed as the author."
  )
  coverletter = forms.CharField(
      label="Cover Letter",
      help_text="Author bio and previous publications",
      widget=forms.Textarea(attrs={
          'class' : 'pagedownBootstrap',
          'rows' : '5'
      })
  )

  # Publishing info
  category = forms.ModelChoiceField(
      label="Category",
      queryset=Category.objects.all(),
      required=False
  )
  featured = forms.BooleanField(label="Featured", required=False)
  date = forms.DateField(
    label="Date",
    help_text="Future dates will automaticly not be listed.",
    widget=forms.widgets.DateInput(attrs={'class' : 'datepicker'}),
  )

  def __init__(self, *args, **kwargs):
    article = kwargs.pop("article")
    super(Edit, self).__init__(*args, **kwargs)
    self.fields["title"].initial = article.title
    self.fields["author"].initial = article.author
    self.fields["coverletter"].initial = article.coverletter
    self.fields["preview"].initial = article.preview
    self.fields["content"].initial = article.content
    self.fields["category"].initial = article.category
    self.fields["featured"].initial = article.featured
    self.fields["date"].initial = article.date

