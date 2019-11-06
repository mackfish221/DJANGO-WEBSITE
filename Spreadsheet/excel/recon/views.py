from django.shortcuts import render
import os, io
import re
import pandas as pd
from django.http import HttpResponseBadRequest, HttpResponse
import xlsxwriter
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage




# Create your views here.

def reconciliations(request):
    
    return render(request, 'recon/reconciliations.html')


# def read_excel(data_input):
#     

#     extension = os.path.splitext(data_input)[1].lower()[1:]

#     assert extension in read_map
#     assert os.path.isfile(data_input)
def messages(request):
    return render(request, 'recon/messages.html')

def upload(request):
    if request.method == "POST" and request.FILES['data_file']:
        if 'data_file' not in request.FILES:
            return render(request, 'recon/form.html')

        data = request.FILES['data_file']
        if not data.name.endswith('.xlsx'):
            return render(request, 'recon/messages.html')
            #return render(request, 'recon/form.html')

        #UPLOAD_DIR= 'C:/Users/McQueen Aghaulor/Desktop'
        #os.path.join(UPLOAD_DIR, data)

    
        else:
            df = pd.read_excel(data)

            df['ref'] = df['Description']
            df['Description'] = df.Description.str.extract(r'\d(\d+)', expand=True)

            #df.sort_values(['ref', 'Description'], ascending=[True, 'ref'], inplace=True)

            df.drop_duplicates(subset='Description', keep=False, inplace=True)
            #result = df.to_excel('C:/Users/McQueen Aghaulor/Desktop/recon.xlsx')
            result= FileSystemStorage(df.to_excel('C:/Users/McQueen Aghaulor/Desktop/Recon.xlsx'))
            #result.save(data.name, data)
            return render(request, 'recon/form.html')
    
            #return render(request, df.to_excel('C:/Users/McQueen Aghaulor/Desktop/recon.xlsx'))
    else:
        return render(request, 'recon/form.html')


