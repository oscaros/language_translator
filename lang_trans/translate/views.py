from django.shortcuts import render
from django.http import HttpResponse
import googletrans
from translate.models import languagesModel

# Create your views here.

def homePage(request): 
    data = None 
    # try:  
    translator = googletrans.Translator()
    data =translator.translate('Example', dest='de').text
    languages =languagesModel.objects.all()
        # data = translator.detect('habari')
    # except:
    #     pass
    return render(request, "./translate.html", {'languages': languages})
    # return HttpResponse(data)

