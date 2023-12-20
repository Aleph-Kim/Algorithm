_ = input()
song = list(map(ord, list(input())))

arr = list(range(97, 122))

for i in range(len(arr)):
    arr[i] = song.count(arr[i])
    
print(max(arr))