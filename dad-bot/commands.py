import re

PATTERN = re.compile(r"\b[Ii](?:['’]\s*|\s+)?(?:[Aa]\s+)?[Mm]\b")

def parse_dad_joke_trigger(message: str) -> str | None:
    match = PATTERN.search(message)
    if not match:
        return None

    target = message[match.end():].strip()
    if not target:
        return None

    return target
    
def clear(message):
    amount = int(message[len("!clear "):] )
    amount += 1
    return amount