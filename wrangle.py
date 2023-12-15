#standard DS imports
import pandas as pd
import numpy as np

#visualization imports
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

import env
import os


def wrangle_zillow():
    """
    This function acquires and prepares the Zillow dataset for analysis.

    If the 'zillow.csv' file exists, the function reads the data from the CSV file.
    If the file does not exist, it reads the data from the 'zillow' database using SQL queries
    and saves the resulting DataFrame to 'zillow.csv'.

    The function then drops any rows with missing values and performs necessary data type conversions
    on the 'yearbuilt', 'bedroomcnt', 'fips', 'taxvaluedollarcnt', and 'calculatedfinishedsquarefeet' columns.

    Returns:
    - pd.DataFrame: The prepared and cleaned Zillow dataset.

    Example:
    df_zillow = wrangle_zillow()
    """
    # acquire the data
    filename = 'zillow.csv'
    if os.path.exists(filename):
        print('this file exists, reading from csv')
        #read from csv
        df = pd.read_csv(filename, index_col=0)
    else:
        print('this file doesnt exist, reading from sql and saving to csv')
        #read from sql
        url = env.get_db_url('zillow')
        df = pd.read_sql('''select bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
        from propertylandusetype
        join properties_2017
            using (propertylandusetypeid)
        WHERE propertylandusedesc = ("Single Family Residential");''', url)
        #save to csv
        df.to_csv(filename)

    df = df.dropna()

    df.yearbuilt = df.yearbuilt.astype(int)
    df.bedroomcnt = df.bedroomcnt.astype(int)
    df.fips = df.fips.astype(int)
    df.taxvaluedollarcnt = df.taxvaluedollarcnt.astype(int)
    df.calculatedfinishedsquarefeet = df.calculatedfinishedsquarefeet.astype(int)

    return df

def splitting_data(df):
    '''
    Prepare the Telco dataset by cleaning and transforming the data.

    Parameters:
    - df (DataFrame): The input DataFrame containing Telco data.

    Returns:
    - DataFrame: The cleaned and transformed Telco DataFrame.

    Steps:
    1. Drop unnecessary columns: 'payment_type_id', 'internet_service_type_id', 'contract_type_id'.
    2. Replace any empty spaces in 'total_charges' with '0.0'.
    
    Example:
        telco_data = pd.read_csv('telco.csv')
        cleaned_telco = prep_telco(telco_data)
    '''

    #first split
    train, validate_test = train_test_split(df,
                     train_size=0.6,
                     random_state=123,
                    )
    
    #second split
    validate, test = train_test_split(validate_test,
                                     train_size=0.5,
                                      random_state=123,
                                     )
    return train, validate, test