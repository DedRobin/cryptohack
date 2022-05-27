def decode(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = [alphabet[(alphabet.index(letter) + key) % 26] if letter != " " else " " for letter in string.lower()]
    return "".join(string)

if __name__ == "__main__":
    for x in range(1, 27):
        print(decode("XBJFW QZLLFLJ QZCZWD FZLZXY", x))
