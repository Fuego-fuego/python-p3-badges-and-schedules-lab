def badge_maker(name):
    badge = f"Hello, my name is {name}."
    return badge

def batch_badge_creator(names):
    badges = [ badge_maker(name) for name in names]
    return badges

def assign_rooms(names):
    
    rooms = []
    room_number = 1
    for name  in names:
        rooms.append(f"Hello, {name}! You'll be assigned to room {room_number}!")
        room_number += 1
    return rooms

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    
    for badge in badges:
        print(badge)
        
    for room in rooms:
        print(room)
    return None
