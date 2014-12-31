from django import forms

class Create(forms.Form):

  title = forms.CharField(label="Title")
  content = forms.CharField(
      label="Content",
      widget=forms.Textarea(attrs={
          'class' : 'pagedownBootstrap',
          'rows' : '10'
      })
  )
  in_sidebar = forms.BooleanField(label="In sidebar", required=False)
  sidebar_ordering = forms.IntegerField(
      label="Sidebar ordering position",
      initial=0
  )

class Edit(Create):

  def __init__(self, *args, **kwargs):
    page = kwargs.pop("page")
    super(Edit, self).__init__(*args, **kwargs)
    self.fields["title"].initial = page.title
    self.fields["content"].initial = page.content
    self.fields["in_sidebar"].initial = page.in_sidebar
    self.fields["sidebar_ordering"].initial = page.sidebar_ordering

