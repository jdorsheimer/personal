import random

# Define the rooms and the items in each room
rooms = {
    "Kitchen": ["Knife", "Stove"],
    "Living Room": ["Couch", "Television"],
    "Bedroom": ["Bed", "Dresser"],
    "Bathroom": ["Shower", "Toilet"],
}

# Define the starting room
current_room = "Kitchen"

# Define the items the player has collected
collected_items = []

# Game loop
while True:
    # Display the room and its items
    print("You are in the", current_room)
    print("The items in this room are:", rooms[current_room])
    
    # Display the items the player has collected
    print("You have collected:", collected_items)
    
    # Ask the player what they want to do
    action = input("What would you like to do (Collect, Move, Quit)? ")
    
    # Collect an item
    if action == "Collect":
        # Ask the player which item they want to collect
        item = input("Which item would you like to collect? ")
        
        # Check if the item is in the room
        if item in rooms[current_room]:
            # Add the item to the player's inventory
            collected_items.append(item)
            
            # Remove the item from the room
            rooms[current_room].remove(item)
            
            print("Item collected.")
        else:
            print("Item not found.")
    
    # Move to a different room
    elif action == "Move":
        # Display the possible rooms to move to
        print("The rooms you can move to are:", list(rooms.keys()))
        
        # Ask the player which room they want to move to
        destination = input("Which room would you like to move to? ")
        
        # Check if the destination is a valid room
        if destination in rooms:
            current_room = destination
            
            print("You have moved to the", destination)
        else:
            print("Invalid room.")
    
    # Quit the game
    elif action == "Quit":
        print("Goodbye!")
        break
    
    # Invalid action
    else:
        print("Invalid action.")
