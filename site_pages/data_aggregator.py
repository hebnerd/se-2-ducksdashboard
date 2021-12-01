import requests

URL_PREFIX = 'https://teamducks.herokuapp.com/api/monitoring'

# Only need to pass aggregate_on_quantity_field=True for Product_Sales

def group_collection(collection, attribute, max_bins, aggregate_on_quantity_field=False):
    categories_map = {}
    if not aggregate_on_quantity_field:
        for row in collection:
            try:
                categories_map[row[attribute]] += 1
            except:
                categories_map[row[attribute]] = 1
    else:
        for row in collection: # Aggregate the quantity each time rather than increment by one.
            try:
                categories_map[row[attribute]] += row['Quantity']
            except:
                categories_map[row[attribute]] = row['Quantity']

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

    if other_values > 0: # Hide the All Other category if it is empty.
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
	
def get_product_sales(timerange, max_bins, aggregate_on_quantity_field=True):
    query = requests.get(f"{URL_PREFIX}/sales/products?timerange={timerange}")
    results = query.json()['results']
    return group_collection(results, 'Description', max_bins)

def get_site_visits_region(timerange, max_bins):
    query = requests.get(f"{URL_PREFIX}/usage/visits?timerange={timerange}")
    results = query.json()['results']
    return group_collection(results, 'Region', max_bins)
	
def get_site_visits_country(timerange, max_bins):
    query = requests.get(f"{URL_PREFIX}/usage/visits?timerange={timerange}")
    results = query.json()['results']
    return group_collection(results, 'Country', max_bins)
	
def get_page_views(timerange, max_bins):
    query = requests.get(f"{URL_PREFIX}/usage/views?timerange={timerange}")
    results = query.json()['results']
    return group_collection(results, 'Page_Name', max_bins)

def get_users_metrics():
    query = requests.get(f"{URL_PREFIX}/users/registered")
    registered_users_count = len(query.json()['results'])

    query = requests.get(f"{URL_PREFIX}/users/online")
    online_users_count = len(query.json()['results'])

    return registered_users_count, online_users_count

def get_site_visits_datetimes(timerange, max_bins):
    query = requests.get(f"{URL_PREFIX}/usage/visits?timerange={timerange}")
    results = query.json()['results']
    return group_collection(results, 'Visited_Timestamp', max_bins)