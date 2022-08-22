import pyperclip as pc

def main():
    unicode = {
        "new": "🗼",
        "update": "✨",
        "fix": "🔨",
        "patch": "🤝",
        "merge": "⚡",
        "security": "🔒",
        "bug": "🐛",
        "label": "🏷️",
        "legal": "📝",
        "docs": "📚",
        "test": "🔬",
        "build": "🔧",
        "deploy": "🚀",
        "release": "🎉",
        "restructure": "🔥",
        "beautify": "🔮",
        "package": "📦",
        "license": "🔑",
        "minor_changes": "📍",
    }

    print("\n")
    print("Precomit Dictionary")
    print("----------------")

    for key, value in unicode.items():
        print(key, ":", value)
    print("\n")

    print("Enter the name of the emoji you want to copy to the clipboard")
    print("Enter 'quit' to exit the program")
    print("\n")

    while True:
        emoji = input("Emoji: ")
        if emoji == "quit":
            break
        elif emoji in unicode:
            pc.copy(unicode[emoji])
            print("Copied emoji", unicode[emoji], "to clipboard")
        else:
            print("Emoji not found")



if __name__ == "__main__":
	main()
