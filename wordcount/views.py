"""
from django.http import HttpResponse
from django.shortcuts import render
"""
import blockchain as bl
import json
import datetime as date
import time

# We create the genesis block
"""
# Idea: could it be possible to make a blockchain where no token is created because relies on time >? Ie one block every x sec ? 
"""
# how to print the blockchain in JSON format
bl.block['blockchain'].append(bl.New_Block().json_format())
chaine = print('chaine',json.dumps(bl.block, indent=2))



def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    return render(request, 'count.html', {'fulltext': fulltext})
