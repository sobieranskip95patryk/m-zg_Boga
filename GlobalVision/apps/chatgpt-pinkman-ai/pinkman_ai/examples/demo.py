from pinkman_ai.core import GaiaHub
from pinkman_ai.modules.extractor import Extractor
from pinkman_ai.modules.semantic import Semantic
from pinkman_ai.modules.recommender import Recommender
from pinkman_ai.modules.action import Action

if __name__ == "__main__":
    hub = GaiaHub()
    hub.register("extractor", Extractor())
    hub.register("semantic", Semantic())
    hub.register("recommender", Recommender())
    hub.register("action", Action())

    data = "Hello PinkMan AI"
    result = hub.run(data)
    print("Final result:", result)
