import re

def course_code_check(code: str):
    if re.fullmatch(r"[A-Z]{3}[0-9]{3}", code): return True
    else: return False

## test cases
print(course_code_check("TEC001"))
print(course_code_check("Azns6969"))
