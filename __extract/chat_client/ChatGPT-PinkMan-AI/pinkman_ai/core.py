class GaiaHub:
    """Centralny koordynator systemu PinkMan AI."""

    def __init__(self):
        self.state = {}
        self.modules = {}

    def register(self, name, module):
        self.modules[name] = module

    def run(self, input_data):
        """Prosty cykl danych przez moduły."""
        output = input_data
        for name, module in self.modules.items():
            if hasattr(module, "process"):
                output = module.process(output)
        return output
