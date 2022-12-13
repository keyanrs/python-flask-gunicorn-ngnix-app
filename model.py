
class Model:
    def __init__(self):
        self.model = LRModel()

    def predict(self, input):
        return self.model.predict(input)

class LRModel:
    def predict(self, input):
        return '{"status":"Ok", "result":{"expected":1000}}'