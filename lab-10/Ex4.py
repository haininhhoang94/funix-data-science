import re

str = (
    "The advancements in biomarine studies franky@google.com, with the investments"
    " necessary and Davos sinatra123@yahoo.com Then The New Yorker article on wind"
    " farms..."
)
# Type your answer here.

regex = r"\b[A-Za-z0-9._%+-]+@"
emails = re.findall(regex, str)
emails_dup = []

for email in emails:
    a = email.split('@')
    emails_dup.append(a[0])

emails = emails_dup
print(emails)
