import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Ask user for details
name = input("What is your name? ")
age = input("How old are you? ")
color = input("What is your favorite color? ")

# Create greeting message
greeting = f"Hello {name}! Wow, {age} is a great age to be! And {color} is such a beautiful color!"

# Print and speak the greeting
print("\n🎯 Your Personalized Greeting:")
print(greeting)

engine.say(greeting)   # Queue the message
engine.runAndWait()    # Play the message

from muthu_footer import add_footer

# ... your app code

add_footer()