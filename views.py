from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def index(request):
    """
    redirect to the dialer
    """
    return HttpResponseRedirect(reverse('dialer_start'))
