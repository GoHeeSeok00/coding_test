function solution(s) {
    const answer = [];
    const words = s.toLowerCase().split(' ');
    console.log(words);
    for (const word of words) {
        if (word === '') {
            answer.push(word);
        } else if (isNaN(word[0])) {
            answer.push(word[0].toUpperCase() + word.slice(1));
        } else {
            answer.push(word);
        }
            
        console.log(word);
    }
    return answer.join(' ');
}