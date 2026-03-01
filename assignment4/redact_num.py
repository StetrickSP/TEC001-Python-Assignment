import re

def redact_phone_num(text: str):
    return re.sub(r"\d{10}|\+84\d+", "[REDACTED]", text)

# test cases
print(redact_phone_num("0767139786"))
print(redact_phone_num("+84767139786"))
