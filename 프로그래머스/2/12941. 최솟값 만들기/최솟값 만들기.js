function solution(A,B){
    let answer = 0;

    // 각 배열에서 하나씩 뽑아서 곱한 수를 모두 더한값이 최솟값이 되러면 한 배열의 가장 높은 값과 다른 배열의 가장 낮은 값을 곱해야 함
    // 1. 각 배열 오름, 내림 차순 정렬
    // 2. 반복문으로 곱 연산 및 누적 더하기
    
    const aList = A.sort((a, b) => a - b);
    const bList = B.sort((a, b) => b - a);

    for (let i = 0; i < aList.length; i++) {
        answer += aList[i] * bList[i];
    }
    return answer;
}