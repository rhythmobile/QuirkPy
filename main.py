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
        "🎨 Welcome to QuirkPy Your creativity is welcome here!",
        "🚀 Ready to add some chaos? Fork and contribute anything!",
        "🌟 This project grows through community magic - add your touch!",
        "🤝 All contributions welcome: features, fixes, jokes, or nonsense!",
        "🎉 The chaos continues with YOU! What will you add?"
    ]
    return random.choice(welcome_messages)


def main():
    """Main function that runs the show"""
    import sys
    
    # Check for AI demo flag
    if "--ai-demo" in sys.argv:
        showcase_all_features()
        return
    
    # Classic chaos mode
    print("=" * 60)
    print(hello_chaotic())
    print("\n" + contribution_welcome())
    print("=" * 60)
    
    # Show AI integration hint
    if random.random() < 0.3:  # 30% chance
        print("\n🧠 NEW: Try --ai-demo flag for AI features! 🧠")
    
    # Fun easter egg for contributors
    if random.random() < 0.15:  # 15% chance
        print("\n🥚 EASTER EGG! Add your own chaos below this line! 🥚")


def hello_bangla_ai():
    """New AI-powered Bangla greeting generator"""
    try:
        from ml_modules.chaos_engine import BanglaChaosGenerator
        generator = BanglaChaosGenerator()
        meme = generator.generate_meme_text("welcome")
        return f"🇧🇩 {meme['top']} {meme['bottom']}"
    except ImportError:
        return "🧠 Install AI features: pip install -r requirements.txt"

def showcase_all_features():
    """Show both classic chaos and new AI features"""
    print("\n🎪 QUIRKPY FEATURE SHOWCASE 🎪")
    print("=" * 50)
    
    # Classic chaos
    print("1️⃣ Classic Chaos:")
    print(hello_chaotic())
    
    # New AI features
    print("\n2️⃣ AI/ML Evolution:")
    print(hello_bangla_ai())
    
    # Quick demo
    print("\n3️⃣ Quick AI Demo:")
    try:
        from ml_modules.chaos_engine import test_bangla_chaos
        print("✅ Bangla Chaos Engine: Ready!")
        print("   Run: python ml_modules/chaos_engine.py")
    except ImportError:
        print("⚠️  Install dependencies first: pip install -r requirements.txt")

# AI/ML EVOLUTION ZONE 🧠🇧🇩
#
# 🆕 QUIRKPY 2.0 - NOW WITH AI!
#
# 🎯 NEW COMMANDS:
#   python main.py --ai-demo      # Full AI showcase
#   python ml_modules/chaos_engine.py  # Bangla text generation
#   python -c "from ml_modules.chaos_engine import test_bangla_chaos; test_bangla_chaos()"
#
# 🌏 BANGLADESH AI REVOLUTION:
#   ✅ Generate Bangla text datasets
#   ✅ Create AI-powered memes
#   ✅ Build ML models for Bangla language
#   ✅ Community-driven AI research
#
# 🤝 CONTRIBUTION PATHS:
#   1. Add Bangla words to chaos_engine.py
#   2. Create new ML modules in ml_modules/
#   3. Build Bangla NLP tools
#   4. Share datasets with community
#   5. Train meme generation models


if __name__ == "__main__":
    main()