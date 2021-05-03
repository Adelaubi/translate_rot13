import string


def trans_rot13(word):
    if type(word) != string:
        rot13_translate = str.maketrans("NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
                                        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")
        return str.translate(word, rot13_translate)
    else:
        return "Error incorrect type of var"


if __name__ == '__main__':
    print(trans_rot13("Pbatengf! Wr erivraf iref gbv encvqrzrag !"))
