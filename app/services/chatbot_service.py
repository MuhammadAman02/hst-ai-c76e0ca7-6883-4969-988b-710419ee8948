class ChatbotService:
    def __init__(self):
        self.commands = {
            "hello": "Hello! How can I assist you today?",
            "help": "I can respond to 'hello', 'help', and 'bye'. For anything else, I'll try my best to assist you.",
            "bye": "Goodbye! Have a great day!",
        }

    def process_message(self, message: str) -> str:
        message = message.lower().strip()
        return self.commands.get(message, "I'm not sure how to respond to that. Can you try rephrasing or ask for 'help'?")

chatbot = ChatbotService()