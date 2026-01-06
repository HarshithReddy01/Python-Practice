users = ['john', 'bob', 'alex', 'alice', 'charlie', 'john',
         'alex', 'alice', 'john', 'alex']

logins = {}

for i in users:
    if i in logins:
        logins[i] += 1
    else:
        logins[i] = 1
for user, count in logins.items():
    print(f"{user:8} : {count} logins")