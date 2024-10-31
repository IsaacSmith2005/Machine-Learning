from collections import defaultdict
from queue import PriorityQueue

# Tạo code Best First Search
class Node:
    def __init__(self, name, par=None, h=0):
        self.name = name
        self.par = par
        self.h = h
    
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

data = defaultdict(list)
data['A'] = [('D', 3), ('B', 5)]    
data['B'] = [('C', 1)]
data['C'] = [('E', 6), ('G', 8)]
data['D'] = [('E', 2), ('F', 2)]
data['E'] = [('B', 4)]
data['F'] = [('G', 3)]
data['G'] = [('E', 4)]

def best_first_search(S=Node(name='A'), G=Node(name='G')):
    Open = PriorityQueue()
    Closed = PriorityQueue()
    S.h = data[S.name][-1]
    Open.put(S)
    while True:
        if Open.empty():
            print('Không tìm thấy đích.')
            return
        O = Open.get()
        Closed.put(O)
        print('Duyệt: ', O.name, O.h)
        if equal(O, G):
            print('Đã tìm thấy đích')
            distance = 0
            getPath(O, distance)
            return
        
        # Check children of O
        i = 0
        while i < len(data[O.name]) - 1:
            name = data[O.name][i]
            h = data[name][-1]
            tmp = Node(name=name, h=h)
            tmp.par = O  # Set parent node
            
            oK1 = checkInPriority(tmp, Open)
            oK2 = checkInPriority(tmp, Closed)
            
            if not oK1 and not oK2:
                Open.put(tmp)
            i += 1

def equal(O, G):
    if O.name == G.name:
        return True
    return False

def checkInPriority(node, queue):
    tmp_list = []
    found = False
    while not queue.empty():    
        tmp = queue.get()
        tmp_list.append(tmp)
        if tmp.name == node.name:
            found = True
            break
    
    # Reinsert items back into queue after checking
    for item in tmp_list:
        queue.put(item)
    
    return found

def getPath(node, distance):
    path = []
    while node.par is not None:
        path.append(node.name)
        node = node.par
        distance += 1
    path.append(node.name)
    path.reverse()
    
    print('Đường đi từ điểm đầu đến điểm cuối: ', path)
    print('Số lượng bước đi: ', distance)

best_first_search() 

