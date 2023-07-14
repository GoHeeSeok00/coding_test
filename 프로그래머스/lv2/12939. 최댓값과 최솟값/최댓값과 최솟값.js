function solution(s) {
    let maxN
    let minN
    
    const numList = s.split(' ').map((v) => Number(v))
    maxN = numList[0]
    minN = numList[0]

    for (let i = 1; i < numList.length; i++) {
        if (maxN < numList[i]) {
            maxN = numList[i]
        }
        if (minN > numList[i]) {
            minN = numList[i]
        }
    }
    return `${minN} ${maxN}`
}