# F-strings, also known as formatted string literals, were introduced in
# Python 3.6. They provide a way to embed expressions inside string literals,
# using curly braces {}. F-strings are prefixed with an f or F before the
# opening quote. They are faster and more readable than older string
# formatting methods like % formatting and str.format().
s
name="aqsa"
country="Pakistan"
print(f"Hey! My name is {{{name}}} , Im from {country} ")
# With single braces print aqsa ,double print {name} , three print
# {aqsa}
print("Hey!My name is {1} Im from {0}".format(country , name))