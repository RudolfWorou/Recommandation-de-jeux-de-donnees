from django.shortcuts import render
from django.http import HttpResponse
from .forms import RequestForm
from .search_function import search
import pickle5 as pickle
import os
from datetime import datetime
from django.contrib import messages

# Create your views here.
def home(request):
    form = RequestForm()

    if request.method=="POST":
        print(request.POST)
        form = RequestForm(request.POST)
    
    
    context={'form': form}
        
        

    
    return render(request,'myapp/home.html',context)


def result(request):
    #print(request.GET)
    try: 
        if (request.POST['start_date']==""):
            start_date = datetime(1800,1,1,0,0,0) 
        else:
            start_date = datetime.fromisoformat(request.POST['start_date'])
        if (request.POST['end_date']==""):
            end_date=datetime.now()
        else:
            end_date = datetime.fromisoformat(request.POST['end_date'])
    except:
        #messages.error(request, "Error")
        return HttpResponse('Veuillez entrer une date au format adapté')

    query = request.POST['query']
    
    #execute the search
    
    with open(os.path.join(os.getcwd(),"myapp","data","cluster_model.pkl"), 'rb') as file:  
        model = pickle.load(file)

    with open(os.path.join(os.getcwd(),"myapp","data","X.pkl"), 'rb') as file:  
        X = pickle.load(file)
        
    with open(os.path.join(os.getcwd(),"myapp","data","metadata.pkl"),'rb') as file:
        metadata=pickle.load(file)
        
    with open(os.path.join(os.getcwd(),"myapp","data","vectorizer.pkl"),'rb') as file:
        vectorizer = pickle.load(file)
    result_list= search(query,metadata,X,vectorizer,model,start_date,end_date)
    #result_dict= dict(zip(range(len(result_list)),result_list)) 
    context={'result_list': result_list}
    print(request.POST)
    return render(request,'myapp/result.html',context)
    #return HttpResponse('zkjdnzudz ziudz')