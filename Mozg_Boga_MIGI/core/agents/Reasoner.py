class Reasoner:
    def __init__(self):
        self.knowledge_base = []

    def add_knowledge(self, knowledge):
        self.knowledge_base.append(knowledge)

    def reason(self, query):
        # Implement logical reasoning based on the knowledge base
        results = []
        for knowledge in self.knowledge_base:
            if self.evaluate_query(knowledge, query):
                results.append(knowledge)
        return results

    def evaluate_query(self, knowledge, query):
        # Placeholder for query evaluation logic
        return query in knowledge

    def clear_knowledge(self):
        self.knowledge_base.clear()