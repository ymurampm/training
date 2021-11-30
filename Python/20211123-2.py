# Write a function that transforms a list of characters into a list of dictionaries, where:

# The keys are the characters themselves.
# The values are the ASCII codes of those characters.
# Examples
# to_dict(["a", "b", "c"]) ➞ [{"a": 97}, {"b": 98}, {"c": 99}]

# to_dict(["^"]) ➞ [{"^": 94}]

# to_dict([]) ➞ []

cl=["a", "b", "c"]
dic={}

def to_dict(charlist):
  for i in range(len(charlist)):
    dic[charlist[i]]=ord(charlist[i])
  return dic

print (to_dict(cl))
