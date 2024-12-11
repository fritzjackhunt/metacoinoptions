from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def homee(request):
    return render(request, 'metacoin/index.html')

def test(request):
    return render(request, 'metacoin/test.html')

def ourteam(request):
    return render(request, 'metacoin/ourteam.html')

def awards(request):
    return render(request, 'metacoin/awards.html')

def segregated(request):
    return render(request, 'metacoin/segregated.html')

def disclosure(request):
    return render(request, 'metacoin/disclosure.html')

def terms(request):
    return render(request, 'metacoin/terms.html')

def policy(request):
    return render(request, 'metacoin/policy.html')

def laundering(request):
    return render(request, 'metacoin/laundering.html')

def audit(request):
    return render(request, 'metacoin/audit.html')

def trade_risk(request):
    return render(request, 'metacoin/trade_risk.html')

def bonus(request):
    return render(request, 'metacoin/bonus.html')

def forex_essentials(request):
    return render(request, 'metacoin/forex_essentials.html')

def exchange_rates(request):
    return render(request, 'metacoin/exchange_rates.html')

def analysis(request):
    return render(request, 'metacoin/analysis.html')

def technical_analysis(request):
    return render(request, 'metacoin/technical_analysis.html')

def forex(request):
    return render(request, 'metacoin/forex.html')

def precious_metals(request):
    return render(request, 'metacoin/precious_metals.html')

def cfd_shares(request):
    return render(request, 'metacoin/cfd_shares.html')

def cfd_indices(request):
    return render(request, 'metacoin/cfd_commodities.html')

def cfd_crypto(request):
    return render(request, 'metacoin/cfd_crypto.html')

def leverage(request):
    return render(request, 'metacoin/leverage.html')

def contact(request):
    if request.method == "POST":
        contact_fname = request.POST['fname']
        contact_lname = request.POST['lname']
        contact_email = request.POST['email']
        contact_message = request.POST['message']

        send_mail(
            contact_fname, 
            contact_message,
            contact_email,
            ['info.metacoinoptions@gmail.com'],
            fail_silently = False,
        )


        return render(request, 'metacoin/contact.html', {'contact_fname' : contact_fname})


    else:
        return render(request, 'metacoin/contact.html')



