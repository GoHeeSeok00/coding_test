function solution(s) {
    const answer = [];
    const words = s.split(' ');
    console.log(words);
    for (const word of words) {
        if (word === '') {
            answer.push(word);
        } else if (isNaN(word[0])) {
            answer.push(word[0].toUpperCase() + word.slice(1).toLowerCase());
        } else {
            answer.push(word.toLowerCase());
        }
            
        console.log(word);
    }
    return answer.join(' ');
}