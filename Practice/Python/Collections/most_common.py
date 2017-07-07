from collections import Counter, defaultdict
if __name__ == '__main__':
    count = Counter(input())
    result = defaultdict(list)
    for w, c in count.items():
        result[c].append(w)
    out = [(w, c) for c in sorted(result.keys(), reverse=True) for w in sorted(result[c])]
    for r in out[:3]:
        print(*r)
