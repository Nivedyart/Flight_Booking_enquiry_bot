# Flight_Booking_enquiry_bot

The Flight Booking enquiry Bot is a conversational AI application designed to assist users in booking flights quickly and efficiently.

## Overview

The Flight Booking Bot utilizes natural language processing (NLP) to understand user queries and provide relevant flight options. It assist users with flight booking inquiries. It provides users with information about flight availability, schedules, prices, and booking procedures through a chat interface.

## Features

- **Flight Search**: Users can search for flights by providing details such as departure city, destination, and date.
- **Flight Availability**: The bot fetches real-time information on flight availability.
- **Flight Pricing**: Users can inquire about the prices of available flights based on their search .criteria.

### How to use

- Install the required dependencies
- Run "flask run"

### Sample data

| Flight_ID | Airline   | Departure_City | Arrival_City | Departure_Date | Departure_Time | Arrival_Date | Arrival_Time | Price |
|-----------|-----------|----------------|--------------|----------------|----------------|--------------|--------------|-------|
| FL001     | Delta     | New York       | Los Angeles  | 15-04-2024     | 8:00 AM        | 15-04-2024   | 11:00 AM     | $300  |
| FL002     | United    | Los Angeles    | New York     | 20-04-2024     | 10:00 AM       | 20-04-2024   | 4:00 PM      | $350  |
| FL003     | American  | Chicago        | Miami        | 01-05-2024     | 12:00 PM       | 01-05-2024   | 3:00 PM      | $280  |
| FL004     | Southwest | Miami          | Chicago      | 05-05-2024     | 2:00 PM        | 05-05-2024   | 5:00 PM      | $260  |


### Sample input

```{"message":"Is there any ticket available from New York to Los Angeles on 15-04-2024"}```

### Sample output

```{
    "data": [
        {
            "Airline": "Delta",
            "Arrival_Date": "2024-04-15",
            "Arrival_Time": "11:00",
            "Departure_Time": "08:00",
            "Flight_ID": "FL001",
            "Price": "$300"
        }
    ],
    "error": "No error",
    "status": "Success"
}```