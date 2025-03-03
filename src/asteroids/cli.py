import argparse 
from datetime import datetime
from .api import get_asteroids


def validate_date(value):
    try:
        # Check if the date format is valid
        datetime.strptime(value, '%Y-%m-%d')
        return value
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid date format: {value}. Expected format is YYYY-MM-DD.")
    

def main():
    parser = argparse.ArgumentParser(description="Get a list of asteroids that have approached Earth around a given date.")
    parser.add_argument("--date", help="Date to search for asteroids (YYYY-MM-DD)", required=True, type=validate_date)
    args = parser.parse_args()
    asteroids = get_asteroids(args.date)
    for asteroid in asteroids:
        print(f"{asteroid['name']} approached Earth on {asteroid['approach_date']}")
        print(f"It came as close as {asteroid['distance_km']} km and has a diameter of {asteroid['diameter_meters']} m.")
        print()
    