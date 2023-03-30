from django.shortcuts import render

import pandas as pd
from random import choice
from django.shortcuts import render
from datetime import date, timedelta

from .models import Brother, Pledge, Pairing
# Create your views here.

def index(request):
    return render(request, 'pairing/index.html')

def read_excel_file(file_path):
    """Reads an Excel file and returns the data as a list of dictionaries."""
    data = []
    df = pd.read_excel(file_path, header=None)
    for row in df.values:
        first_name = row[0]
        last_name = row[1]
        data.append({'first_name': first_name, 'last_name': last_name})
    return data

def generate_pairings(request):

    # Read brothers and pledges data from Excel sheets
    brothers_data = read_excel_file('brothers.xlsx')
    pledges_data = read_excel_file('pledges.xlsx')

    # Create brothers and pledges if they don't exist already
    brothers = []
    for row in brothers_data:
        brother, created = Brother.objects.get_or_create(
            first_name=row['first_name'],
            last_name=row['last_name']
        )
        brothers.append(brother)

    pledges = []
    for row in pledges_data:
        pledge, created = Pledge.objects.get_or_create(
            first_name=row['first_name'],
            last_name=row['last_name']
        )
        pledges.append(pledge)

    # Get the current week's pairings
    week_start = date.today() - timedelta(days=date.today().weekday())
    week_end = week_start + timedelta(days=5)
    # so it resets a day early
    # available_brothers = {}
    # for pledge in pledges:
    #     available_brothers[pledge] = brothers
    
    # Pair pledges with brothers
    # current_pairings = Pairing.objects.filter(week_start=week_start, week_end=week_end)

    # Pair pledges with brothers
    print("There are ",len(brothers),"Brothers")
    i = 1
    for brother in brothers:
        print(i, brother)
        i += 1
    pairings = []
    available_brothers = {}
    for pledge in pledges:
        # Get brothers that are available for this pledge
        paired_brothers = Pairing.objects.filter(pledge=pledge).values_list('brother', flat=True)
        print("# of Paired Bros",(len(paired_brothers)))
        other_paired_brothers = Pairing.objects.filter(week_start=week_start, week_end=week_end).exclude(pledge=pledge).values_list('brother', flat=True)
        print("# of Other Paired Bros",(len(other_paired_brothers)))
        available_brothers[pledge] = Brother.objects.exclude(id__in=paired_brothers).exclude(id__in=other_paired_brothers)
        
        # Pair the pledge with an available brother
        if available_brothers[pledge]:
            brother = choice(available_brothers[pledge])
            pairing = Pairing(
                pledge=pledge,
                brother=brother,
                week_start=week_start,
                week_end=week_end
            )
            pairing.save()
            print(len(available_brothers[pledge]))
            pairings.append(pairing)

    # Pass the pairings to the template
    context = {'pairings': pairings}
    return render(request, 'pairing/pairings.html', context)
    