def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    d = {}
    for i in range(len(cities)):
        d[i] = cities[i]
    return d
cities = ["Bukhara", "Khiva", "Namangan", "Samarkand", "Tashkent"]
print(cities_dict(cities))