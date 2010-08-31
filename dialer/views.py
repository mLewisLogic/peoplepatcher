from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from dialer.forms import DialerForm
from dialer.util import add_to_conference

def start(request):
    """
    Renders a form for starting a new dial
    """
    form = DialerForm(request.POST or None)
    if form.is_valid():
        call = form.save()
        call.sid1 = add_to_conference(call.id, call.number1, call.name1, call.name2)
        call.sid2 = add_to_conference(call.id, call.number2, call.name2, call.name1)
        call.save()
        
        return redirect('dialer_dialed')
    
    return render_to_response(
        'dialer/start.html',
        {'form': form},
        context_instance = RequestContext(request)
    )

def dialed(request):
    return render_to_response(
        'dialer/dialed.html',
        {},
        context_instance = RequestContext(request)
    )

def conf(request):
    return render_to_response(
        'dialer/conf.xml',
        {'confid': request.GET.get('confid', ''),
         'from_name': request.GET.get('from_name', ''),
         'to_name': request.GET.get('to_name', ''),},
        context_instance = RequestContext(request)
    )