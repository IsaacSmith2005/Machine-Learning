from collections import defaultdict

#Depth Firt Search
#Khai báo class
class Node:
    def __init__(self, name, par = None):
        self.name = name
        self.par = par

#Biểu diễn cây
data = defaultdict(list)
data['A'] = ['B', 'C', 'D']
data['B'] = ['E', 'F']
data['C'] = ['G', 'H']
data['D'] = ['I', 'J']
data['F'] = ['K', 'L', 'M']
data['H'] = ['N', 'O']
print(data)

#Khai báo tìm kiếm theo chiều sâu
def DepthFirtSearch(S = Node('A'), G = Node('O')):
    Open = []
    Closed = []
    #B1: Cho đỉnh xuất phát vào Open
    Open.append(S)
    while True:
        #B2: Nếu Open rỗng thì tìm kiếm thất bại, kết thúc chương trình
        if len(Open) == 0:
            print('Không tìm thấy đích.')
            return
        #B3: Lấy đỉnh đầu trong open ra gọi O, cho O vào closed
        O = Open.pop()
        Closed.append(O)
        print(f"Duyệt: {O.name}")
        #B4: Nếu O là đích thì tìm kiếm thành công, kết thúc chương trình
        if O.name == G.name:
            print('Đã tìm thấy đích.')
            #in đường đi
            induongdi(O)
            return
        #B5: Tìm tất cả đỉnh con của O
        for i in data[O.name]:
            if i not in [x.name for x in Closed]:
                new_node = Node(i, O)
                Open.append(new_node)
        #B6: Trở lại bước 2
        
def induongdi(node):
    path = []
    while node:
        path.append(node.name)
        node = node.par
    path.reverse()
    print('Đường đi từ điểm đầu đến điểm cuối: ', path)
    print('Số lượng bước đi:', len(path)) 
    
DepthFirtSearch()