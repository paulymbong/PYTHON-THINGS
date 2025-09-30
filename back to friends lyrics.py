import time
import sys

lyrics = [
    ("How can we go back to being friends", 0.1, 1.0),
    ("When we just shared a bed?", 0.1, 2.3),
    ("How can u look at me and pretend", 0.1, 2.0),
    ("Im someone you've never met?", 0.1, 2.9),
    ("How can we go back to being friends", 0.1, 1.0),
    ("When we just shared a bed?", 0.1, 2.6),
    ("How can u look at me and pretend", 0.1, 2.6),
    ("Im someone you've never met?", 0.1, 2.9),
]

def type_out(text, char_delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def play_lyrics(lyrics):
    for line, char_delay, line_delay in lyrics: 
        type_out(line, char_delay)
        time.sleep(line_delay)

if __name__ == "__main__":
    print("Now playing: back to friends\n")
    play_lyrics(lyrics)
