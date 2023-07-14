function solution(x) {
    let sumNumber = 0
    for (const i of String(x)) {
        sumNumber += Number(i)
    }
    return x % sumNumber === 0
}