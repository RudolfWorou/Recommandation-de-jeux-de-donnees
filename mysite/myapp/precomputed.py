import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from datetime import datetime
import pickle5 as pickle
import os


# normalisation of the data
def norm_data(data,col,columns):
    new_data=data.copy()
    new_data = new_data[col]
    
    new_data.rename(columns=dict(zip(col,columns)),inplace=True)
    new_data.dropna(inplace=True)
    new_data['published_date']=pd.to_datetime(new_data['published_date'], errors='coerce')
    #new_data.dropna(subset=['published_date'],inplace=True)
    return new_data

# preprocessing function
def string_preprocess(s):
    
    s = re.sub(r'[^\w\s]',' ',s)
    s.lower()
    
    return " ".join(set(s.split()) - set(stopwords.words('french')))
    

def main():
        # files importation
    canada_metadata=pd.read_csv('./data/metadata/canada_metadata.csv')
    france_metadata=pd.read_csv('./data/metadata/france_metadata.csv',sep=";")

    # define the columns that we will use
    columns=['id','title','description','url','organization',
                                'published_date','topic']

    # columns equivalent for the datasets
    canada_col = ['ref_number','title_fr','description_fr','portal_url_fr',
                'owner_org_title','date_published','program_alignment_architecture_fr']
    france_col= ['id','title','description','url','organization','last_modified','tags']
    
    # 
    canada_metadata=norm_data(canada_metadata,canada_col,columns)
    france_metadata=norm_data(france_metadata,france_col,columns)

    # metadata fusion
    metadata=pd.concat([canada_metadata,france_metadata])

    # adding the search text 
    metadata['search_string'] = metadata.topic.str.lower() + " " + metadata.title.str.lower() + " " + metadata.topic.str.lower()

    # preprocessing the search text
    metadata['search_string']=metadata['search_string'].map(string_preprocess)

    # reseting the indexes
    metadata.reset_index(drop=True,inplace=True)

    # 
    docs = list(metadata['search_string'])

    # Instantiate a TfidfVectorizer object
    vectorizer = TfidfVectorizer()
    # It fits the data and transform it as a vector
    X = vectorizer.fit_transform(docs)

    # clustering
    model = KMeans(100)
    model.fit(X)

    # adding the clusters to the dataset
    metadata['cluster'] = model.labels_

    # saving the models and dataset 
    with open(os.path.join(os.getcwd(),"myapp","data","X.pkl"), 'wb') as file:  
        pickle.dump(X, file)
    with open(os.path.join(os.getcwd(),"myapp","data","vectorizer.pkl"),'wb') as file : 
        pickle.dump(vectorizer,file)

    with open(os.path.join(os.getcwd(),"myapp","data","cluster_model.pkl"), 'rb') as file:  
        model = pickle.load(file)
    with open(os.path.join(os.getcwd(),"myapp","data","metadata.pkl"),'wb') as file : 
        pickle.dump(metadata,file)

    


if __name__=="__main__":
    main()