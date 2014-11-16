class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

def print_list(head=None):
    """Prints linked list contents recursively"""
    print head
    if(head.next):
        print_list(head.next)

def print_list_reverse(head=None):
    """Prints linked list backwards """
    if(head==None):
        return

    top = head

    tail = head.next
    print_list_reverse(tail)
    print top

def delete_node(head, nodetodelete):
    """Delete a node in the linked list"""

    #Nothing to do if the head is None or the nodetodelete is None
    if not head and not nodetodelete:
        print 'Nothing to delete. No arguments passed in'
        return

    #is the nodetodelete the head node, deal with that.
    node=head

    while(node.next):
        if(node.next == nodetodelete):
            if(node.next.next == None):
                node.next = None
            else:
                node.next = node.next.next

            #After finding the relevant nodetodelete, break out of the loop
            break
        node = node.next


if(__name__=="__main__"):
    #Create the nodes and next pointers
    head_node = Node('Ganesh');
    node2 = Node('Raji');
    node3 = Node('Pattu');
    node4 = Node('Bunny');

    head_node.next = node2
    node2.next = node3
    node3.next = node4

    delete_node(head_node, node4)
    print_list(head_node)
