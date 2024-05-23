import os

class Graph:
    def __init__(self):
        self.graph = {}
        self.vertices_no = 0

    def add_city(self, city):
        if city in self.graph:
            print(f'City {city} has already been added.')
        else:
            self.graph[city] = []
            self.vertices_no += 1
            print(f'City {city} successfully added.\n')

    def add_city_distance(self, city1, city2, distance):
        if city1 not in self.graph:
            print(f"City {city1} not available.")
        elif city2 not in self.graph:
            print(f"City {city2} not available.")
        else:
            for i in range(len(self.graph[city1])):
                if city2 in self.graph[city1][i]:
                    print(f'Distance between city {city1} and city {city2} has already been added.')
                    break
            else:
                self.graph[city1].append([city2, distance])
                self.graph[city2].append([city1, distance])
                print(f'Successfully added distance between {city1} and {city2} ----> {distance}\n')

    def get_graph(self):
        print(self.graph)

    def route_distance(self, city1, city2):
        if city1 not in self.graph:
            print(f"City {city1} not available.")
        elif city2 not in self.graph:
            print(f"City {city2} not available.")
        else:
            direct_distance = 0
            for i in range(len(self.graph[city1])):
                if city2 == self.graph[city1][i][0]:
                    direct_distance += self.graph[city1][i][1]

            route = [city1]
            indirect_distance = 0
            for i in range(len(self.graph[city1])):
                if city2 != self.graph[city1][i][0]:
                    neighboring_cities1 = [self.graph[city1][i] for i in range(len(self.graph[city1]))]
                    neighboring_cities2 = [self.graph[city2][j] for j in range(len(self.graph[city2]))]
                    for city1_neighbor in neighboring_cities1:
                        for city2_neighbor in neighboring_cities2:
                            if city1_neighbor[0] == city2_neighbor[0]:
                                total_distance = city1_neighbor[1] + city2_neighbor[1]
                                if indirect_distance == 0:
                                    indirect_distance = total_distance
                                    route.append(city1_neighbor[0])
                                elif indirect_distance > total_distance:
                                    indirect_distance = total_distance
                                    route[-1] = city1_neighbor[0]

            route.append(city2)
            if direct_distance != 0:
                if indirect_distance == 0 or direct_distance < indirect_distance:
                    print(f'The distance between city {city1} and {city2} is {direct_distance}')
                elif direct_distance > indirect_distance:
                    print(f'The route from {city1} to {city2} is {route} with a distance of {indirect_distance}')
            elif indirect_distance != 0:
                if direct_distance == 0 or indirect_distance < direct_distance:
                    print(f'The route from {city1} to {city2} is {route} with a distance of {indirect_distance}')
                elif indirect_distance > direct_distance:
                    print(f'The distance between city {city1} and {city2} is {direct_distance}')

g = Graph()

def main_menu():
    print('''City Data Application\n
    1. Add city
    2. Add distance between two cities
    3. Check route
    4. Print city graph
    5. Exit''')
    menu_choice = int(input('Choose a menu option: '))
    if menu_choice == 1:
        add_city()
    elif menu_choice == 2:
        add_city_distance()
    elif menu_choice == 3:
        check_city_distance()
    elif menu_choice == 4:
        os.system('cls')
        g.get_graph()
        main_menu()
    elif menu_choice == 5:
        print('Done.')

def add_city():
    city = input('Enter city name: ')
    os.system('cls')
    g.add_city(city)
    main_menu()

def add_city_distance():
    city1, city2, distance = input('Enter the names of the two cities and the distance between them (city1, city2, distance): ').split(", ")
    os.system('cls')
    distance = int(distance)
    g.add_city_distance(city1, city2, distance)
    main_menu()

def check_city_distance():
    city1, city2 = input('Enter the names of the two cities to find the distance (city1, city2): ').split(', ')
    os.system('cls')
    g.route_distance(city1, city2)
    main_menu()

main_menu()
