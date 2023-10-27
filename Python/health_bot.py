#pip install chatterbot chatterbot_corpus in bash
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


health_bot = ChatBot('HealthBot')
trainer = ChatterBotCorpusTrainer(health_bot)
trainer.train('chatterbot.corpus.english')

# Define a function to interact with the chatbot
def health_chat():
    print("HealthBot: Hello! I'm here to help you with health-related questions. You can type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("HealthBot: Goodbye!")
            break
        
        response = health_bot.get_response(user_input)
        print("HealthBot:", response)

if __name__ == "__main__":
    health_chat()
#Save this code to a Python file (e.g., health_chatbot.py) and run it using your terminal or preferred Python development environment. The chatbot will engage in conversations related to general health using pre-trained data from the ChatterBot corpus.
