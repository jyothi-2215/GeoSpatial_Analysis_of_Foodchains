import pandas as pd
import requests
import json

#Read restaurants csv
df=pd.read_csv("restaurants.csv")
#print(df.head())

#API call and get latitute & longitude values
for i,row in df.iterrows():
    apiAddress= str(df.at[i,'street'])+','+str(df.at[i,'zip'])+','+str(df.at[i,'city'])+','+str(df.at[i,'country'])
    # print(apiAddress)
    parameters={
        "key":"xToLRpzK0arecAa27HliHMC1Yv0o2BPn",
        "location":apiAddress
    }
    response= requests.get("http://www.mapquestapi.com/geocoding/v1/address",params=parameters)
    lat=json.loads(response.text)['results' ][0]['locations'][0]['latLng']['lat']
    lng=json.loads(response.text)['results' ][0]['locations'][0]['latLng']['lng']
    df.at[i,'lat']=lat
    df.at[i,'lng']=lng
    # print(lat,lng)
df.to_csv('restaurantsGeo.csv')

#Save data to CSV with geodata