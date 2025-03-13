import time
from pynput import keyboard

morse_code = ""
decoded_text = ""
press_start_time = None

# Morse Dictionary
morse_dict = {
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "a": ".-", "b": "-...",
    "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
    "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
    "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..",
    "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"
}


reverse_morse_dict = {v: k for k, v in morse_dict.items()}  # to convert the morse to text got this part from chatgbt
# to simplify what i did earlier

print(f"Welcome to my Morse Code converter!\n"
      f" Press 'a' quickly (less than 0.5s) → . (dot)\n"
      f" Press 'a' long (0.6s to 2s) → - (dash)\n"
      f" Press 's' → Converts the Morse code to Text\n"
      f" Press 'Backspace' → Resets input\n"
      f" Press 'ESC' → Exit program\n")


def on_press(key):
    """Detects when 'a' is pressed and starts the timer."""
    global press_start_time

    try:
        key_name = key.char
    except AttributeError:
        key_name = key

    if key_name == 'a':
        press_start_time = time.time()


def on_release(key):
    global press_start_time, morse_code, decoded_text

    try:
        key_name = key.char
    except AttributeError:
        key_name = key

    if key_name == 'a' and press_start_time is not None:
        press_duration = time.time() - press_start_time

        if press_duration < 0.3:  # Fast tap
            morse_code += '.'
        if press_duration >= 0.3:  # Longer press
            morse_code += '-'

        print(f"Morse Code: {morse_code}")

        press_start_time = None  # Reset press start time

    elif key_name == 's':  # Convert Morse to text
        if morse_code in reverse_morse_dict:
            decoded_text += reverse_morse_dict[morse_code]  # Decode
            print(f"Decoded Text: {decoded_text}")
        else:
            print("Invalid Morse Code!")  # Handle incorrect inputs

        morse_code = ""  # Reset Morse code after conversion

    elif key_name == keyboard.Key.backspace:  # Reset input
        morse_code = ""
        decoded_text = ""
        print("Morse Code reset!")

    elif key_name == keyboard.Key.esc: # exit
        print(f"Final Decoded Message: {decoded_text}")
        print("Exiting program...")
        return False  # To Stop listener


# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()