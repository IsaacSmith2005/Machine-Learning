#Thuật toán tìm kiếm theo chiều rộng (BFS)

#Khai báo class
class Node:
    def __init__(self, name, par = None):
        self.name = name
        self.par = par
        
#Biểu diễn cây
from collections import defaultdict
data = defaultdict(list)
data['A'] = ['B', 'C', 'D']
data['B'] = ['E', 'F']
data['C'] = ['G', 'H']
data['D'] = ['I', 'J']
data['F'] = ['K', 'L', 'H']
data['H'] = ['N', 'O']

#In đư��ng đi

def induongdi(O):
    if O.par is None:
        print(O.name, end = '')
        return
    induongdi(O.par)
    print(f' -> {O.name}', end = '')

# Thuật toán BFS
<<<<<<< HEAD
def BreadthFirstSearch(S = Node('A'), GG = Node('O')):
=======
def BestFirstSearch(S = Node('A'), GG = Node('O')):
>>>>>>> 58076f0efc6a8f3908ad846ec5781b3993d9f9b9
    Open = []
    Closed = []
    #B1: Cho đỉnh xuất phát vào Open
    Open.append(S)
    while True:
        #B2: Nếu Open rỗng thì tìm kiếm thất bại, kết thúc chương trinh
        if len(Open) == 0:
            print('Không tìm thấy đích')
            break
        #B3: Lấy đỉnh đầu trong Open ra và gọi đó là O, cho O và closed
        O = Open.pop(0)
        Closed.append(O)
        print(f'Duyệt: {O.name}')
        #B4: Nếu O là đỉnh đích thì tìm kiếm thành công, kết thúc chương trình
        if O.name == GG.name:
            print('Đã tìm thấy đích.')
            print('Đường đi: ', end='')
            #in đườnng đi
            induongdi(O)
            break
        #B5: Tìm tất cả đỉnh con của O
        for i in data[O.name]:
            tam = Node(i, par=O)
            #B6: Nếu đinh con chưa trong Open và Closed thì đưa vào Open
            if tam.name not in [x.name for x in Open] and tam.name not in [x.name for x in Closed]:
                Open.append(tam)

<<<<<<< HEAD
BreadthFirstSearch()
=======
BestFirstSearch()
>>>>>>> 58076f0efc6a8f3908ad846ec5781b3993d9f9b9
