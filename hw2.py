class Solution: 
    def canVisitAllRooms(self, rooms): 
        visited = set() 
        queue = deque([0]) 
 
        while queue: 
            room = queue.popleft() 
            if room not in visited: 
                visited.add(room) 
                queue.extend(key for key in rooms[room] if key not in visited) 
 
        return len(visited) == len(rooms)