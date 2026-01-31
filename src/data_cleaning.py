import pandas as pd
import numpy as np
def load_path(file_path,encodingsystem="ISO-8859-1"):
    """
    Load CSV into pandas DataFrame
    :param file_path: Path to CSV file
    Return:
        pd.DataFrame:loaded dataframe
    """
    df=pd.read_csv(file_path,encoding=encodingsystem)
    return df
def drop_missing_customers(df,Columnname):
    """
    Remove rows with missing CustomerID.
    
    :param df: df(pd.DataFrame)
    Returns:
        pd.DataFrame:cleaned dataframe
    """
    df=df.dropna(subset=[Columnname])
    return df
def convert_invoice_date(df,column):
    """
    convert invoicedate column which is in string to datetime object
    
    :param df: pd.DataFrame
    :param column: column name to convert

    Return pd.DataFrame :With datetime column.
    """
    df[column]=pd.to_datetime(df[column])
    return df
def save_clean_data(df,output_path):
    """
    Save cleaned dataframe to csv
    
    :param df: pd.Datframe
    :param output_path: data_clean.csv
    """
    df.to_csv(output_path,index=False)

    