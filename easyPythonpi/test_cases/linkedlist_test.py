import unittest
import sys, os
p=os.getcwd()[:-11]
sys.path.append(f"{p}/methods")
l=f"{p}/methods/linkedlist"
from linkedlist import *

class LinkedListTest(unittest.TestCase):

    def test_create_node(self):
        data = 3
        #Creating a node using create_node 
        node = create_node(data)
        #Asserting that the data matches and next is none
        self.assertEqual(node.data, 3)
        self.assertIsNone(node.next)

    def test_linking_nodes(self):
        #Creating two nodes
        node_a = create_node(2)
        node_b = create_node(3)
        #Linking the 2 nodes
        node_link(node_a,node_b)
        #Checking if both the nodes are linked
        self.assertEqual(node_a.next,node_b)
        self.assertIsNone(node_b.next)

    def test_count_node(self):
        #Testing the value of count if head is none
        self.assertEqual(count_node(None),0)
        #Created 3 nodes and linked them
        head = create_node(1)
        node_a = create_node(2)
        node_link(head,node_a)
        node_b = create_node(3)
        node_link(node_a,node_b)
        #Asserting if the value of count is 3
        self.assertEqual(3,count_node(head))


if __name__ == "__main__":
    unittest.main()

    
        
