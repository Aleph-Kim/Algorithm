def solution(N, stages):
    answer = []
    limit_per = [0] * (N + 1)
    try_cnt = [0] * (N + 1)
    limit_cnt = [0] * (N + 1)

    for i in stages:
        limit_cnt[i-1] += 1
        for j in range(i):
            try_cnt[j] += 1

    limit_per = {i+1 : limit_cnt[i] / try_cnt[i] if limit_cnt[i] or try_cnt[i] else 0 for i in range(N)}

    return [i[0] for i in sorted(limit_per.items(), key=lambda item:item[1], reverse=True)]