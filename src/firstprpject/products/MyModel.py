

class MyModel:
    def __init__(self, model,):
        self.instance = None

    def getInstance(self):
        if not self.instance:
            self.instance = MyModel()

        return self.instance

    def predict(self, features: dict):
        pass


