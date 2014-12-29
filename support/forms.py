from django import forms

class Support(forms.Form):

  amount = forms.DecimalField(
      label="Total amount (in USD)",
      initial=10.0,
      min_value=0.0
  )
  ratio = forms.DecimalField(
      label="Authors share (in %)",
      initial=90.0,
      max_value=100.0,
      min_value=0.0
  )

