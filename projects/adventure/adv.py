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
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# ------------------------------------------------------------------------------------------------------------------------------
# player.current_room.id
# exits = player.current_room.get_exits()

rev_dir = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

print(f'room_graph: {len(room_graph)} ')


def get_id():
    id = player.current_room.id
    return id


def get_exits():
    exits = player.current_room.get_exits()
    return exits


def visit_all_rooms(starting_vertex, visited=set()):
    path = []

    for d in get_exits():
        player.travel(d)
        if get_id() not in visited:
            visited.add(get_id())
            path.append(d)

            path = path + visit_all_rooms(get_id(), visited)

            if len(visited) != len(room_graph):
                player.travel(rev_dir[d])
                path.append(rev_dir[d])
            else:
                break
        else:
            player.travel(rev_dir[d])

    return path


traversal_path = visit_all_rooms(get_id())

# ------------------------------------------------------------------------------------------------------------------------------
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
