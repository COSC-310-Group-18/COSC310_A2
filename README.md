# NOVABOT, THE ROBOT ASTRONOMER
---

# Project Description

Nova is a chatbot that was designed to answer questions pertaining to astronomy. She knows the answers to several questions regarding galaxies, stars, our solar system, black holes and many other astronomical topics. As technology progresses, our society will likely look towards venturing further into the depth of space. Therefore, we aim to educate individuals on the basics of astronomy through this chatbot to prepare them for the future. 

# Software Development Life Cycle

We chose to use the incremental development life cycle. We chose this life cycle because we will be gathering a lot of user feedback while we are developing and this will likely lead to many changes to our requirements and design. Having this agile cycle will allow more freedom for us to make changes during development. We also want to utilize pair programming during our development which is a crucial factor in agile development. Our incremental development phases will include a project planning phase, a researching phase, a development ohase, an review phase and then a presentation phase. We aim to develop a basic chatbot in the first major increment then develop a GUI for the chatbot in the second major increment. 

# How does Nova work?

Nova was developed in python and uses natural language processing to understand and converse with the user. She takes the input from the user and cleans the sentences into a condensed and easily-readable format. She then compares the input to the questions she has in her questionbank then gives a response based on the similarity between the input and questionbank questions. All the questions and responses are found inside the corpus.txt file and may be expanded or changed as more astronomy questions are thought of. 

# Requirements

You will need to download and install NLTK and Spacy in your python IDE before using Nova. You will also need to download en_core_web_lg for Spacy. Once that is complete, you can run main.py and begin using Nova. 

# Branches

- **Main**: This section introduces the user, take their input and manages how the program executes 
- **Preprocessor**: This section is in charge of formatting the user input into a more readable format for the system
- **Processor**: This section takes the preprocessed data and tries to match it with its accurate response
- **Corpus**: Contains a compilation of questions and responses that Nova uses to converse with the user

# Capabilities

- Nova utilizes natural language processing and pattern matching effectively so the user input does not have to match the predefined questions exactly to get an accurate response
- Nova cover a wide range of topics in astronomy and astrophysics 
- Nova is easy to refactor and reuse since its structure is very basic. The corpus.txt can be modified to suit any topic of interest

# Limitations

- Nova can take a while to processes user input and output the correct responses since there is a lot of conversion and formatting to be done
- Nova is somewhat limitted to the predefined questions and responses in the corpus.txt. The file would have to be expanded in order for Nova to answer more questions
- Nova cannot recognize synonyms or similar phrases to the terms in the corpus.txt 

