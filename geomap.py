from geopy.geocoders import GoogleV3

##################################################
# Some dummy values just so the script is
# self contained and runnable
api_key='AIzaSyBIsCas-a96l683C0DoexcbTEkJohUUOrE'
rows=[{'avg_lat':46.133788848275124, 'avg_lon':-1.1173750335938166}]
##################################################

def get_component(location, component_type):
    for component in location.raw['address_components']:
        if component_type in component['types']:
            return component['long_name']

geolocator = GoogleV3(api_key)
for row in rows:
    location = geolocator.reverse((row['avg_lat'], row['avg_lon']), timeout = 10,  exactly_one=True)
    post_code = get_component(location, 'postal_code')
    country = get_component(location, 'country')

    print location.address