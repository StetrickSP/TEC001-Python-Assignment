import re

def color_code_check(code: str):
    return bool(re.fullmatch(r"#[0-9A-Fa-f]{6}", code))

# test cases
print(color_code_check("#FF0000"))
print(color_code_check("#99999Z"))
