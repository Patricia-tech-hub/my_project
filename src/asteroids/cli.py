import argparse 
from .api import get_asteroids

def main():
    parser = argparse.ArgumentParser(description="Get a list of asteroids that have approached Earth around a given date.")
    parser.add_argument("--date", help="Date to search for asteroids (YYYY-MM-DD)", required=True)
    args = parser.parse_args()
    asteroids = get_asteroids(args.date)
    for asteroid in asteroids:
        print(f"{asteroid['name']} approached Earth on {asteroid['approach_date']}")
        print(f"It came as close as {asteroid['distance_km']} km and has a diameter of {asteroid['diameter_meters']} m.")
        print()
    