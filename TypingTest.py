import streamlit as st
import time
import random
import nltk

nltk.download('punkt')
nltk.download('words')
nltk.download('brown')
words = set(nltk.corpus.words.words())
freq_words = set([w.lower() for w in nltk.corpus.brown.words(categories='news') if w.lower() in words])

# Define the number of sentences in the paragraph
num_sentences = 10

# Generate a list of random frequent sentences
freq_sentence_list = []
while len(freq_sentence_list) < num_sentences:
    sentence = random.choice(list(nltk.corpus.brown.sents(categories='news')))
    sentence = ' '.join([w.lower() for w in sentence if w.lower() in freq_words])
    if len(sentence.split()) >= 10 and len(sentence.split()) <= 20:
        freq_sentence_list.append(sentence)

# Join the sentences into a paragraph separated by periods
paragraph = ' '.join(freq_sentence_list) + '.'

# Define the countdown timer
timer_duration = 60  # seconds
timer_interval = 1  # seconds

# Define the start button
start_button = st.button("Start Typing Test")

if start_button:
    # Display the paragraph to the user
    st.write(paragraph)

    # Start the timer
    start_time = time.time()
    end_time = start_time + timer_duration

    # Define the text input box
    text = st.text_input("Enter the text you want to type")

    # Define the timer display
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        timer_text = f"Time remaining: {remaining_time} seconds"
        st.write(timer_text)
        time.sleep(timer_interval)
    st.write("Time's up!")

    # Disable text input once the timer runs out
    st.text_input("Time's up! You can't type anymore.", value="", disabled=True)

    # Calculate typing speed and accuracy
    elapsed_time = end_time - start_time
    num_words = len(text.split())
    typing_speed = num_words / (elapsed_time / 60)
    typed_words = text.split()
    original_words = paragraph.split()
    num_correct = sum([1 for i in range(len(typed_words)) if typed_words[i] == original_words[i]])
    accuracy = num_correct / len(original_words)

    # Display typing speed and accuracy to the user
    st.write("Typing speed:", typing_speed, "words per minute")
    st.write("Accuracy:", accuracy * 100, "%")
