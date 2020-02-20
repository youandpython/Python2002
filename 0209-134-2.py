file = open('english_story.txt', 'r')
s = file.read()
s2 = ''
for st in s:
    if 'a' <= st <= 'z':
        s2 += st.upper()
    elif 'A' <= st <= 'Z':
        s2 += st.lower()
    else:
        s2 += st
file.close
file = open('english_story.txt', 'w')
file.write(s2)
file.close()
