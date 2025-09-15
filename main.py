#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QuirkPy - A Community-Driven Python Experiment 🌀

This is your canvas for chaos! Add anything you want:
- New greeting styles
- Random features
- Silly functions
- Useful tools
- Complete nonsense

The only rule: Make it fun! 🎉
"""

import random
import time


def hello_ascii_art():
    """Print Hello World in glorious ASCII art"""
    ascii_styles = [
        """
    ██╗  ██╗ ██████╗ ███╗   ███╗     ██████╗ ██████╗ ███╗   ███╗
    ██║  ██║██╔═══██╗████╗ ████║    ██╔════╝██╔═══██╗████╗ ████║
    ███████║██║   ██║██╔████╔██║    ██║     ██║   ██║██╔████╔██║
    ██╔══██║██║   ██║██║╚██╔╝██║    ██║     ██║   ██║██║╚██╔╝██║
    ██║  ██║╚██████╔╝██║ ╚═╝ ██║    ╚██████╗╚██████╔╝██║ ╚═╝ ██║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝
        """,
        """
  _   _      _ _         _        _____ _           
 | | | |    | | |       | |      / ____| |          
 | |_| | ___| | | ___   | |     | |  __| | _____  __
 |  _  |/ _ \ | |/ _ \  | |     | | |_ | |/ _ \ \/ /
 | | | |  __/ | | (_) | | |____ | |__| | |  __/>  < 
 |_| |_|\___|_|_|\___/  |______|\_____|_|\___/_/\_\\
        """,
        """
    ╔╗ ╔═╗╔╗╔╔═╗╔╦╗╔═╗╔╗╔
    ╠╩╗╠╣ ║║║║╣  ║ ║ ║║║║
    ╚═╝╚  ╝╚╝╚═╝ ╩ ╚═╝╝╚╝
    ╔═╗ ╦ ╦╔═╗╔╗╔╔╦╗╔═╗╦═╗
    ║═╬╗║ ║╠╣ ║║║ ║║╠╣ ╠╦╝
    ╚═╝╚╚═╝╚  ╝╚╝═╩╝╚═╝╩╚═
        """
    ]
    return random.choice(ascii_styles)


def hello_reversed_text():
    """Print Hello World backwards because normal is boring"""
    reversed_styles = [
        "dlroW ,olleH 🙃",
        "¿dlroW olleH",
        "H€llø Wørld"[::-1],  # Actually reversed
        "Hello World"[::-1].upper(),
        "dlrow ,olleh" * 2
    ]
    return random.choice(reversed_styles)


def hello_emoji_party():
    """Hello World but make it an emoji celebration"""
    emoji_combos = [
        "👋🌍✨ Hello World! ✨🌍👋",
        "🤗🌎🎉 HELLO WORLD! 🎉🌎🤗",
        "🚀🌌 Hello from space world! 👽🪐",
        "🌈🎊 Hellooo beautiful world! 🎊🌈",
        "👑🗺️ Hello World, you're royalty! 👑🗺️",
        "🦄🌟 Magical Hello World! 🌟🦄"
    ]
    return random.choice(emoji_combos)


def hello_chaotic():
    """The main chaos orchestrator - picks a random greeting style"""
    greeting_functions = [
        hello_ascii_art,
        hello_reversed_text,
        hello_emoji_party
    ]
    
    # Add some dramatic pause for effect
    time.sleep(random.uniform(0.1, 0.3))
    
    chosen_greeting = random.choice(greeting_functions)()
    return chosen_greeting


def contribution_welcome():
    """Print a welcome message for potential contributors"""
    welcome_messages = [
        "🎨 Welcome to ChaosPy! Your creativity is welcome here!",
        "🚀 Ready to add some chaos? Fork and contribute anything!",
        "🌟 This project grows through community magic - add your touch!",
        "🤝 All contributions welcome: features, fixes, jokes, or nonsense!",
        "🎉 The chaos continues with YOU! What will you add?"
    ]
    return random.choice(welcome_messages)


def main():
    """Main function that runs the show"""
    print("=" * 60)
    print(hello_chaotic())
    print("\n" + contribution_welcome())
    print("=" * 60)
    
    # Fun easter egg for contributors
    if random.random() < 0.15:  # 15% chance
        print("\n🥚 EASTER EGG! Add your own chaos below this line! 🥚")


# CONTRIBUTION ZONE 🎯
# 
# BEFORE YOU ADD: Read CONTRIBUTING.md for guidelines!
# 
# ✅ GOOD CONTRIBUTIONS:
# - def hello_bangla_rap(): return "বাংলা র‍্যাপে হ্যালো!"
# - def hello_with_time(): return f"Hello World! It's {datetime.now().strftime('%H:%M')}"
# - def hello_story(): return "Once upon a time... Hello World!"
# 
# ❌ AVOID:
# - def hello_basic(): return "Hello World"  # Too simple!
# - def hello_copy(): return existing_function()  # Duplicate!
# 
# Make it UNIQUE, CREATIVE, and add VALUE!


if __name__ == "__main__":
    main()