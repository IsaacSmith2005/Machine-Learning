from collections import defaultdict
from queue import PriorityQueue

class Node:
    def __init__(self, name, par=None, h=0):
        self.name = name
        self.par = par
        self.h = h  # Chi phí từ gốc đến nút này
        
    def display(self):
        print(self.name, self.h)    
        
    def __lt__(self, other):
        if other is None:
            return False
        return self.h < other.h
    
    def __eq__(self, other):
        if other is None:
            return False
        return self.name == other.name

data = defaultdict(list)
data['A'] = [('D', 3), ('B', 5)]    
data['B'] = [('C', 1)]
data['C'] = [('E', 6), ('G', 8)]
data['D'] = [('E', 2), ('F', 2)]
data['E'] = [('B', 4)]
data['F'] = [('G', 3)]
data['G'] = [('E', 4)]

def uniform_cost_search(start='A', goal='G'):
    start_node = Node(name=start, h=0)
    open_set = PriorityQueue()
    open_set.put(start_node)
    closed_set = set()

    while not open_set.empty():
        current_node = open_set.get()
        
        # Nếu nút đã được xử lý, bỏ qua
        if current_node.name in closed_set:
            continue
        
        closed_set.add(current_node.name)

        # Kiểm tra nếu đã đến đích
        if current_node.name == goal:
            print('Đã tìm thấy đích')
            get_path(current_node)
            return
        
        # Duyệt qua các nút con
        for neighbor, cost in data[current_node.name]:
            total_cost = current_node.h + cost
            neighbor_node = Node(name=neighbor, par=current_node, h=total_cost)

            if neighbor not in closed_set:
                open_set.put(neighbor_node)

def get_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.par
    path.reverse()
    
    print('Đường đi từ điểm đầu đến điểm cuối:', path)
    print('Số lượng bước đi:', len(path) - 1)

uniform_cost_search()