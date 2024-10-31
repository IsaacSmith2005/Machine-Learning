from collections import defaultdict
from queue import PriorityQueue

# Tạo class Node
class Node:
    def __init__(self, name, par=None, h=0):
        self.name = name
        self.par = par
        self.h = h
    
    def display(self):
        print(self.name, self.h)

    def __lt__(self, other):
        return self.h < other.h if other else False

    def __eq__(self, other):
        return self.name == other.name if other else False

# Biểu diễn cây
data = defaultdict(list)
data['A'] = ['B', 'C', 'D', 6]
data['B'] = ['E', 'F', 3]
data['C'] = ['G', 'H', 4]
data['D'] = ['I', 'J', 5]
data['E'] = [3]
data['F'] = ['K', 'L', 'M', 1]
data['G'] = [6]
data['H'] = ['N', 'O', 2]
data['I'] = [5]
data['J'] = [4]
data['K'] = [2]
data['L'] = [0]
data['M'] = [4]
data['N'] = [0]
data['O'] = [4]

def equal(O, G):
    return O.name == G.name

def checkInPriority(tmp, Priority):
    temp_list = list(Priority.queue)
    for item in temp_list:
        if equal(item, tmp):
            return True
    return False

def getPath(O):
    path = []
    distance = 0
    while O is not None:
        path.append(O.name)
        if O.par is not None:
            distance += data[O.name][-1]
        O = O.par
    path.reverse()
    print(f"Đường đi: {' -> '.join(path)}, Tổng khoảng cách: {distance}")

def BestFirstSearch(S=Node(name='A'), G=Node(name='N')):
    Open = PriorityQueue()
    Closed = PriorityQueue()
    S.h = data[S.name][-1]
    Open.put(S)
    
    while not Open.empty():
        O = Open.get()
        Closed.put(O)
        print(f'Duyệt: {O.name}, {O.h}')
        
        if equal(O, G):
            print('Tìm kiếm thành công')
            getPath(O)
            return
        
        i = 0
        while i < len(data[O.name]) - 1:
            name = data[O.name][i]
            h = data[name][-1]
            tmp = Node(name=name, h=h, par=O)  # Thiết lập cha cho mỗi Node
            ok1 = checkInPriority(tmp, Open)
            ok2 = checkInPriority(tmp, Closed)
            if not ok1 and not ok2:
                Open.put(tmp)
            i += 1
    
    print('Tìm kiếm thất bại')

BestFirstSearch()