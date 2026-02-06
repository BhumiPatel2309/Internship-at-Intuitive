from tools import load_document

class ReActDocumentAgent:
    def __init__(self):
        self.state = {}
        self.finished = False
        self.max_steps = 5   
        self.step_count = 0

    def reason(self, user_input: str):
        """
        Decide next step based on STATE
        """
        if "document" in self.state:
            return {
                "thought": "I already have the document. I can answer now.",
                "action": None
            }

        return {
            "thought": "I need to load the document before answering.",
            "action": "load_document",
            "action_input": {"doc_id": "doc_1"}
        }

    def act(self, action_name: str, action_input: dict):
        if action_name == "load_document":
            return load_document(**action_input)
        raise ValueError("Unknown action")

    def observe(self, observation):
        self.state["document"] = observation

    def respond(self):
        document = self.state["document"]

        self.finished = True

        return (
            "Microservices offer scalability, independent deployment, "
            "fault isolation, and faster development cycles."
        )

    def run(self, user_input: str):
        while not self.finished and self.step_count < self.max_steps:
            self.step_count += 1

            step = self.reason(user_input)
            print(f"\nThought: {step['thought']}")

            if step["action"] is None:
                return self.respond()

            print(f"Action: {step['action']}")
            observation = self.act(step["action"], step["action_input"])
            print(f"Observation: {observation.strip()}")
            self.observe(observation)

        raise RuntimeError("ReAct agent exceeded max steps")
