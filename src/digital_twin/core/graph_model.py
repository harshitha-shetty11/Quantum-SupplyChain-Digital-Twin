import networkx as nx

class SupplyChainTwin:
    def __init__(self):
        self.graph = nx.Graph()
        # Expanded demo: Add more nodes and edges
        self.graph.add_node("SupplierA", type="supplier")
        self.graph.add_node("SupplierB", type="supplier")
        self.graph.add_node("Warehouse1", type="warehouse")
        self.graph.add_node("Warehouse2", type="warehouse")
        self.graph.add_node("StoreX", type="store")
        self.graph.add_node("StoreY", type="store")
        self.graph.add_edge("SupplierA", "Warehouse1", cost=10)
        self.graph.add_edge("SupplierB", "Warehouse1", cost=8)
        self.graph.add_edge("SupplierA", "Warehouse2", cost=12)
        self.graph.add_edge("Warehouse1", "StoreX", cost=5)
        self.graph.add_edge("Warehouse2", "StoreY", cost=7)
        self.graph.add_edge("Warehouse1", "Warehouse2", cost=3)
        self.graph.add_edge("Warehouse2", "StoreX", cost=9)

    def update_state(self, event):
        # Reset graph to default before applying event
        self.graph.clear()
        self.graph.add_node("SupplierA", type="supplier")
        self.graph.add_node("SupplierB", type="supplier")
        self.graph.add_node("Warehouse1", type="warehouse")
        self.graph.add_node("Warehouse2", type="warehouse")
        self.graph.add_node("StoreX", type="store")
        self.graph.add_node("StoreY", type="store")
        self.graph.add_edge("SupplierA", "Warehouse1", cost=10)
        self.graph.add_edge("SupplierB", "Warehouse1", cost=8)
        self.graph.add_edge("SupplierA", "Warehouse2", cost=12)
        self.graph.add_edge("Warehouse1", "StoreX", cost=5)
        self.graph.add_edge("Warehouse2", "StoreY", cost=7)
        self.graph.add_edge("Warehouse1", "Warehouse2", cost=3)
        self.graph.add_edge("Warehouse2", "StoreX", cost=9)

        # Apply scenario-specific changes
        if event == "Supplier Disruption":
            # Remove SupplierA and its edges
            if "SupplierA" in self.graph:
                self.graph.remove_node("SupplierA")
        elif event == "Demand Spike":
            # Increase costs to StoreX
            if self.graph.has_edge("Warehouse1", "StoreX"):
                self.graph["Warehouse1"]["StoreX"]["cost"] = 15
            if self.graph.has_edge("Warehouse2", "StoreX"):
                self.graph["Warehouse2"]["StoreX"]["cost"] = 18
        elif event == "Inventory Shortage":
            # Increase costs to StoreY
            if self.graph.has_edge("Warehouse2", "StoreY"):
                self.graph["Warehouse2"]["StoreY"]["cost"] = 17
        # For 'Normal Operation' or unknown, keep default

    def get_state(self):
        return nx.node_link_data(self.graph, edges="links")
