import tkinter as tk

class GraphVisualizer:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=500, bg="lightgray")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.node_tooltips = {}
        self.tooltip_label = tk.Label(root, text="", bg="yellow")
        self.setup_bindings()

    def setup_bindings(self):
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<Motion>", self.on_canvas_motion)

    def on_canvas_motion(self, event):
        item = self.canvas.find_closest(event.x, event.y)
        tags = self.canvas.gettags(item)
        for tag in tags:
            if "node" in tag:
                node_info = self.node_tooltips.get(tag, None)
                if node_info:
                    bbox = self.canvas.bbox(item)
                    tooltip_x = (bbox[0] + bbox[2]) / 2
                    tooltip_y = bbox[1] - 10
                    self.tooltip_label.config(text=node_info)
                    self.tooltip_label.place(x=tooltip_x, y=tooltip_y, anchor="s")
                break
        else:
            self.tooltip_label.place_forget()

    def on_press(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def on_drag(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def generate_positions_by_level(self, root, canvas_width, canvas_height):
        levels = {}
        queue = [(root, 0)]
        while queue:
            current, level = queue.pop(0)
            if level not in levels:
                levels[level] = []
            levels[level].append(current)
            for child in current.children:
                queue.append((child, level + 1))

        max_level = max(levels.keys())
        level_distance = canvas_height / (max_level + 1)
        positions = {}

        for level, nodes in levels.items():
            num_nodes = len(nodes)
            for i, node in enumerate(nodes):
                x = canvas_width * (i + 1) / (num_nodes + 1)
                y = (level + 1) * level_distance
                positions[node.val] = (x, y)

        return positions

    def draw_graph(self, nodes, positions):
        for node in nodes:
            x, y = positions[node.val]
            oval = self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="white", tags=f"node{node.val}")
            self.canvas.create_text(x, y, text=node.val)
            self.node_tooltips[f"node{node.val}"] = node.tooltip
            
            for i, child in enumerate(node.children):
                cx, cy = positions[child.val]
                self.canvas.create_line(x, y, cx, cy)
                weight = node.weights[i]
                wx, wy = (x + cx) / 2, (y + cy) / 2
                self.canvas.create_text(wx, wy, text=weight)

