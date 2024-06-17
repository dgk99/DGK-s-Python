# wrap_in_tag(tag, contect)

def wrap_in_tag(arg_a, arg_b):
    result = (f"<{arg_a}>{arg_b}</{arg_a}>")
    return result

print(wrap_in_tag('p', 'hello'))
print(wrap_in_tag('b', 'world'))