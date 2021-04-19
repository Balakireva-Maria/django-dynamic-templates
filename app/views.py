from django.shortcuts import render
import csv
from django.http import HttpResponse

def inflation_view(request):
    template_name = 'inflation.html'
    with open('inflation_russia.csv', 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            print(', '.join(row))

    context = {'list': reader

               }
    return render(request, template_name,
                  context)