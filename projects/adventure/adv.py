from room import Room
from player import Player
from world import World

from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


def get_traversal_path():
    rooms = {}
    opposites = {"n": "s", "e": "w", "s": "n", "w": "e"}


    def dft(current_room, visited=None):

        if not visited:
            visited = set()
        if current_room.id in visited:
            # print(visited)
            return
        
        visited.add(current_room.id)


        rooms[current_room.id] = {}

        exits = current_room.get_exits()


        for exit_path in exits:
            neighbor = current_room.get_room_in_direction(exit_path)
            rooms[current_room.id][exit_path] = neighbor.id

        
    
            dft(neighbor, visited)



    def bfs(starting_id, destinantion_id):
        q = Queue()
        q.enqueue([starting_id])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            current_room_id = path[-1]

            if current_room_id in visited:
                continue
            elif current_room_id == destinantion_id:
                return path
        
            visited.add(current_room_id)

            for room_id in rooms[current_room_id].values():
                q.enqueue(path + [room_id])


    


    
    dft(player.current_room)

    ids = list(rooms.keys())

    traversal_path = []


    for i in range(len(ids)-1):
        path = bfs(ids[i], ids[i+1])
        

        
        for j in range(len(path)-1):
            current_room_id = path[j]
            next_room_id = path[j+1]

            for k, v in rooms[current_room_id].items():
                if v == next_room_id:
                    traversal_path.append(k)
   
    return traversal_path


traversal_path = get_traversal_path()


# print(traversal_path)


""" Start in the starting room, look at all possible exits with get_exits(), 
choose one using random go to the next room, 
mark it as visited also mark that rooms opposite direction as known, when we hit a dead end, that is, there is no other exit then the way we came then we need to go back one room, once we're there, check to see if there are any other unexplored directions, if so, use our random choice to pick one, and repeat, do this until the length of our traversal path is 500""" 

# bfs(player.current_room.id)
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
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms\n {len(traversal_path)} moves,")



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
