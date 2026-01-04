import re

sent = "Long ago, when there was no written history, these islands were the home of millions of happy birds; the resort of a hundred times more millions of fishes, sea lions, and other creatures. Here lived innumerable creatures predestined from the creation of the world to lay up a store of wealth for the British farmer, and a store of quite another sort for an immaculate Republican government."
sent1 = "Long ago, when there was no written history, these islands were the home of millions of happy birds; the resort of a hundred times more millions of fishes, sea lions, and other creatures. Here lived innumerable creatures predestined from the creation of the world to lay up a store of wealth for the British farmer, and a store of quite another sort for an immaculate Republican government."

words1 = re.findall(r'\w+', sent.lower())
words2 = re.findall(r'\w+', sent1.lower())

wset1 = set(words1)
wset2 = set(words2)

common = wset1 & wset2
unique = wset1 | wset2

ratio = len(common) / len(unique)

print(f"Jaccard Similarity: {ratio:.2f}")