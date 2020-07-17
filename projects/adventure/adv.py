from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#------------------------------------------------------------------------------------------------------------------------------
# player.current_room.id
exits = player.current_room.get_exits()
# player.travel(direction)
# print(f' {player.travel("n")}, {player.current_room.id}, {player.current_room.get_exits()} ')
# print(f' {player.travel("n")}, {player.current_room.id}, {player.current_room.get_exits()} ')
# print(f' {player.travel("n")}, {player.current_room.id}, {exits} ')

print(f'room_graph: {len(room_graph)} ')
def get_id():
    id = player.current_room.id
    return id

def get_exits():
    exits = player.current_room.get_exits()
    return exits

room_map = {}
room_map[get_id()] = {d: '?' for d in get_exits()}

def get_neighbors(direction):
    
    current_room = get_id()
    # print(direction)
    if direction == 'n': 
        player.travel("n")
        room_map[current_room].update({'n': get_id()})
        room_map[get_id()] = {d: '?' for d in get_exits()}
        room_map[get_id()].update({'s': current_room})
    if direction == 's':
        player.travel("s")
        room_map[current_room].update({'s': get_id()})
        room_map[get_id()] = {d: '?' for d in get_exits()}
        room_map[get_id()].update({'n': current_room})
    if direction == 'w':
        player.travel("w")
        room_map[current_room].update({'w': get_id()})
        room_map[get_id()] = {d: '?' for d in get_exits()}
        room_map[get_id()].update({'e': current_room})   
    if direction == 'e':
        player.travel("e")
        room_map[current_room].update({'e': get_id()})
        room_map[get_id()] = {d: '?' for d in get_exits()}
        room_map[get_id()].update({'w': current_room})
    
    return get_id()

def visit_all_rooms():
    s = Stack()   
    s.push(get_id())
    rooms_visited = set()
    current_room = ''

    check_point = set()
    check_point.add(get_id())
    to_check_point = False
    check_point_path = []
    

    while len(rooms_visited) < len(room_graph) and s.size() != 0:
        current_room = s.pop()
        
        if current_room not in rooms_visited:
            rooms_visited.add(current_room)
        
        if to_check_point:
            if check_point_path[-1] is 'n':
                s.push(get_neighbors('s'))
                check_point_path.pop()
            elif check_point_path[-1] is 's':
                s.push(get_neighbors('n'))
                check_point_path.pop()
            elif check_point_path[-1] is 'e':
                s.push(get_neighbors('w'))
                check_point_path.pop()
            elif check_point_path[-1] is 'w':
                s.push(get_neighbors('e'))
                check_point_path.pop()
            else:
                to_check_point = False
        
        if room_map[current_room].get('n') is '?':
            s.push(get_neighbors('n'))
            check_point_path.append('s')
        elif room_map[current_room].get('s') is '?':
            s.push(get_neighbors('s'))
            check_point_path.append('n')
        elif room_map[current_room].get('w') is '?':
            s.push(get_neighbors('w'))
            check_point_path.append('e')
        elif room_map[current_room].get('e') is '?':
            s.push(get_neighbors('e'))
            check_point_path.append('w')
        else:
            to_check_point = True

        
        print('map:', room_map)
        print('rooms:',rooms_visited)
        
visit_all_rooms()
#------------------------------------------------------------------------------------------------------------------------------
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
