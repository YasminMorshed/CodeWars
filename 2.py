import re
def to_camel_case(text):
    b = re.sub("([-_])\s*([a-z])", lambda p: p.group(0).upper(), text)
    c = b.replace("-", "")
    d = c.replace("_", "")
    return d