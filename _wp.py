import sys, os
target = sys.argv[1]
content = sys.stdin.read()
os.makedirs(os.path.dirname(target), exist_ok=True)
with open(target, "w", encoding="utf-8") as f:
    f.write(content)
print("OK:", os.path.getsize(target), "bytes")
