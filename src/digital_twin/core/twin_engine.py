# Core engine for managing the digital twin state

class TwinEngine:
    def __init__(self, twin):
        self.twin = twin

    def apply_event(self, event):
        self.twin.update_state(event)

    def get_snapshot(self):
        return self.twin.get_state()
