def convert_emoji(messages):
    words = messages.split(' ')
    emoji = {
        ":)": "🙂",
        ":(": "😔",
        ":'(": "😭",
        ":3": "😗",
        ":')": "😂",
        ":D": "😃"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input("> ")
print(convert_emoji(message))
