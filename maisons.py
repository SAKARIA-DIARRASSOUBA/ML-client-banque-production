import pandas as pd

def Build_predict(liste_6_elts):
    col_name=["CreditScore","Geography","Gender","Age","Tenure","Balance","EstimatedSalary"]
    res=pd.DataFrame(liste_6_elts).T
    res.columns=col_name
    return(res)