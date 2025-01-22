"""
>>> find_shortest_path(atlanta)
cheapest_prices_table: {'Atlanta': 0, 'Boston': 100, 'Denver': 160, 'Chicago': 200, 'El Paso': 280}
"""
import heapq

class City:
    def __init__(self, name):
        self.name = name
        self.routes = {}
        
    def add_route(self, city, price):
        self.routes[city] = price
        
    def __lt__(self, other):
        return self.name < other.name
    
    def __repr__(self):
        return self.name

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

def find_shortest_path(start_city):
    cheapest_prices_table = {}
    
    priority_queue = []
    
    heapq.heappush(priority_queue, (0, start_city))
    
    while priority_queue:
        cur_price, cur_city = heapq.heappop(priority_queue)
        # use cheapest_prices_table instead of visited set
        if cur_city.name in cheapest_prices_table:
            continue
        cheapest_prices_table[cur_city.name] = cur_price # unusual, in dijkstra we update prices before line 53
        
        for adj_city, price in cur_city.routes.items():
            price_through_current_city = cur_price + price
            
            if adj_city.name not in cheapest_prices_table or price_through_current_city < cheapest_prices_table[adj_city.name]:
                heapq.heappush(priority_queue, (price_through_current_city, adj_city))
    print("cheapest_prices_table:", cheapest_prices_table)

import doctest
doctest.testmod(verbose=True)