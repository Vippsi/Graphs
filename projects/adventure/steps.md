Marlon's Algorithm

Before you proceed:
a. have a traversal graph(an actual graph or just a normal dictionary) that
has the starting room as key. the value will be a dictionary with directions as keys
and "?" as value
    eg: {0: {n: "?", s: "?", e: "?", w:"?"}}
    - do not hardcode this
    - you can get 0 from one of the attributes in player class
    - you can do a dictionary comprehension to generate the 'n: "?"...' part using the
    list of exits available for that room

b. opposite_dir(either a dictionary or an attribute in your graph class)
    - key will be direction and value will be opposite of the key


c. traversal_path which will contain all the directions you traverse

1. Function to get available exits(directions in traversal_graph that has "?" as value)
   for current room
   - this function accepts a room as argument
   - declare an empty list which will contain the directions that are still available for the given room
   - loop through the dictionary of available exits ({n: "?", s: "?", e: "?", w:"?"})
     - if the direction has a value of "?", append it to the list
   - return the list
   ** Notes
   - this function will return an empty list if you are on a dead end

2. Function to traverse list until you reach a dead end(room with no available exits) -> DFT
    - this will take a room as an argument
    - we'll set up a while loop with the condition that as long as there are AVAILABLE EXITS  in the current room, we'll continue running the code inside this loop

    - first, we randomly choose a direction from the LIST OF AVAILABLE EXITS
    - we also want to store the current room we're in to a variable so we can reference later once we travel
    - we can then append that direction to traversal_path

    - at this point, we're on a different room, check if the room doesn't exist in your traversal graph

        - if it doesn't, add it to your traversal graph
    - outside of the if statement, add the previous room you're in as the value of the opposite direction that you traveled in your traversal graph
            eg: 0: {n: "?", s:"?", e:"?", w:"?"}
            - we picked "n" as random direction and traverse it
            - we add the current room to our traversal graph so it now looks like this:
                0: {n: "?", s:"?", e:"?", w:"?"}
                1: {n:"?" s:"?"}
            - outside of if statement, we add 0 as the value of the opposited direction in the current room we're in
                0: {n: "?", s:"?", e:"?", w:"?"}
                1: {n:"?" s: 0}
            - we do the same for the previous room we're in
                0: {n: 1, s:"?", e:"?", w:"?"}
                1: {n:"?" s: 0}
    - lastly, you want to update the room to be the new room you're currently in
            room = player.current_room.id

            
3. From dead end, this function returns the room(which will be used as target) - BFS Nearest room
    - this function takes in a room as an argument
    - we create a queue and add the room to it and also set up your visited set
    - declare a variable and initialize it as None or 0
    - do a bft traversal
        - after adding the room to your set, have an if statement to check if the length of AVAILABLE EXITS for that room is greater than 0
            - if it is, that's your target room and set the value of the variable you declared eaelier as that room and return it
        - loop through the current room's available exits and append the ROOM(not the direction) to your queue 
4. Still on dead end, this function will return a list containing all the directions
   to travel in order to get to target room - BFT PATH
   - this function takes in a TARGET ROOM and a starting room, which is the current room you're in, as arguments
   - we create a queue, but this time, instead of adding just the room, we're going to add an array containing the starting room 
   - we also create a visited set
   - and a final_path which will contain all the directions
   - same thing as normal BFS
        - after you've added the room to your visited set, check have an if statement checking if the room[-1](since room is actually an array and we only want the last element there) is the same as TARGET ROOM, assign room(which is the path or a list) as the new value of final_path and "break" out of the while loop
        - else:
            - do the loop 
            - if you use traversal_graph[room] in your for loop, this will give you the keys, which are directions and we don't want that
            - instead, we want to use list(traversal_graph[room].values())
            - we create a copy of room and add the neighbor rooms just like in BFS in your assignment
    - AFTER THE WHILE LOOP EXECUTES
    - your final path should now have the rooms path which should look something like this
            eg: if you use this map "maps/test_loop_fork.txt" and you're in room 17 if 1 has north and east unexplored
                [17, 16, 15, 1]
    - now we declare a new path list which will contain the directions that we'll need to traverse to get to our target room
    - for loop using the length of final_path
        - inside this for loop, we'll have another for loop looping over traversal_graph[final_path[i]]
            - this for loop will loop over the directions available to that room
            - have an if statement checking if the traversal_graph[final_path[i]][direction] is the same as final_path[i + 1]
                - so for [17, 16, 15, 1], in your traversal_graph, 17: {s: "16"}
                - so for room 17, traversal_graph[final_path[i]][direction] is equal to 16
                - if it is, we append it new path list we created
    - after your for loop, return the path
5. we create a while loop that will finally complete this damn thing
    - the condition is that as long as the length of your traversal graph is not equal to the number of rooms in your map, continue to do these stuff
    - we use DFT function passing in the player's current room id
    - grab the nearest room using your BFS Nearest Room function
    - grab the path to nearest using your BFT PATH function
    - loop over the result of BFT PATH 
        - travel to each direction
        - append each direction to your traversal path