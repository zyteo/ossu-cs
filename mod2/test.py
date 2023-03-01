an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

for character in word:
   if character in an_letters:
       print("Give me an " + character + "! " + character)
   else:
       print("Give me a  " + character + "! " + character)
print("What does that spell?")
for i in range(times):
    print(word, "!!!")