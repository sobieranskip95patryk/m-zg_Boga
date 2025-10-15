class Planner:
    def __init__(self):
        self.plan = []

    def create_plan(self, goal, context):
        """
        Create a plan based on the provided goal and context.
        """
        self.plan = self._generate_steps(goal, context)
        return self.plan

    def _generate_steps(self, goal, context):
        """
        Generate steps for the plan based on the goal and context.
        This is a placeholder for the actual planning logic.
        """
        steps = [
            f"Step 1: Define the goal - {goal}",
            f"Step 2: Analyze the context - {context}",
            "Step 3: Identify resources needed",
            "Step 4: Create a timeline",
            "Step 5: Execute the plan"
        ]
        return steps

    def get_plan(self):
        """
        Retrieve the current plan.
        """
        return self.plan

    def clear_plan(self):
        """
        Clear the current plan.
        """
        self.plan = []