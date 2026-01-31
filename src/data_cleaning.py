import pandas as pd
import numpy as np
def load_path(file_path,encodingsystem="ISO-8859-1"):
    """
    Load CSV into pandas DataFrame
    :param file_path: Path to CSV file
    
    """
    pd.read_csv(file_path,encoding=encodingsystem)
def drop_missing_customers(df,Columnname):
    """
    Remove rows with missing CustomerID.
    
    :param df: df(pd.DataFrame)
   
    """
    df.dropna(subset=[Columnname])
    
def convert_invoice_date(df,column):
    """
    convert invoicedate column which is in string to datetime object
    
    :param df: pd.DataFrame
    :param column: column name to convert

    
    """
    df[column]=pd.to_datetime(df[column])
   
def save_clean_data(df,output_path):
    """
    Save cleaned dataframe to csv
    
    :param df: pd.Datframe
    :param output_path: data_clean.csv
    """
    df.to_csv(output_path,index=False)

    