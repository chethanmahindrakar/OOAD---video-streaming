import pandas as pd
import numpy as np
import math
from sklearn.metrics.pairwise import cosine_similarity
from random import *


class reccengine:
    def __init__(self,tag_list = '',path = "database/recc_data.csv",):
        self.path = path
        print(tag_list)
        self.tag_list = list(set(tag_list.split(sep=',')))
    
    def reccomendations(self):
        df=pd.read_csv(self.path)
        df.head()

        df=df[['ID','title','tags','url','imgurl']]
        tags=[]
        for i in df['tags']:
            i = str(i)
            m =list(i.split(sep=','))
            for j in m:
                tags.append(j)
        tags=sorted(list(set(tags)))
      
        page_profile_matrix=[]
        for i in range(len(df['tags'])):
            page_profile_matrix.append(list())
            
        for i in range(len(df['ID'])):
            for j in range(len(tags)):
                if tags[len(tags) -j -1] in df['tags'][i]:
                    page_profile_matrix[i].append(1)
                else:
                    page_profile_matrix[i].append(0)           

        cosine_sim=cosine_similarity(page_profile_matrix)

        popular_tags = []
        for i in range(0,6):
            popular_tags.append(randint(0,len(df['tags'])-1))
        popular_tags = list(set(popular_tags))

        recommended_pages_indexes = []
        for i in range(len(popular_tags)):
            scores_series=pd.Series(cosine_sim[popular_tags[i]]).sort_values(ascending=False)
            recommended_pages_indexes.append(scores_series[0:1].index[0])

        recommended_pages=[]
        for j in recommended_pages_indexes:
                recommended_pages.append([df['imgurl'][j],df['title'][j]])
        #recommended_pages = list(set(recommended_pages))
        return recommended_pages
    def personalized_reccs(self):
        df=pd.read_csv(self.path)
        df.head()

        df=df[['ID','title','tags','url','imgurl']]
        tags=[]
        for i in df['tags']:
            i = str(i)
            m =list(i.split(sep=','))
            for j in m:
                tags.append(j)
        tags=sorted(list(set(tags)))
        


        page_profile_matrix=[]
        for i in range(len(df['tags'])):
            page_profile_matrix.append(list())
            
        for i in range(len(df['ID'])):
            for j in range(len(tags)):
                if tags[len(tags) -j -1] in df['tags'][i]:
                    page_profile_matrix[i].append(1)
                else:
                    page_profile_matrix[i].append(0)           

        cosine_sim=cosine_similarity(page_profile_matrix)

        recommended_pages_indexes = []
        scores_series=pd.Series(cosine_sim[int((tags.index(self.tag_list[0]))/2)]).sort_values(ascending=False)
        recommended_pages_indexes.append(scores_series[0:1].index[0])
        scores_series=pd.Series(cosine_sim[int((tags.index(self.tag_list[1]))/2)]).sort_values(ascending=False)
        recommended_pages_indexes.append(scores_series[0:1].index[0])

        recommended_pages=[]
        for j in recommended_pages_indexes:
                recommended_pages.append([df['imgurl'][j],df['title'][j]])
        #recommended_pages = list(set(recommended_pages))
        return recommended_pages


