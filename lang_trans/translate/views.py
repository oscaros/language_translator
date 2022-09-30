from django.shortcuts import render
from django.http import HttpResponse
import googletrans
from translate.helpers import load_languages
from translate.models import LanguagesModel

# Create your views here.

def homePage(request): 
    data = None 
    # try:  
    translator = googletrans.Translator()
    data = translator.translate('Example', dest='de').text
    languages = LanguagesModel.objects.all()
    # load_languages()
        # data = translator.detect('habari')
    # except:
    #     pass
    return render(request, "./translate.html", {'languages': languages})
    # return HttpResponse(data)

