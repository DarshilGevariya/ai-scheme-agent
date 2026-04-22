import re

class Agent:
    def __init__(self, memory):
        self.memory = memory

    def execute(self, user_text):

        prompt = self.memory.current_prompt

        # 🔒 ONLY HANDLE CURRENT PROMPT
        if prompt == "age":
            match = re.search(r"\b(\d{1,3})\b", user_text)
            if match:
                self.memory.update("age", int(match.group(1)))
                return "kripya apni aay batayein, jaise 200000"
            else:
                return "kripya sirf number boliye, jaise 20"

        if prompt == "income":
            match = re.search(r"\b(\d{3,7})\b", user_text)
            if match:
                self.memory.update("income", int(match.group(1)))
                return "kripya apni category batayein, jaise samanya, obc"
            else:
                return "kripya sirf number boliye, jaise 200000"

        if prompt == "category":
            self.memory.update("category", user_text.lower())
            return "dhanyavaad, main yojana jaanch raha hoon"

        return None
