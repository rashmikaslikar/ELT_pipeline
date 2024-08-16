import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer
import json
import requests

value_id1='0100011D00FF'
value_id2='0100021D00FF'

def get_data(url):
    response=requests.get(url)
    data=response.text
    data=json.loads(data)
    return data

def prepare_df(data, value_id):
    df = pd.DataFrame(data['data'])
    
    # Convert the timestamp to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Create separate 'date' and 'time' columns
    df['date'] = df['timestamp'].dt.date
    df['time'] = df['timestamp'].dt.time
    
    #rename column value_id to energy_consumed
    df=df.rename({value_id: "units_consumed"}, axis = 1)
    
    #df.set_index('timestamp', inplace=True)
    df['units_consumed x 1000'] = df["units_consumed"].apply(lambda x: x*1000)
    
    
    df = df[['timestamp','date', 'time', 'measurement', 'units_consumed', 'units_consumed x 1000', 'tags']]
    
    df = pd.concat([df.drop(['tags'], axis=1), df['tags'].apply(pd.Series)], axis=1)
    
    df = df[::-1]
    
    return df

data_1 = get_data("https://exnaton-public-s3-bucket20230329123331528000000001.s3.eu-central-1.amazonaws.com/challenge/95ce3367-cbce-4a4d-bbe3-da082831d7bd.json")
df_1 = prepare_df(data_1,value_id1)

renderer = StreamlitRenderer(df_1, spec='pygwalker_spec_data_1.json')
renderer.explorer()