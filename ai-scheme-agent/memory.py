class Memory:
    def __init__(self):
        self.data = {
            "age": None,
            "income": None,
            "category": None
        }
        self.current_prompt = "age"

    def update(self, field, value):
        self.data[field] = value

        if field == "age":
            self.current_prompt = "income"
        elif field == "income":
            self.current_prompt = "category"
        elif field == "category":
            self.current_prompt = None

    def is_complete(self):
        return all(self.data.values())
