from node import node
from ele import ele
import turtle
import numpy as np
import math
import copy

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

        node1 = node(1,0,0,0,0,np.nan,np.nan)
        node2 = node(2,2,0,0,0,np.nan,np.nan)
        node3 = node(3,2,2,np.nan,np.nan,0.1,-0.2)

        self.node_list = [node1,node2,node3]

        ele1 = ele(1,1,1,1, 0 , node1 , node2)
        ele2 = ele(2,1,1, 1 , math.pi / 2 , node2 , node3)
        ele3 = ele(3,1*math.sqrt(2),1, 1 , math.pi / 4 , node1 , node3)

        self.ele_list = [ele1, ele2, ele3]
    
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
        
        dis_list = []
        for n in self.node_list:
            dis_list.append(n.dis_x)
            dis_list.append(n.dis_y)

        dis = np.array(dis_list)

        f_list = []
        for n in self.node_list:
            f_list.append(n.f_x)
            f_list.append(n.f_y)

        f = np.array(f_list)
        
        #check for undetermined values in dis and create linear eqns

        GK_dis =  copy.deepcopy(self.GK)
        f_dis =  copy.deepcopy(f)

        del_row = []
        index_list = list(range(0,2*len(self.node_list)))
        for i in range(0,2*len(self.node_list)):
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
        
        ans_force = np.dot(self.GK,dis)
        self.force_list = ans_force
        
        k = 0
        for i in self.node_list:
            i.dis_x = self.dis_list[k]
            k = k  + 1
            i.dis_y = self.dis_list[k]
            k = k  + 1
              
        
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
        #turtle.Screen().exitonclick()
       
	t.goto((ele[0].node_a.pos_x + ele[0].node_a.dis_x)*70, (ele[0].node_a.pos_y + ele[0].node_a.dis_y)*70)
 
        #after solving
        t.pencolor("green")        
        for ele in self.ele_list:
            t.goto((ele.node_a.pos_x + ele.node_a.dis_x)*70, (ele.node_a.pos_y + ele.node_a.dis_y)*70)
            t.goto((ele.node_b.pos_x + ele.node_b.dis_x)*70, (ele.node_b.pos_y + ele.node_b.dis_y)*70)
        
        for node in self.node_list:
            t.penup()
            t.goto((node.pos_x + node.dis_x)*70, (node.pos_y  + node.dis_y)*70)
            t.pendown()
            t.dot(15,"yellow") 
        turtle.Screen().exitonclick()

truss1 = truss()
truss1.solve()
truss1.visualize()
