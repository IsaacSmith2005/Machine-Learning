from collections import defaultdict
from queue import PriorityQueue


# Biểu diễn dữ liệu cây 
data = defaultdict(list)
data['A'] = ['C', 17, 'D', 12, 'E', 15 ,'F', 20, 30]
data['B'] = [0]
data['C'] = ['H', 12, 25]
data['D'] = ['E', 8, 'H', 10, 20]
data['E'] = ['I', 9, 'K', 10, 24]
data['F'] = ['G', 13, 'I', 12, 'N', 16, 22]
data['G'] = ['N', 10, 17]
data['H'] = ['B', 18, 'K', 11, 16]
data['I'] = ['B', 6, 'K', 5, 'N', 9, 13]
data['K'] = ['B', 8, 14]
data['N'] = ['B', 7, 12]
print(data)

#Khai báo class
class Node:
    def __init__(self, name, par = None, g = 0, h = 0):
        self.name = name
        self.par = par
        self.g = g
        self.h = h
    
    def __lt__(self, other):
        return self.g + self.h < other.g + other.h
    
def getPath(node):
    path = []
    while node is not None:
        path.append(node.name)
        node = node.par
    path.reverse()
    
    print('Đường đi từ điểm đầu đến điểm cuối: ', path)
    print('Số lượng bước đi:', len(path))       
                
def Astar(S = Node('A'), G = Node('B')):
    Open = PriorityQueue()
    Closed = PriorityQueue()
    #B1: Cho đỉnh xuất phát vào open
    Open.put(S)
    S.h = data[S.name][-1]
    while True:
        #B2: Nếu open rỗng thì tìm kiếm thất bại, kết thúc chương trình
        if Open.empty():
            print('Không tìm thấy đường đi')
            return
        #B3: Lấy đỉnh đầu trong Open ra và gọi đó là O, cho O và closed
        O = Open.get()
        Closed.put(O)
        print(f"Duyệt: {O.name}")
        #B4: Nếu O là đỉnh đích thì tìm kiếm thành công, kết thúc việc tìm kiếm
        if O.name == G.name:    
            print('Tìm thấy đường đi')
            #in đường đi
            getPath(O)
            #in khoảng cách
            print("Khoảng cách các bước đi:", O.g + O.h)
            return
        
        #B5: Tìm tất cả các đỉnh con của O không thuộc open và closed cho vào open theo thứ tự tăng dần
        for i in range(0, len(data[O.name])-1, 2):
            name = data[O.name][i]
            g = O.g + data[O.name][i + 1]
            h = data[name][-1]
            tam = Node(name, O, g, h)
            if tam.name not in Closed.queue and tam.name not in Open.queue:
                Open.put(tam)
        #B6: Trở lại bước 2

Astar(Node('A'), Node('B'))