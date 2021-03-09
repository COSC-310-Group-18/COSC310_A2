# THE NOVABOT
---

# Project Description

Nova is a chatbot that was designed to answer questions pertaining to astronomy. She knows the answers to several questions regarding galaxies, stars, our solar system, black holes and many other astronomical topics. As technology progresses, our society will likely look towards venturing further into the depth of space. Therefore, we aim to educate individuals on the basics of astronomy through this chatbot to prepare them for the future. 

# How does Nova work?

Nova was developed in python and uses natural language processing to understand and converse with the user. She takes the input from the user and cleans the sentences into a condensed and easily-readable format. She then compares the input to the questions she has in her questionbank then gives a response based on the similarity between the input and questionbank questions. All the questions and responses are found inside the corpus.txt file and may be expanded or changed as more astronomy questions are thought of. 

# Requirements

You will need to download and install NLTK and Spacy in your python IDE before using Nova. You will also need to download en_core_web_lg for Spacy. Once that is complete, you can run main.py and begin using Nova. 

# Branches

- **Main**: This section introduces the user, take their input and manages how the program executes 
- **Preprocessor**: This section is in charge of formatting the user input into a more readable format for the system
- **Processor**: This section takes the preprocessed data and tries to match it with its accurate response
- **Corpus**: Contains a compilation of questions and responses that Nova uses to converse with the user


