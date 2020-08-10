class TreeNode:

    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.next_in_level = None
        self.node_value = None

    def get_value(self):
        return self.node_value

    def set_value(self, value):
        self.node_value = value

    def get_left_child(self):
        return self.left

    def set_left_child(self, value):
        self.left = value

    def get_right_child(self):
        return self.right

    def set_right_child(self, value):
        self.right = value

    def get_next_in_level(self):
        return self.next_in_level

    def set_next_in_level(self, value):
        self.next_in_level = value


def link_next_in_line(root:TreeNode):
    current_list = []
    levels_list = []

    if (root is None):
        return
    levels_list.append(root)

    while (len(levels_list) > 0):
        current_list = list(levels_list)
        levels_list = []

        for i in range(len(current_list)):
            current_node = TreeNode(current_list[i])
            j = i + 1

            if (j < len(current_list)):
                next_node = TreeNode(current_list[j])
                current_node.set_next_in_level(next_node)

            if (current_node.get_right_child != None):
                levels_list.append(current_node.get_right_child())
            
            if (current_node.get_left_child != None):
                levels_list.append(current_node.get_left_child())

def main():
    print("Hello world")


main()
