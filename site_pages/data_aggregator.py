import requests

URL_PREFIX = 'https://teamducks.herokuapp.com/api/monitoring'

def group_collection(collection, attribute, max_bins):
    categories_map = {}
    for row in collection:
        try:
            categories_map[row[attribute]] += 1
        except:
            categories_map[row[attribute]] = 1

    categories = list(categories_map.keys())
    values = list(categories_map.values())
    max_index = 0
    temp_str = ''
    temp_int = 0
    for i in range(0, ( len(categories) - 1 )):
        for j in range (i+1, len(categories)):
            if values[j] > values[max_index]:
                max_index = j
        temp_str = categories[max_index]
        categories[max_index] = categories[i]
        categories[i] = temp_str

    return categories[:(max_bins - 1)], values[:max_bins]
    
def get_pet_sales_categories(timerange, max_bins):
    query = requests.get(f"{URL_PREFIX}/sales/pets?timerange={timerange}")
    results = query.json()['results']
    return group_collection(results, 'Category', max_bins)

def get_pet_sales_breeds(timerange, max_bins):
    query = requests.get(f"{URL_PREFIX}/sales/pets?timerange={timerange}")
    results = query.json()['results']
    return group_collection(results, 'Breed', max_bins)