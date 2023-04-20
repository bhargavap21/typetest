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
num_sentences = st.sidebar.number_input("Select the number of sentences in the paragraph", min_value=1, max_value=50, value=10)

# Generate a list of random frequent sentences
@st.cache
def generate_sentences():
    freq_sentence_list = []
    while len(freq_sentence_list) < num_sentences:
        sentence = random.choice(list(nltk.corpus.brown.sents(categories='news')))
        sentence = ' '.join([w.lower() for w in sentence if w.lower() in freq_words])
        if len(sentence.split()) >= 10 and len(sentence.split()) <= 20:
            freq_sentence_list.append(sentence)
    return freq_sentence_list

freq_sentence_list = generate_sentences()

# Join the sentences into a paragraph separated by periods
paragraph = ' '.join(freq_sentence_list) + '.'

# Define the countdown timer
timer_duration = st.sidebar.number_input("Select the duration of the typing test (in seconds)", min_value=10, max_value=300, value=60)
timer_interval = 1  # seconds

# Define the start button
start_button = st.sidebar.button("Start Typing Test")

if start_button:
    # Display the paragraph to the user
    st.write(paragraph)

    # Start the timer
    start_time = time.time()
    end_time = start_time + timer_duration

    # Define the text input box
    text_input = st.empty()
    text_input_box = text_input.text_input("Enter the text you want to type")

    # Define the timer display
    timer_display = st.empty()
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        timer_text = f"Time remaining: {remaining_time} seconds"
        timer_display.text(timer_text)
        time.sleep(timer_interval)
    timer_display.text("Time's up!")

    # Disable text input once the timer runs out and get the typed text
    typed_text = text_input.value
    text_input_box = text_input.text_input("Time's up! You can't type anymore.", value=typed_text, disabled=True)
    
    # Calculate typing speed and accuracy
    st.write(typed_text)
    elapsed_time = end_time - start_time
    num_words = len(typed_text.split())
    typing_speed = num_words / (elapsed_time / 60)
    typed_words = typed_text.split()
    original_words = paragraph.split()
    num_correct = sum([1 for i in range(len(typed_words)) if typed_words[i] == original_words[i]])
    accuracy = num_correct / len(original_words)

    # Display typing speed and accuracy to the user
    st.write("Typing speed:", typing_speed, "words per minute")
    st.write("Accuracy:", accuracy * 100, "%")
