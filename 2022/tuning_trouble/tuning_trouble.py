def detect_marker(n):
    for i in range(0,len(signal)):
        chunk = signal[i:i+n]
        if len(set(chunk)) == n:
            return i+n

with open('input.txt','r') as f:
    signal = f.read().strip()

    print(f"First result: {detect_marker(4)}")
    print(f"Second result: {detect_marker(14)}")
