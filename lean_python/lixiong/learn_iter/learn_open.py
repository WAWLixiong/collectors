def myreadlines(f, newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096)
        if not chunk:
            yield buf
            break
        buf += chunk

with open('test.txt', 'r') as f:
    for line in myreadlines(f, "{|}"):
        print(line)
