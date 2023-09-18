import requests
from bs4 import BeautifulSoup
import csv

# URL of the website
url = "https://weather.com/weather/tenday/l/Youngstown+OH?canonicalCityId=2793e44da479328c35f16aaab4bd1a229f11b2dac0caef70d1e9334fbfd08c3b"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all elements with the specified class and data-testid attribute
    forecast_elements = soup.find_all('p', class_='DailyContent--narrative--3Ti6_', attrs={'data-testid': 'wxPhrase'})

    # Create a CSV file for writing
    with open('weather_forecast.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Day', 'Forecast'])  # Write header row

        # Loop through the first 10 elements and write to the CSV file
        for i, element in enumerate(forecast_elements[:10]):
            day_number = i + 1
            forecast_text = element.get_text(strip=True)
            writer.writerow([f"Day {day_number}", forecast_text])
            print(f"Day {day_number} Forecast: {forecast_text}")

    print("Weather forecast data has been written to 'weather_forecast.csv'")
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
