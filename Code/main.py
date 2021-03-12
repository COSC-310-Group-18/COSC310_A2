import Preprocessor
import Processor

questions, responses = Preprocessor.load_corpus()

print("Booting Up...")
question_list = Processor.vectorizer(questions)
print("The Chat Bot has loaded. Type 'goodbye' to exit")
print("Hello. My name is Nova, the astronomy Chat Bot. Pleased to meet you")

while True:  # The Chat Bot will run until 'goodbye' is inputted
    user_input = input("Input: ").lower()
    if user_input.lower() == "goodbye":
        print("Nova: See you soon!")
        quit()
    else:
        print("Nova:",end=' ')
        Processor.process(user_input, question_list, responses)
