import nltk
import pandas as pd 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from datetime import datetime
import json
from app.models import APIResponse

#Load flight ticket booking dataset
flight_data = pd.read_excel('/home/nivedya/pythonprojects/jiji2/flight_data.xlsx')


def process_user_input(user_input):
    #tokenize user input
    tokens = word_tokenize(user_input)

    #extract departure_city, arrival_city and date
    departure_city = ""
    arrival_city = ""
    date = ""

    for i in range(len(tokens)):
        if tokens[i].lower() == 'from' and i < len(tokens) - 1:
            # departure_city = tokens[i + 1]
            fromIndex = i
        elif tokens[i].lower() == 'to' and i < len(tokens) - 1:
            # arrival_city = tokens[i + 1]
            toIndex = i
        elif tokens[i] == 'on' and i < len(tokens) - 1:
            date = tokens[i + 1]
            print(date)
            onIndex = i 
       
    for i in range(fromIndex,toIndex-1):
        departure_city = departure_city+tokens[i+1]+" "
    departure_city = departure_city.strip()
    print(departure_city)
    
    for i in range(toIndex,onIndex-1):
        arrival_city = arrival_city+tokens[i+1]+" "
    arrival_city = arrival_city.strip()
    print(arrival_city)
    
    
    #search for flights based on user input
    if departure_city and arrival_city and date:
        input_date_obj = datetime.strptime(date, "%d-%m-%Y")
        convertedDate = input_date_obj.strftime("%Y-%m-%d")

        filtered_flights = flight_data[
        (flight_data['Departure_City'] == departure_city) &
        (flight_data['Arrival_City'] == arrival_city) & 
        (flight_data['Departure_Date'] == convertedDate)]

        #generate response based on search results
        if not filtered_flights.empty:
            response = []
            for index, row in filtered_flights.iterrows():
                flight_reponse={
                    "Flight_ID":row['Flight_ID'],
                    "Airline": row['Airline'],   
                    "Departure_Time": row['Departure_Time'].strftime('%H:%M'),
                    "Arrival_Date": row['Arrival_Date'].strftime('%Y-%m-%d'),
                    "Arrival_Time": row['Arrival_Time'].strftime('%H:%M'),
                    "Price": row['Price']
                }
                response.append(flight_reponse)

            api_response  = APIResponse("Success", response , "No error")


        else:
            api_response = APIResponse("Success", None ,"Sorry. No flights are available for the given criteria")
    else:
        api_response = APIResponse("Success", None , "Please provide departure city, arrival city as well as the date")

    return api_response
    




        