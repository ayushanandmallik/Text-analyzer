from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def analyze(request):

    djtext = request.POST.get('text', 'default')
    punctuation = ''',:'_.!-?().";/-'''
    rempunction = request.POST.get('rempunc', 'off')
    fin_text = ""
    if rempunction=="on":
        for char in djtext:
            if char not in punctuation:
                fin_text = fin_text + char
    if rempunction=="off":
        for char in djtext:
            fin_text = fin_text + char
    cap = request.POST.get('capitalize', 'off')
    if cap=='on':
        fin_text = fin_text.capitalize()
    if cap=='off':
        fin_text = fin_text
    upp = request.POST.get('uppercase', 'off')
    if upp=='on':
        fin_text = fin_text.upper()
    if upp=='off':
        pass
    spc = request.POST.get('extraspace', 'off')
    if spc=='on':
        final = ""
        for index,char in enumerate(fin_text):
            if not (fin_text[index]== ' ' and fin_text[index+1]==' '):
                final = final + char
    if spc=='off':
        final = fin_text

    par= {'purpose':'analyzed', 'finaltext': final, 'chcnt':'not_selected'}
    chc = request.POST.get('charcount', 'off')
    count=0

    if chc=='on':
        for i in range(len(final)):
            count = count+1
            i = i+1
            par['chcnt']= count
    if chc=='off':
        pass

    return render(request, 'analyze.html', par)