import re

pattern = r"[a-z]+nline"  # [] fo grp , r for raw string
text = '''WI-kee) is a form of online hypertext publication that is collaboratively edited and managed by
  its own audience directly through a web browser. A typical wiki contains multiple pages for the 
  subjects or scope of the project, and could pnline be either open to the public or limited to use within 
  an organization for maintaining its internal knowledge base.'''

# match = re.search(pattern , text)
# print(match)
# for print more than one match
matches = re.finditer(pattern , text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])