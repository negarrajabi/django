from django.http import HttpResponse
from django.template import loader
from .models import account
def detail(request, account_id):
    return HttpResponse("you're looking at account id %s." % account_id)
def index(request):
    latest_accounts_list = account.objects.order_by('-account_id')[:5]
    template = loader.get_template('accounts/index.html')
    context = {'latest_accounts_list': latest_accounts_list, }
    return HttpResponse(template.render(context,request))
