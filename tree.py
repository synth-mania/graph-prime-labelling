class Node:
    def __init__(self, value: any = None, parent: "Node" = None):
        self.value = value
        self.branch: list["Node"] = []
        self.parent = parent

    def grow_child(self):
        new_child = Node(parent = self)
        self.branch.append(new_child)
        return new_child

    def get_children(self) -> list["Node"]:
        return self.branch.copy()

    def get_parent(self) -> "Node":
        return self.parent

    def remove(self):
        if self.parent is None:
            return  # There's no parent, so just return

        for i, child in enumerate(self.parent.branch):
            if self is child:  # You can safely use 'is' or '==' to compare object identities
                self.parent.branch.pop(i)  # Remove this instance from the parent's branch
                return  # Once removed, break out of the loop