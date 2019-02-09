import googlemaps

def distance_matrix(origins, destinations, region='RU'):
    gmaps = googlemaps.Client(key='AIzaSyBNtYP55CU8LGJ7Q1oXFToBOxHyPlV7vQw')
    return gmaps.distance_matrix(origins=[x+','+region for x in origins], destinations=[x+','+region for x in destinations], language='RU')

distance_matrix_result = distance_matrix([x+',RU' in 'турку 5, петербург'], ['московский вокзал'])
distance_matrix_result
for i in distance_matrix_result['rows']:
    for j in i['elements']:
        print(j['distance']['value'], end='\t')
    print('')    
