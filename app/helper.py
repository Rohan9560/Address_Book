from math import radians, sin, cos, sqrt, atan2


def calculate_distance(latitude1, longitude1, latitude2, longitude2):
    Radius = 6371.0  # Radius of the Earth in km
    # Convert latitude and longitude from degrees to radians
    latitude1 = radians(latitude1)
    longitude1 = radians(longitude1)
    latitude2 = radians(latitude2)
    longitude2 = radians(longitude2)

    # Calculate the change in coordinates
    dlon = longitude2 - longitude1
    dlat = latitude2 - latitude1

    # Calculate distance using Haversine formula
    a = sin(dlat / 2) ** 2 + cos(latitude1) * cos(latitude2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = Radius * c
    print("distance.....", distance)
    return distance