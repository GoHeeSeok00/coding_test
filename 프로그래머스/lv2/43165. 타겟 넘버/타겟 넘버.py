def solution(numbers, target):
    answer = [0]

    def target_of_case(numbers, i, v):
        if i == len(numbers):
            if v == target:
                answer[0] += 1
            return

        target_of_case(numbers, i + 1, v + numbers[i])
        target_of_case(numbers, i + 1, v - numbers[i])

    target_of_case(numbers, 0, 0)
    return answer[0]
