from django.shortcuts import render, HttpResponse
from .models import AbbreviationList,Abbreviation
import string
import re

# Create your views here.

def index(requst):
    abbr_list = AbbreviationList.objects.filter(user='sanders')[0]
    abbrs = Abbreviation.objects.filter( abbreviation_list=abbr_list)
    context = {"abbr_list":abbr_list, "abbrs":abbrs}

    return render(requst,'note/index.html',context)



def convert(request):

    #convert note
    # converted_note = convert_abbreviations_to_full_form(request.POST["rawnote"])
    if request.POST:
        converted_note = convert_abbreviations_to_full_form(request.POST["rawnote"])
    else:

        converted_note = ""

    return render(request,'note/index.html',
                  {"rawnote":"" if not request.POST else request.POST["rawnote"],
                   "converted_note":converted_note}
                  )


def convert_abbreviations_to_full_form(rawnote):
    abbr_list = AbbreviationList.objects.filter(user='sanders')[0]
    abbrs = Abbreviation.objects.filter( abbreviation_list=abbr_list)
    abbrs_dict = {}
    punctuation = set(string.punctuation)
    for abbr in abbrs:
        abbrs_dict[abbr.abbreviation] = abbr.full_form

    word_list = re.findall(r"[\w/']+|[.:,!?;]", rawnote)

    for idx,word in enumerate(word_list):
        if word.lower() in abbrs_dict:
            word_list[idx] = abbrs_dict[word.lower()]


    # return " ".join(word_list)
    return " ".join(word_list)
