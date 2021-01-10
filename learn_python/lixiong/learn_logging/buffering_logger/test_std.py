import sys
ret = sys.stdout.write('hello world')
print()
print(ret)
ret = sys.stderr.write('error')
print()
print(ret)
