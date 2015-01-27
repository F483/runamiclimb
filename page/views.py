from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from page.models import Page
from page import forms

@login_required
def create(request):
  if not request.user.is_superuser:
    raise PermissionDenied
  if request.method == "POST":
    form = forms.Create(request.POST)
    if form.is_valid():
      page = Page()
      page.title = form.cleaned_data["title"].strip()
      page.content = form.cleaned_data["content"]
      page.in_sidebar = form.cleaned_data["in_sidebar"]
      page.sidebar_ordering = form.cleaned_data["sidebar_ordering"]
      page.save()
      return HttpResponseRedirect(page.url())
  else: # "GET"
    form = forms.Create()
  templatearguments = {
    "generic_form" : {
      "title" : "Create Page",
      "cancel_url" : "/",
      "form" : form,
    }
  }
  return render(request, 'common/submit.html', templatearguments)

@login_required
def edit(request, page_id):
  if not request.user.is_superuser:
    raise PermissionDenied
  page = get_object_or_404(Page, id=page_id)
  if request.method == "POST":
    form = forms.Edit(request.POST, page=page)
    if form.is_valid():
      page.title = form.cleaned_data["title"].strip()
      page.content = form.cleaned_data["content"]
      page.in_sidebar = form.cleaned_data["in_sidebar"]
      page.sidebar_ordering = form.cleaned_data["sidebar_ordering"]
      page.save()
      return HttpResponseRedirect(page.url())
  else: # "GET"
    form = forms.Edit(page=page)
  templatearguments = {
    "generic_form" : {
      "title" : "Edit Page",
      "cancel_url" : page.url(),
      "form" : form,
    }
  }
  return render(request, 'common/submit.html', templatearguments)



@login_required
def delete(request, page_id):
  if not request.user.is_superuser:
    raise PermissionDenied
  page = get_object_or_404(Page, id=page_id)
  if request.method == "POST":
    page.delete()
    return HttpResponseRedirect("/")
  templatearguments = {
    "generic_form" : {
      "title" : "Delete page?",
      "submit_label" : "Delete",
      'cancel_url' : page.url(),
    },
  }
  return render(request, 'common/submit.html', templatearguments)


def display(request, page_id):
  page = get_object_or_404(Page, id=page_id)
  return render(request, 'page/display.html', { "page" : page })

def subscribe(request):
  return render(request, 'page/subscribe.html', {})

