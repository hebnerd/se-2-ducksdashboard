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
    temp_str = ''
    temp_int = 0
    list_len = len(categories)
    for i in range(0, list_len-1):
        for j in range(i+1, list_len):
            if values[j] > values[i]:
                temp_str = categories[j]
                temp_int = values[j]
                categories[j] = categories[i]
                values[j] = values[i]
                categories[i] = temp_str
                values[i] = temp_int
    
    other_values = sum(values[max_bins:]) # Aggregate everything > max_bins into an 'Other' grouping.
    categories = categories[:max_bins]
    values = values[:max_bins]

    categories.append('All Other')
    values.append(other_values)

    return categories, values

def get_pet_sales_categories(timerange, max_bins):
    query = requests.get(f"{URL_PREFIX}/sales/pets?timerange={timerange}")
    results = query.json()['results']
    return group_collection(results, 'Category', max_bins)

def get_pet_sales_breeds(timerange, max_bins):
    query = requests.get(f"{URL_PREFIX}/sales/pets?timerange={timerange}")
    results = query.json()['results']
    return group_collection(results, 'Breed', max_bins)