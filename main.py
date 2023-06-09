
import tkinter as tk
import time
import random

# Define the list of text samples
text_samples = [
    "The quick brown fox jumps over the lazy dog.",
    "The five boxing wizards jump quickly.",
    "How vexingly quick daft zebras jump!",
    "Jackdaws love my big sphinx of quartz.",
    "Pack my box with five dozen liquor jugs.",
    "Mr. Jock, TV quiz Ph.D., bags few lynx.",
    "Sphinx of black quartz, judge my vow.",
    "The quick onyx goblin jumps over the lazy dwarf.",
    "Waltz, nymph, for quick jigs vex Bud.",
    "Bawds jog, flick quartz, vex nymphs."
]

# Define the high scores dictionary
high_scores = {}

# Load the high scores from a file
def load_high_scores():
    global high_scores
    try:
        with open("high_scores.txt", "r") as f:
            high_scores = eval(f.read())
    except:
        pass

# Save the high scores to a file
def save_high_scores():
    with open("high_scores.txt", "w") as f:
        f.write(str(high_scores))

# Initialize the tkinter app
app = tk.Tk()
app.title("Typing Trainer")

# Define the GUI elements
instruction_label = tk.Label(app, text="Type the following text:")
instruction_label.pack()

text_label = tk.Label(app, text="", font=("Arial", 14))
text_label.pack()

input_textbox = tk.Entry(app, font=("Arial", 14))
input_textbox.pack()

result_label = tk.Label(app, text="")
result_label.pack()

high_scores_label = tk.Label(app, text="")
high_scores_label.pack()

# Define the function to generate a random text sample
def generate_text_sample():
    global current_text_sample
    current_text_sample = random.choice(text_samples)
    text_label.config(text=current_text_sample)

# Define the function to calculate the typing speed
def calculate_speed():
    input_text = input_textbox.get()
    words_typed = len(input_text.split())
    time_taken = time.time() - start_time
    speed = int(words_typed / (time_taken / 60))
    result_label.config(text="Your typing speed is " + str(speed) + " words per minute.")
    if speed > high_scores.get(current_text_sample, 0):
        high_scores[current_text_sample] = speed
        high_scores_label.config(text="New high score for \"" + current_text_sample + "\": " + str(speed))
        save_high_scores()

# Define the function to start the typing test
def start_typing_test():
    generate_text_sample()
    input_textbox.delete(0, tk.END)
    input_textbox.focus()
    start_button.config(state=tk.DISABLED)
    calculate_button.config(state=tk.NORMAL)
    global start_time
    start_time = time.time()

# Define the function to reset the typing trainer
def reset_typing_trainer():
    high_scores.clear()
    save_high_scores()
    high_scores_label.config(text="")
    generate_text_sample()

# Add a "Start Typing Test" button to start the typing test
start_button = tk.Button(app, text="Start Typing Test", command=start_typing_test)
start_button.pack()

# Add a "Calculate Speed" button to calculate the typing speed
calculate_button = tk.Button(app, text="Calculate Speed", command=calculate_speed, state=tk.DISABLED)
calculate_button.pack()

# Add a "Reset Typing Trainer" button to reset the typing trainer
reset_button = tk.Button(app, text="Reset Typing Trainer", command=reset_typing_trainer)
reset_button.pack()

# Load the high scores
load_high_scores()

# Start the tkinter event loop
app.mainloop()
