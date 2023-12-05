# Shared import function -- find out how to put this in a different file, if possible.
def import_df(file_name, cols,dayfirst=True,is_verbose=False):

    import pandas as pd
    import csv
    import numpy as np
    # Making a list of missing value types
    missing_values = ["n/a", "na", "-"]
    
    #import data
    df = pd.read_csv(file_name
                     ,thousands=','
                     ,dtype=str
                     ,na_values = missing_values
                    ).fillna(0)
    df = df[cols]
 
    #rename columns
    df.rename(columns={'Adj Close**':'Close'}, inplace=True)
    df.rename(columns={'Adj Close':'Close'}, inplace=True)
    
    #convert date to datetime
    df['Date'] = pd.to_datetime(df['Date'],format='mixed',dayfirst=dayfirst)
    
    #convert close to float
    df['Close'].replace(',','',regex=True,inplace=True)
    df['Close'] = pd.to_numeric(df['Close'])

    # Convert volume to int, checking for unexpected values--there is something funky here.  Possibly revisit.
    df['Volume'].replace(',','',regex=True,inplace=True)
    cnt=0
    for row in df['Volume']:
        try:
            df.loc[cnt, 'Volume']=int(row)
        except ValueError:
            df.loc[cnt, 'Volume']=np.nan
        if(df.loc[cnt, 'Volume']==0):
            df.loc[cnt, 'Volume']=np.nan
        cnt+=1
    df['Volume'] = pd.to_numeric(df['Volume'])  

    #debugging stuff 
    #print(df.isna())
    #print(df.isnull().sum())
    
    # Replace nulls using median 
    median = df['Volume'].median()
    df['Volume'].fillna(median, inplace=True)
    df.set_index('Date',inplace=True)

    if(is_verbose):
        print(file_name + ' info:')
        print(df.info())
         #print(df.head())
        print('\n')

    return df