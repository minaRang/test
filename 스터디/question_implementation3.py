#문자열 압축
def solution(s):
    l = len(s)
    result = [l]

    for size in range(1, l//2):
        short = ""
        splited = [s[i:i+size] for i in range(0, l, size)]
        count = 1
        for j in range(1, len(splited)):
            before, now = splited[j-1], splited[j]
            if before == now:
                count += 1
            else:
                if count > 1:
                    short += (str(count) + before)
                 else:
                    short+=before
                count = 1
        if count>1:
            short += (str(count) + splited[-1])
        else:
            short+=splited[-1]
        result.append(len(short))

    return min(result)
