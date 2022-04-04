import ele,node
import turtle
class truss:

    node_list = list()
    ele_list = list()
    
    def __init__(self) :

        self.nnode= int(input("Enter the number of nodes: "))
        self.nele= int(input("Enter the number of elements: "))
        
        for i in range(1, self.nnode+1):
            # Enter the code to input node stats
            #include append to list
            pass

        for i in range(1, self.nele+1):
            # Enter the code to input element stats
            #include append to list
            pass

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
    
    def solve(self):
        pass

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
truss1.visualize()