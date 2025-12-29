phrase = 'snooze alarms'
phrase1 = "alas, no more Z's"

phrase = phrase.lower()
phrase1 = phrase1.lower()

for x in phrase:
    if x.isalpha():
        if phrase.count(x) != phrase1.count(x):
            print('Not anagrams')
            break
    else:
        print("Anagrams")