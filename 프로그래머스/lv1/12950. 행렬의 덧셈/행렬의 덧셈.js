function solution(arr1, arr2) {
    const answer = []
    const firstLen = arr1.length
    const secondLen = arr1[0].length
    

    for (let i = 0; i < firstLen; i++) {
        const rowArr = []
        for (let j = 0; j < secondLen; j++ ) {
            rowArr.push(arr1[i][j] + arr2[i][j])
        }
        answer.push(rowArr)
    }
    return answer
}