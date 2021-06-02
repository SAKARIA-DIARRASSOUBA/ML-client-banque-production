
import pandas as pd


def Proportion_donnees(data):    
	df_Partir = data[data['position'] == 'Partir']
	df_Rester = data[data['position'] == 'Rester'][0:5000]
	return (df_Partir,df_Rester)



def Over_sampling(data):
	df_1,df_2=Proportion_donnees(data)
	df_1_over=df_1.sample(5000, replace=True)
	df=pd.concat([df_2,df_1_over])
	return (df)


def convert_int(word):
    dico={"Rester":0, "Partir":1}
    return(dico[word])

def Augmenter_Data(data):
	df=Over_sampling(data)
	df["position"]=df["position"].apply(lambda x :convert_int(x) )
	return (df)


