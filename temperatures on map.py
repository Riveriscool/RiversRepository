import folium
import requests
import pandas as pd

API_key = "714c2da2279a72ec8bb713798409d352"

def coolfn(zip_code):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={API_key}")
    data = response.json()

    if 'main' in data and 'temp' in data['main']:
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        return temperature_celsius
    else:
        return None
def zip_to_coordinates(zip_code, csv_file="uszips.csv"):
    # Read the CSV file into a DataFrame, considering double-quoted values
    df = pd.read_csv(csv_file, sep=',', quotechar='"', dtype={"zip": str})

    # Check if the provided zip code is in the DataFrame
    if str(zip_code) in df["zip"].values:
        # Retrieve the latitude and longitude for the given zip code
        coordinates = df.loc[df["zip"] == str(zip_code), ["lat", "lng"]].values[0]
        return tuple(coordinates)
    else:
        print(f"Zip code {zip_code} not found in the CSV file.")
        return None


def plot_temperatures(zip_codes):
    # Create a map centered around the first zip code
    first_zip_code = zip_codes[0]
    first_coordinates = zip_to_coordinates(first_zip_code)
    if first_coordinates is None:
        print(f"Could not retrieve coordinates for {first_zip_code}")
        return

    world_map = folium.Map(location=first_coordinates, zoom_start=12)

    # Plot temperatures for each zip code
    for zip_code in zip_codes:
        coordinates = zip_to_coordinates(zip_code)
        if coordinates is not None:
            temperature = coolfn(zip_code)

            if temperature is not None:
                popup_text = f"Zip Code: {zip_code}<br>Temperature: {temperature:.2f} °C"
                folium.Marker(location=coordinates, popup=popup_text).add_to(world_map)
            else:
                print(f"Could not retrieve temperature for {zip_code}")
        else:
            print(f"Could not retrieve coordinates for {zip_code}")

    # Save the map to an HTML file
    world_map.save("temperature_map.html")

# Example usage:
if __name__ == "__main__":
    zip_codes = ["10001", "90210", "75001", "60601", "94105"]
    plot_temperatures(zip_codes)
