
with open('accounts.txt','r') as f:
    data = f.read()
    data = data.replace ('123', '234')
    print(data)
    with open('accounts.txt','w') as f:
        f.write(data)
        