from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from comment.models import Comment

@login_required
def delete(request, comment_id):
  if not request.user.is_superuser:
    raise PermissionDenied
  return_url = request.GET.get('next', '/')
  comment = get_object_or_404(Comment, id=comment_id)
  if request.method == "POST":
    comment.delete()
    return HttpResponseRedirect(return_url)
  templatearguments = {
    "comment" : comment,
    "disable_comment_delete" : True,
    "generic_form" : {
      "title" : "Delete comment?",
      "submit_label" : "Delete",
      'cancel_url' : return_url,
    },
  }
  return render(request, 'comment/delete.html', templatearguments)

