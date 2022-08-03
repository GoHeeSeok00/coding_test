def solution(name):
    # 탐욕법은 규칙을 세팅하는게 중요
    # - 알파벳
    # 1. 알파벳 순서를 쉽게 표현하기 위해 아스키코드 사용
    # 2. N(110 | 13)을 기준으로 A에서 B로 이동할지 Z로 이동할지 결정
    #
    # - 커서
    # 1. A인 문자열은 커서 이동을 할 필요가 없다.(기본세팅값 A)
    # 2. 다음 문자열이 A라면 이동경로 변수A + 1 (A가 아닌 문자열이 나올 때 까지)
    # 3. A가 아닌 문자열이 나오면 맨 마지막 문자열 부터 A인지 확인 (이동경로 변수 B + 1)
    # 4. 마지막부터 검사했을 때 A가 아닌 문자열을 만나면 이동경로 A와 B를 비교 (B의 경우 현재 인덱스 거리만큼 추가)
    # 5. 경로가 작은쪽으로 이동결정
    # 6. A의 경우 B의 경우 Case 확인
    first = True
    check_name = []
    for word in name:
        if word == "A":
            check_name.append(1)
        else:
            check_name.append(0)

    index = 0  # 처음 시작은 0번째 인덱스 부터
    result1 = 0
    while 0 in check_name:  # check_name에 0이 없을 때 까지 반복
        if check_name[index] == 1:
            i = index + 1
            right = 1
            left = 1
            while check_name[i] == 1:  # 앞쪽 탐색
                right += 1
                i += 1
            else:  # 조건 초기화
                i = index - 1
            while check_name[i] == 1:  # 뒤쪽 탐색
                left += 1
                i -= 1

            if first:
                index += right
                result1 += right
                first = False
                continue

            if right < left:
                index += right
                result1 += right
            else:
                index -= left
                result1 += left
            continue

        asciicode = ord(name[index])
        if asciicode > ord("N"):  # 110 = N의 아스키코드
            result1 += ord("Z") - asciicode + 1  # ex) alphabet = P, 122-112+1 = 11
            check_name[index] = 1
            continue
        result1 += asciicode - ord("A")  # ex) alphabet = J, 106 - 97 = 9
        check_name[index] = 1

    first = True
    check_name = []
    for word in name:
        if word == "A":
            check_name.append(1)
        else:
            check_name.append(0)

    index = 0  # 처음 시작은 0번째 인덱스 부터
    result1 = 0
    while 0 in check_name:  # check_name에 0이 없을 때 까지 반복
        if check_name[index] == 1:
            i = index + 1
            right = 1
            left = 1
            while check_name[i] == 1:  # 앞쪽 탐색
                right += 1
                i += 1
            else:  # 조건 초기화
                i = index - 1
            while check_name[i] == 1:  # 뒤쪽 탐색
                left += 1
                i -= 1

            if first:
                index -= left
                result1 += left
                first = False
                continue

            if right < left:
                index += right
                result1 += right
            else:
                index -= left
                result1 += left
            continue

        asciicode = ord(name[index])
        if asciicode > ord("N"):  # 110 = N의 아스키코드
            result1 += ord("Z") - asciicode + 1  # ex) alphabet = P, 122-112+1 = 11
            check_name[index] = 1
            continue
        result1 += asciicode - ord("A")  # ex) alphabet = J, 106 - 97 = 9
        check_name[index] = 1

    first = True
    check_name = []
    for word in name:
        if word == "A":
            check_name.append(1)
        else:
            check_name.append(0)

    index = 0  # 처음 시작은 0번째 인덱스 부터
    result2 = 0
    while 0 in check_name:  # check_name에 0이 없을 때 까지 반복
        if check_name[index] == 1:
            i = index + 1
            right = 1
            left = 1
            while check_name[i] == 1:  # 앞쪽 탐색
                right += 1
                i += 1
            else:  # 조건 초기화
                i = index - 1
            while check_name[i] == 1:  # 뒤쪽 탐색
                left += 1
                i -= 1

            if first:
                index -= left
                result2 += left
                first = False
                continue

            if right <= left:
                index += right
                result2 += right
            else:
                index -= left
                result2 += left
            continue

        asciicode = ord(name[index])
        if asciicode > ord("N"):  # 110 = N의 아스키코드
            result2 += ord("Z") - asciicode + 1  # ex) alphabet = P, 122-112+1 = 11
            check_name[index] = 1
            continue
        result2 += asciicode - ord("A")  # ex) alphabet = J, 106 - 97 = 9
        check_name[index] = 1

    first = True
    check_name = []
    for word in name:
        if word == "A":
            check_name.append(1)
        else:
            check_name.append(0)

    index = 0  # 처음 시작은 0번째 인덱스 부터
    result2 = 0
    while 0 in check_name:  # check_name에 0이 없을 때 까지 반복
        if check_name[index] == 1:
            i = index + 1
            right = 1
            left = 1
            while check_name[i] == 1:  # 앞쪽 탐색
                right += 1
                i += 1
            else:  # 조건 초기화
                i = index - 1
            while check_name[i] == 1:  # 뒤쪽 탐색
                left += 1
                i -= 1

            if first:
                index += right
                result2 += right
                first = False
                continue

            if right <= left:
                index += right
                result2 += right
            else:
                index -= left
                result2 += left
            continue

        asciicode = ord(name[index])
        if asciicode > ord("N"):  # 110 = N의 아스키코드
            result2 += ord("Z") - asciicode + 1  # ex) alphabet = P, 122-112+1 = 11
            check_name[index] = 1
            continue
        result2 += asciicode - ord("A")  # ex) alphabet = J, 106 - 97 = 9
        check_name[index] = 1

    return min(result1, result2)