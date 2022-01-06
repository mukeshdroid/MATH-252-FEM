#class for nodes
class ele:
   
    # init method or constructor 
    #nan values are used to indicate if the value needs to be determined.
    def __init__(self, num, length , area , ym , theta, node_a , node_b):
        self.num = num
        self.len = length
        self.area = area
        self.ym = ym
        self.theta = theta
        self.node_a = node_a 
        self.node_b = node_b