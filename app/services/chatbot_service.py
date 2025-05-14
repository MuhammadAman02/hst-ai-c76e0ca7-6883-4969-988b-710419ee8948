class ChatbotService:
    def __init__(self):
        self.commands = {
            "hello": "Hello! How can I assist you with software development today?",
            "help": "I can answer basic questions about the Software Development Lifecycle (SDLC). Try asking about different phases or general SDLC concepts.",
            "bye": "Goodbye! Good luck with your software development journey!",
        }
        self.sdlc_qa = {
            "what is sdlc": "SDLC stands for Software Development Lifecycle. It's a process used by the software industry to design, develop, and test high-quality software.",
            "phases of sdlc": "The main phases of SDLC are: 1. Planning, 2. Analysis, 3. Design, 4. Implementation, 5. Testing, 6. Deployment, and 7. Maintenance.",
            "what is the planning phase": "The Planning phase is where project goals are determined and a high-level plan for the intended project is created.",
            "what is the analysis phase": "In the Analysis phase, we gather detailed requirements and analyze the feasibility of the project.",
            "what is the design phase": "The Design phase involves creating the software architecture and specifying software requirements.",
            "what is the implementation phase": "The Implementation phase is where the actual coding takes place based on the requirements and design documents.",
            "what is the testing phase": "In the Testing phase, the software is thoroughly tested to ensure it meets the specified requirements and is free of bugs.",
            "what is the deployment phase": "The Deployment phase involves releasing the software to the production environment for end-users.",
            "what is the maintenance phase": "The Maintenance phase includes ongoing support, updates, and improvements to the software after its deployment.",
            "why is sdlc important": "SDLC is important because it provides a structured approach to software development, ensuring better quality, control, and predictability in the development process.",
        }

    def process_message(self, message: str) -> str:
        message = message.lower().strip()
        if message in self.commands:
            return self.commands[message]
        elif message in self.sdlc_qa:
            return self.sdlc_qa[message]
        else:
            return "I'm not sure how to respond to that. Can you try rephrasing or ask for 'help'? You can also ask me about SDLC and its phases."

chatbot = ChatbotService()