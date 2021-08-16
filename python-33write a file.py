# text = "Yooooo\nThis is some text\nHave a great day\n"
text = "Have a nice day! See ya"
# with open('text.txt','w') as file: # Overwriteable
with open('text.txt', 'a') as file: # Fix and just add
    file.write(text)