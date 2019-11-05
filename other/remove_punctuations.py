""" Different method of Removing Punctuation from words """

import time
import re
import string

PATTERN = r".*?[\W_]+"

def enum_method(data):
    """ Using enumerate method """

    start = time.time()
    for i, word in enumerate(data):
        data[i] = "".join((char for char in word if not re.search(PATTERN, char)))
    data = [word for word in data if word]
    return data, time.time()-start


def loop(data):
    """ Using loops and string function """

    start = time.time()
    for i in range(len(data)):
        if not data[i].isalpha():
            for j in range(len(data[i])):
                if data[i][j] not in string.ascii_letters:
                    data[i] = data[i].replace(data[i][j], "")
                    break
    data = [word for word in data if word]
    return data, time.time()-start


def regex(data):
    """ Using re.sub """

    start = time.time()
    new_data = [re.sub(r"[\W]", "", i) for i in data]
    new_data = [word for word in new_data if word]
    return new_data, time.time()-start


def main():
    """ main army """
    words_data = ["Co__rrect", "i", "lo_ved", "th.a.t.", "pa-r--t", 'On)e', 'ha_s', 't%%o', 'op)ti(mi_zed']

    print(enum_method(words_data))
    print(loop(words_data))
    print(regex(words_data))

main()
