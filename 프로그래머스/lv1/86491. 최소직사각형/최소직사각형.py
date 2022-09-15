def solution(sizes):
    x_size = []
    y_size = []

    for size in sizes:
        x_size.append(max(size))
        y_size.append(min(size))

    # print(x_size,y_size)
    answer = max(x_size) * max(y_size)
    return answer