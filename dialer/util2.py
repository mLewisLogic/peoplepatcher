import re
import twilio
import urllib
from xml.dom.minidom import parseString

# Twilio REST API version
API_VERSION = '2008-08-01'

# Twilio AccountSid and AuthToken
ACCOUNT_SID = 'AC6883c41fcf6439d76d2a7c00e7c4c2b2'
ACCOUNT_TOKEN = 'd9d73a1f93beb86cd7544c47be0aece0'

# Outgoing Caller ID previously validated with Twilio
CALLER_ID = '(917) 725-5148';

# Create a Twilio REST account object using your Twilio account ID and token
account = twilio.Account(ACCOUNT_SID, ACCOUNT_TOKEN)

def add_to_conference(confid, number, from_name, to_name):
    params = {
        'confid':confid,
        'from_name':from_name,
        'to_name':to_name,
    }
    d = {
        'Caller' : CALLER_ID,
        'Called' : number,
        'Url' : 'http://peoplepatcher.com/dialer/conf?%s' % urllib.urlencode(params),
        'IfMachine': 'Hangup',
        'Timeout': '20',
        'Method': 'GET',
    }
    
    response = account.request('/%s/Accounts/%s/Calls' % (API_VERSION, ACCOUNT_SID), 'POST', d)
    dom = parseString(response)
    return dom.getElementsByTagName('Sid')[0].childNodes[0].data
