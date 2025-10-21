class Action:
    """Wykonanie akcji (4 rys.)."""

    def process(self, data):
        print(f"[Action] Executing: {data}")
        return {"executed": True}
