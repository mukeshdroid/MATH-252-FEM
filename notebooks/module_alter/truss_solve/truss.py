import ele,node
import turtle
class truss:

    node_list = []
    ele_list = []
    dis_list = []
    f_list = []
    GK = []
    
    def __init__(self) :

        #commented this section now to test if solve works. 
        
        
#         self.nnode= int(input("Enter the number of nodes: "))
#         self.nele= int(input("Enter the number of elements: "))
        
#         for i in range(1, self.nnode+1):
#             # Enter the code to input node stats
#             #include append to list
#             pass

#         for i in range(1, self.nele+1):
#             # Enter the code to input element stats
#             #include append to list
#             pass

        node1 = node.nodep(1,-4,0)
        node2 = node.nodep(2,-2,0)
        node3 = node.nodep(3,0,0)
        node4 = node.nodep(4,2,0)
        node5 = node.nodep(5,4,0)
        node6 = node.nodep(6,4,2.9118)
        node7 = node.nodep(7,2,2.1842)
        node8 = node.nodep(8,0,1.4561)
        node9 = node.nodep(9,-2,0.7280)

        self.node_list = [node1,node2,node3,node4,node5,node6,node7,node8,node9,node1]

        ele1  = ele.elep(1, node1, node2)
        ele2  = ele.elep(2, node2, node3)
        ele3  = ele.elep(3, node3, node4)
        ele4  = ele.elep(4, node4, node5)
        ele5  = ele.elep(5, node5, node6)
        ele6  = ele.elep(6, node6, node7)
        ele7  = ele.elep(7, node7, node8)
        ele8  = ele.elep(8, node8, node9)
        ele9  = ele.elep(9, node9, node1)
        ele10 = ele.elep(10, node2, node9)
        ele11 = ele.elep(11, node2, node8)
        ele12 = ele.elep(12, node3, node8)
        ele13 = ele.elep(13, node4, node8)
        ele14 = ele.elep(14, node4, node7)
        ele15 = ele.elep(15, node4, node6)
        self.ele_list = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8, ele9, ele10, ele11, ele12, ele13, ele14, ele15]
    
    def globalstiff(self):
        #dimension of global matrix
        dim = 2 * len(self.node_list)
        eles = self.ele_list
        #generate and store the element-wise stiffness matrices
        SMs = [e.stiff() for e in eles]

        GK = np.zeros((dim,dim))

        for e in eles:
            i = 2 * e.node_a.num -2
            j = 2 * e.node_a.num -1
            k = 2 * e.node_b.num -2
            l = 2 * e.node_b.num -1
            e_stiff = e.stiff()

            index = [i,j,k,l]
            index2d = [(a,b) for a in index for b in index]
            d = {i:0, j:1, k:2, l:3}
            for p,q in index2d:
                GK[p][q] = GK[p][q] + e_stiff[d[p]][d[q]]
        self.GK = GK
    
    def solve(self):
        #generate global matrix by calling globalstiff method
        self.globalstiff()        
        
        for n in self.node_list:
            dis_list.append(n.dis_x)
            dis_list.append(n.dis_y)

        dis = np.array(dis_list)

        f_list = []
        for n in nodes:
            f_list.append(n.f_x)
            f_list.append(n.f_y)

        f = np.array(f_list)
        
        #check for undetermined values in dis and create linear eqns

        GK_dis =  copy.deepcopy(GK)
        f_dis =  copy.deepcopy(f)

        del_row = []
        index_list = list(range(0,2*len(nodes)))
        for i in range(0,2*len(nodes)):
            if dis_list[i] == 0:
                del_row.append(i)
                index_list.remove(i)
        GK_dis = np.delete(GK_dis,del_row,0)
        GK_dis = np.delete(GK_dis,del_row,1)
        f_dis = np.delete(f_dis,del_row,0)
        
        ans_dis = np.linalg.solve(GK_dis , f_dis)
        
        for i in range(0 , len(ans_dis)):
            dis[index_list[i]] = ans_dis[i]
            self.dis_list = dis
        
        ans_force = np.dot(GK,dis)
        self.force_list = ans_force
        
        print(self.dis_list)
        print(self.force_list)

    def visualize(self):
        turtle.title("Visualization")
        turtle.bgcolor("black")
        t = turtle.Turtle()
        t.hideturtle()
        t.pensize(5)
        t.pencolor("blue")

        for ele in self.ele_list:
            t.goto(ele.node_a.pos_x*70, ele.node_a.pos_y*70)
            t.goto(ele.node_b.pos_x*70, ele.node_b.pos_y*70)
        
        for node in self.node_list:
            t.penup()
            t.goto(node.pos_x*70, node.pos_y*70)
            t.pendown()
            t.dot(15,"red") 
        turtle.Screen().exitonclick()

truss1 = truss()
truss1.solve()
truss1.visualize()