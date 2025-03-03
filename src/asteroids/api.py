import requests
import pandas as pd

def scrape_nasa(date: pd.Timestamp) -> dict:
    """Scrape NASA's API for asteroids that have approached Earth.
    Returns:
    dict: JSON response from NASA's API
    """
    date_start = date.strftime("%Y-%m-%d")
    date_end = date + pd.Timedelta(days=7)
    date_end = date_end.strftime("%Y-%m-%d")
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        "start_date": date_start,
        "end_date": date_end,
        "api_key": "DEMO_KEY",
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    # Save this json to a file
    with open("data.json", "w") as file:
        file.write(response.text)	
    return response.json()

def get_asteroids(date: str) -> dict:
    """Get a list of asteroids that have approached Earth around a given date.
    Args:
    date (str): Date to search for asteroids (YYYY-MM-DD)
    Returns:
    dict: List of asteroids with their name, distance from Earth
    in km, diameter in meters, and date of approach
    """
    date = pd.to_datetime(date)
    data = scrape_nasa(date)

    asteroids = data.get("near_earth_objects", {}).get(str(date.date()), [])

    results = []
    for asteroid in asteroids:
        name = asteroid.get("name", "Unknown")
        approach_data = asteroid.get("close_approach_data", [])[0] 
        distance_km = float(approach_data["miss_distance"]["kilometers"])
        diameter_min = asteroid["estimated_diameter"]["meters"]["estimated_diameter_min"]
        diameter_max = asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"]

        results.append({
            "name": name,
            "distance_km": distance_km,
            "diameter_meters": (diameter_min, diameter_max),
            "approach_date": approach_data["close_approach_date"]
        })

    return results
