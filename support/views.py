import uuid
from decimal import Decimal
from django.shortcuts import render
from article.models import Article
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from paypal.standard.forms import PayPalPaymentsForm
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from config import settings

def support(request, article_id, amount, ratio):
  article = get_object_or_404(Article, id=article_id)
  if not article.issue.published and not request.user.is_superuser:
    raise PermissionDenied

  amount = Decimal(amount)
  if amount < Decimal("0.0"):
    raise PermissionDenied
  ratio = Decimal(ratio)
  if ratio < Decimal("0.0") or ratio > Decimal("100.0"):
    raise PermissionDenied

  item_name = "%i_%f_%f_%s" % (article.id, amount, ratio, article.title_slug())
  url_prefix = "http://www.trainlessmagazine.com/support"
  return_url = "%s/thanks/%s/%s.html" % (
      url_prefix, article.id, article.title_slug()
  )
  cancel_return = "%s/cancel/%s/%s.html" % (
      url_prefix, article.id, article.title_slug()
  )
  paypal_dict = {
      "business": settings.PAYPAL_RECEIVER_EMAIL,
      "amount": amount,
      "item_name": item_name,
      "invoice": str(uuid.uuid4()),
      "notify_url": "http://www.trainlessmagazine.com" + reverse('paypal-ipn'),
      "return_url": return_url,
      "cancel_return": cancel_return,
  }
  templatearguments = { 
      "amount" : amount,
      "ratio" : ratio * 100,
      "article" : article,
      "author_share" : amount * ratio,
      "form": PayPalPaymentsForm(initial=paypal_dict, button_type="donate"),
      "currentcategory" : article.category,
      "currentissue" : article.issue,
  }
  return render(request, "support/support.html", templatearguments)

@csrf_exempt # for paypal
def paypal_return(request, article_id, template):
  article = get_object_or_404(Article, id=article_id)
  if not article.issue.published and not request.user.is_superuser:
    raise PermissionDenied
  templatearguments = {
    "article" : article,
    "currentcategory" : article.category,
    "currentissue" : article.issue,
  }
  return render(request, template, templatearguments)

