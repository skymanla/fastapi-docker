import re

korean = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')


def del_korean(s: str):
    new_s = re.sub(korean, "", s)
    new_s = new_s.replace(" ", "")
    return new_s
