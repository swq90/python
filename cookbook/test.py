*first, last = [1, 2, 3, 5]
print(sum(first), last)
line = 'nobody:*:-2:-2:unprivileged user:/var/empyt:/usr/bin/false'
uname, *field, homedir, sh = line.split(":")
print()