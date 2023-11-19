_, b = map(int, input().split())
c = list(input().split())
def filtering(x):
    return x if int(x) < b else ''

print(' '.join(list(filter(filtering, c))))