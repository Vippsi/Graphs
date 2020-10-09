from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

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


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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
opposites = {"n": "s", "e": "w", "s": "n", "w": "e"}

traversal_graph = {}

traversal_graph[player.current_room.id] = {}
for direction in player.current_room.get_exits():
    if direction not in traversal_graph[player.current_room.id]:
        traversal_graph[player.current_room.id][direction] = "?"

def add_to_traversal_graph(room):
    traversal_graph[room.id] = {}
    for direction in room.get_exits():
        if direction not in traversal_graph[room.id]:
            traversal_graph[room.id][direction] = "?"
        else: continue
    return traversal_graph


# def get_random_direction(all_unexplored_exits):
#     random_next_direction = random.choice(all_unexplored_exits)
#     return random_next_direction

def get_available_exits(current_room):
    exits = []
    # print(current_room.id)
    for exit_option in traversal_graph[current_room.id]:
        if traversal_graph[current_room.id][exit_option] == "?":
            exits.append(exit_option)
    return exits

    

def dft(room):
    # yes = True
    while len(get_available_exits(room)) > 0:
    # while yes == True:
        random_direction = random.choice(get_available_exits(room))
        prev_room = room

        traversal_path.append(random_direction)
        direction = traversal_path[-1]

        player.travel(direction)

        new_room = player.current_room

        if new_room.id not in traversal_graph:
            add_to_traversal_graph(new_room)
    
            # yes = False
        traversal_graph[new_room.id][opposites[random_direction]] = prev_room.id
        traversal_graph[prev_room.id][random_direction] = new_room.id

        room = player.current_room
    print(room)
    return room


    def bfs_nearest_room(room):
        print("INSIDE OF BFS_NEAREST")
        q = Queue()
        temp = None
        visited = set()

        q.enqueue(room)

        if len(get_available_exits(room)) > 0:
            start_room == room
            print("this is temp",temp)
            return start_room
        
            for available_exit in get_available_exits(room):
                q.enqueue(available_exit)
        
    def bft_path(start_room, target_room):
        q = Queue()
        visited = set()
        final_path =[]
        q.enqueue([start_room])
        
        while q.size() > 0:
            room = q.dequeue()
            v = room[-1]

        if v == target_room:
            final_path = room
            
        else:
            for neighbor_room in list(traversal_graph[room].values()):
                newest_room = room + [neighbor_room]
                q.enqueue(newest_room)
        print(final_path)
        return final_path



# print(player.current_room.id)
# dft(player.current_room)
dft(player.current_room)
print("traversal graph", traversal_path)

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
