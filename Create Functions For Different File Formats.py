import pandas as pd

#creating multiple functions for different data types

#users will select their data type and the right function would be executed
#all have been tested and function the same

#create a function which will import a csv file into a dataframe
def csv_loading(file):
    df = pd.read_csv(file)
    return(df)

#create a function which will import a tsv file into a dataframe
def tsv_loading(file):
    df = pd.read_csv(file, sep = '\t')
    return(df)

#create a function which will import an excel worksheet file into a dataframe
def excel_loading(file):
    df = pd.read_excel(file)
    return(df)


#the html for the js program has them  loading only three data sets, aorta_data,
#coro_data, and aorta_coro
#they commented out the het_coro_aorta data in both the html and the js so I left it out here. 

#I am giving the dataframes same name as the files for now but we will
#want to generalize these later

#I used Jupyter Notebook and therefore my working diretory contained the files
#if your files aren't in your working directory you will need to add the file path

coro = tsv_loading('coro_data.tsv')
aorta = tsv_loading('aorta_data.tsv')
aorta_coro = tsv_loading('aorta_coro.tsv')


#for initial testing purposes the head of each dataframe is shown below.
#This will be removed later and is only for confirmation
print(coro.head())
print(aorta.head())
print(aorta_coro.head())

