
try:
    import requests 
    
    api_key="f1603aaec4719390f2c776e8b6d26df2"

    url="https://api.openweathermap.org/data/2.5/weather?q=Hamirpur&appid=YOUR_API_KEY&units=metric"


    city = "Hamirpur"

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")

    data = response.json()

    temperature = data["main"]["temp"]          # number
    description = data["weather"][0]["description"]  # string
    humidity = data["main"]["humidity"]         # number
    city = data["name"]                         # string

    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {description}")
    print(f"Humidity: {humidity}%")


except Exception as e:
    print("sorry an error occurred: ", e)
