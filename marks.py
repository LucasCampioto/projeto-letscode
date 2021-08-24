import warnings
warnings.filterwarnings("ignore")
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import locale
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import marks

def marks_prediction(area, dist):
    df = pd.read_csv('C:/Users/Lucas/Documents/Data science - lets code/Projeto/Datasets/imoveis_rio.csv', sep=';')
    pd.set_option('display.max_colwidth', None)

    df_copy = df.copy()

    df_copy['log_Valor'] = np.log(df_copy['Valor'])
    df_copy['log_Area'] = np.log(df_copy['Area'])
    df_copy['log_Dist_Praia'] = np.log(df_copy['Dist_Praia'] + 1)
    df_copy['log_Dist_Farmacia'] = np.log(df_copy['Dist_Farmacia'] + 1)

    y = df_copy['Valor']

    X = df_copy[['Area','Dist_Praia']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    model = LinearRegression()

    model.fit(X_train, y_train)

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  

    area_imovel = area
    Dist_Praia = dist
    entrada = [[area_imovel, Dist_Praia]]
    resultado = model.predict(entrada)[0] #Revertendo a conversão para obter valores em reais
    valor = locale.currency(resultado, grouping=True, symbol=None)
    return valor
    

    
