"""
>>> find_shortest_path(atlanta, el_paso)
cheapest_prices_table: {'Atlanta': 0, 'Boston': 100, 'Denver': 160, 'Chicago': 200, 'El Paso': 280}
cheapest_previous_stopover_city_table: {'Boston': 'Atlanta', 'Denver': 'Atlanta', 'Chicago': 'Denver', 'El Paso': 'Chicago'}
shortest_path: ['Atlanta', 'Denver', 'Chicago', 'El Paso']
"""

class City:
    def __init__(self, name):
        self.name = name
        self.routes = {}
        
    def add_route(self, city, price):
        self.routes[city] = price

atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
el_paso = City("El Paso")

atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)
boston.add_route(chicago, 120)
boston.add_route(denver, 180)
chicago.add_route(el_paso, 80)
denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)

def find_shortest_path(start_city, final_dest):
    cheapest_prices_table = {}
    cheapest_previous_stopover_city_table = {}
    
    unvisited_cities = [] # sort of queue
    visited_cities = set()
    
    cheapest_prices_table[start_city.name] = 0
    cur_city = start_city
    
    while cur_city:
        visited_cities.add(cur_city.name)
        if cur_city in unvisited_cities:
            unvisited_cities.remove(cur_city)
        
        for adj_city, price in cur_city.routes.items():
            if adj_city.name not in visited_cities:
                unvisited_cities.append(adj_city)
            
            price_through_current_city = cheapest_prices_table[cur_city.name] + price
            
            if adj_city.name not in cheapest_prices_table or price_through_current_city < cheapest_prices_table[adj_city.name]:
                cheapest_prices_table[adj_city.name] = price_through_current_city
                cheapest_previous_stopover_city_table[adj_city.name] = cur_city.name
            
        cur_city = None
        min_price = float('inf')
        
        for city in unvisited_cities:
            city_price = cheapest_prices_table.get(city.name, float('inf'))
            if city_price < min_price:
                min_price = city_price
                cur_city = city
    
    shortest_path = []
    cur_city = final_dest
    
    while cur_city.name != start_city.name:
        shortest_path.append(cur_city.name)
        cur_city.name = cheapest_previous_stopover_city_table[cur_city.name]
    
    shortest_path.append(start_city.name)
    shortest_path.reverse()
    
    print("cheapest_prices_table:", cheapest_prices_table)
    print("cheapest_previous_stopover_city_table:", cheapest_previous_stopover_city_table)
    print("shortest_path:", shortest_path)

import doctest
doctest.testmod(verbose=True)