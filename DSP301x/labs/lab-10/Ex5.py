import re

str = """Au pays parfume que le soleil caresse,
J'ai connu, sous un dais d'arbres tout empourpres
Et de palmiers d'ou pleut sur les yeux la paresse,
Une dame creole aux charmes ignores."""

# Type your answer here.

regex = r"\b[A-Za-z0-9]{8,}\b"
emails = re.findall(regex, str)


print(emails)
