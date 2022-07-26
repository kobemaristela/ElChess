class Room:
    def __init__(self, walls: list, gates: list, adjacent_rooms: list) -> None:
        self.walls = walls
        self.gates = gates

        #indeces will signify direction the room is in: 0 - left, 1 - right, 2- top, 3- down
        self.left_room = adjacent_rooms[0]
        self.right_room = adjacent_rooms[1]
        self.top_room = adjacent_rooms[2]
        self.bottom_room = adjacent_rooms[3]