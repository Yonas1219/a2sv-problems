/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    const wordArray = s.split(" ")
    const orderedSentence = []
    for (let i = 0; i< wordArray.length; i++){
        const idx = wordArray[i].slice(-1) -1
        orderedSentence[idx] = wordArray[i].slice(0, -1) 
    }
    return orderedSentence.join(" ")
};
