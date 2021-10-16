import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from datetime import datetime
import pickle5 as pickle

from .precomputed import string_preprocess


# The function which returns the result for a query
def search(query,metadata,X,vectorizer,model, start_date=datetime(1800,1,1,0,0,0), end_date=datetime.now(),limit=200):
     # preprocessing the query
    query = string_preprocess(query)
    query_vec=vectorizer.transform([query])
    
    # filtering with date
    L=list(metadata[ (metadata['cluster']==int(model.predict(query_vec)) ) & ((start_date<=metadata.published_date) & (metadata.published_date <= end_date)) ].index)
    G=[0 for g in range(len(L))]
    #print( cosine_similarity(q_csr,q_csr )[0][0] )
    for indx, i in enumerate(L):
        # Computing the similarity with each document
        m= cosine_similarity(query_vec,X[i,:].reshape(1,-1)) [0][0]
        #m=np.dot(query_vec.T,X[:,i].reshape(1,-1))
        #print(m)
        G[indx]=np.array([i,m])
    # Sorting the results   
    M=np.array(sorted(G, key=lambda x: x[1],reverse=True))
    
    return list(metadata.iloc[M[:,0][:limit],3])
    

def main():
    pass
    

if __name__=='__main__':
    main()