import pyshorteners
s=pyshorteners.Shortener()
user_input=input('please type your copied url!!!  ')
print(s.dagd.short(str(user_input)))

