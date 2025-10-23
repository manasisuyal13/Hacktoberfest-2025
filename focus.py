"""
===========================================================
🚀 PROJECT: Focus Mode Activator – The Distraction Killer
AUTHOR: Manasi Suyal
LANGUAGE: Python
===========================================================
📘 ABOUT THIS CODE:
This script helps developers or students enter 'focus mode' 
instantly by automating common productivity actions such as:
🔇 Blocking distracting websites
⏱️ Setting a focus timer
💬 Showing motivational quotes

It’s perfect as a Hacktoberfest contribution — small, unique,
and actually useful in daily life.

FEATURES:
✅ Cross-platform (works on Windows/macOS/Linux)
✅ Blocks distracting websites (temporarily)
✅ Displays random motivational quote
✅ Built-in focus timer (Pomodoro style)
===========================================================
"""

import os
import time
import random
from datetime import datetime, timedelta

# Motivational quotes list
QUOTES = [
    "“Discipline equals freedom.” – Jocko Willink",
    "“The way to get started is to quit talking and begin doing.” – Walt Disney",
    "“You don’t have to be extreme, just consistent.”",
    "“Stay focused. It’s not supposed to be easy.”",
    "“The secret of getting ahead is getting started.” – Mark Twain",
    "“Do something today that your future self will thank you for.”"
]

# Common distracting websites
DISTRACTIONS = [
    "www.youtube.com", "www.instagram.com",
    "www.facebook.com", "www.twitter.com",
    "www.netflix.com"
]

HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts" if os.name == "nt" else "/etc/hosts"
REDIRECT_IP = "127.0.0.1"

def block_websites():
    """Block distracting websites temporarily."""
    print("🧱 Blocking distracting websites...")
    with open(HOSTS_PATH, "r+") as file:
        content = file.read()
        for site in DISTRACTIONS:
            if site not in content:
                file.write(f"{REDIRECT_IP} {site}\n")
    print("✅ Websites blocked successfully!")

def unblock_websites():
    """Unblock websites after focus session."""
    print("🪄 Unblocking websites...")
    with open(HOSTS_PATH, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(site in line for site in DISTRACTIONS):
                file.write(line)
        file.truncate()
    print("🌐 Websites unblocked!")

def show_quote():
    """Display a random motivational quote."""
    quote = random.choice(QUOTES)
    print("\n💡 MOTIVATION BOOSTER:")
    print(f"“{quote}”\n")

def focus_timer(minutes=25):
    """Start a Pomodoro-style focus timer."""
    print(f"⏳ Focus timer started for {minutes} minutes. No distractions!")
    end_time = datetime.now() + timedelta(minutes=minutes)
    while datetime.now() < end_time:
        remaining = (end_time - datetime.now()).seconds // 60
        print(f"🕒 Time left: {remaining} minutes", end="\r")
        time.sleep(60)
    print("\n✅ Focus session complete! You’ve earned a break!")

if __name__ == "__main__":
    print("🎯 Focus Mode Activator – by Manasi Suyal\n")
    show_quote()
    block_websites()

    try:
        focus_timer(0.2)  # Quick test: 0.2 = 12 seconds
    finally:
        unblock_websites()
        print("\n🚀 Great job staying focused! Now go conquer your goals 💪")
