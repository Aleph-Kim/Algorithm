s = list(input())

i = 0
for c in s:
    match c:
        case 'A' | 'B' | 'C':
            i += 3
        case 'D' | 'E' | 'F':
            i += 4
        case 'G' | 'H' | 'I':
            i += 5
        case 'J' | 'K' | 'L':
            i += 6
        case 'M' | 'N' | 'O':
            i += 7
        case 'P' | 'Q' | 'R' | 'S':
            i += 8
        case 'T' | 'U' | 'V':
            i += 9
        case 'W' | 'X' | 'Y' | 'Z':
            i += 10
print(i)