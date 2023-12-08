class Node:
    def __init__(self, key, tooltip="", parents=[], weights=[]):
        self.children = []
        self.parents = parents
        self.val = key
        self.tooltip = tooltip
        self.weights = weights
        for i, parent in enumerate(parents):
            parent.children.append(self)
            if i < len(weights):
                parent.weights.append(weights[i])
            else:
                parent.weights.append('')
