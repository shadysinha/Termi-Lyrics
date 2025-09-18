
# import sys
# from time import sleep
# import time

# def printLyrics():
#     # ANSI color and style codes
#     BOLD_GREEN = "\033[1m\033[92m"
#     BOLD_CYAN = "\033[1m\033[96m"
#     BOLD_YELLOW = "\033[1m\033[93m"
#     BOLD_PURPLE = "\033[1m\033[95m"
#     BOLD_MAGENTA = "\033[1m\033[95m"
#     BOLD_RED = "\033[1m\033[91m"
#     RESET = "\033[0m" 

#     lines = [
#         ("Uh, summa-lumma, dooma-lumma, you assumin' I'm a human", BOLD_GREEN, 0.04),
#         ("What I gotta do to get it through to you? I'm superhuman", BOLD_CYAN, 0.035),
#         ("Innovative and I'm made of rubber so that anythin'", BOLD_CYAN, 0.02),
#         ("you say is ricochetin' off of me, and it'll glue to you and", BOLD_CYAN, 0.04),
#         ("I'm devastatin', more than ever demonstratin", BOLD_YELLOW, 0.03),
#         ("how to give a mother- audience a feelin' like it's levitatin'", BOLD_YELLOW, 0.03),
#         ("Never fadin' and I know the haters are forever waitin", BOLD_PURPLE, 0.03),
#         ("for the day that they can say I fell off, they'll be celebratin'", BOLD_PURPLE, 0.02),
#         ("'Cause I know the way to get 'em motivated", BOLD_MAGENTA, 0.025),
#         ("I make elevatin' music, you make elevator music", BOLD_MAGENTA, 0.025),
#         ('"Oh, he\'s too mainstream"', BOLD_RED, 0.03),
#         ("well, that\'s what they do when they get jealous, they confuse it'", BOLD_RED, 0.03)
#     ]

#     for text, color, delay in lines:
#         sys.stdout.write(color) 
#         for char in text:
#             sys.stdout.write(char)
#             sys.stdout.flush()
#             sleep(delay)
#         sys.stdout.write(RESET) 
#         sys.stdout.write("\n")
#         sys.stdout.flush()

# if __name__ == "__main__":
#     printLyrics()



from rich.console import Console
from rich.style import Style
import time
import sys

def printLyrics():
    # Initialize Rich console
    console = Console()

    
    bold_green = Style(color="green", bold=True)
    bold_cyan = Style(color="cyan", bold=True)
    bold_yellow = Style(color="yellow", bold=True)
    bold_purple = Style(color="purple", bold=True)
    bold_magenta = Style(color="magenta", bold=True)
    bold_red = Style(color="red", bold=True)
    
    
    lines = [
        ("Uh, summa-lumma, dooma-lumma, you assumin' I'm a human", bold_green, 0.04),
        ("What I gotta do to get it through to you? I'm superhuman", bold_cyan, 0.035),
        ("Innovative and I'm made of rubber so that anythin'", bold_cyan, 0.02),
        ("you say is ricochetin' off of me, and it'll glue to you and", bold_cyan, 0.04),
        ("I'm devastatin', more than ever demonstratin", bold_yellow, 0.03),
        ("how to give a mother- audience a feelin' like it's levitatin'", bold_yellow, 0.03),
        ("Never fadin' and I know the haters are forever waitin", bold_purple, 0.03),
        ("for the day that they can say I fell off, they'll be celebratin'", bold_purple, 0.02),
        ("'Cause I know the way to get 'em motivated", bold_magenta, 0.025),
        ("I make elevatin' music, you make elevator music", bold_magenta, 0.025),
        ('"Oh, he\'s too mainstream"', bold_red, 0.03),
        ("well, that\'s what they do when they get jealous, they confuse it'", bold_red, 0.03)
    ]

    for text, style, delay in lines:
        for char in text:
            console.print(char, end="", style=style)
            sys.stdout.flush()
            time.sleep(delay)
        console.print("") 

if __name__ == "__main__":
    printLyrics()