const fibMultiRegression = (n) => {

    if (n <= 1) {
        return 0
    }

    if (n === 1) {
        return 1
    }

    else {
        return fib(n-1) + fib(n-2)
    }
}

// console.log(fib(0));
// console.log(fib(1));
// console.log(fib(6));


const fibbonaciLinear = (n) => {
    
    if (n <= 1) {
        return n
    }
    
    let prev = 0
    let current = 1
    let temp = 0

    while (n > 1) {
        temp = prev + current
        prev = current
        current = temp
        n -= 1
    } 
    
    return current
}

const fibbonaci = (n, prev = 0, current = 1) => {
    if (n < 2) {
        return n
    } else if (n === 2) { 
        return prev + current
    } else {
        return fibbonaci(n-1, current, prev + current)
    }   
}

// for (let i = 0; i < 13; i++) {
//     console.log(i, fibbonaci(i))
// }


// Question 2
const isSubList = (arr1, arr2) => {
    
    let bigArr = null
    let smallArr = null

    if (arr1.length > arr2.length) {
        bigArr = arr1
        smallArr = arr2
    } else {
        bigArr = arr2
        smallArr = arr1
    }

    const counterObj = {}

    for (let string of smallArr) {
        if (!counterObj[string]) {
            counterObj[string] = 1
        } else {
            counterObj[string] += 1
        }
    }

    for (let string of bigArr) {
        if (counterObj[string]) {
            counterObj[string] -= 1
        }
    }

    for (num of Object.values(counterObj)) {
        if (num !== 0) {
            return false
        }

    return true
    }
}

// console.log(isSubList(['hello', 'there', 'the'], ['hello', 'the']))
// console.log(isSubList(['the'], ['hello', 'the']))
// console.log(isSubList(['the', 'thing'], ['hello', 'the', 'cat']))
// console.log(isSubList(['the', 'hello'], ['hello', 'the']))
// console.log(isSubList(['hello', 'something', 'cat'], ['hello', 'hello']))
// console.log(isSubList(['hello', 'something', 'cat', 'hello'], ['hello', 'hello']))

// Question 3

const googleSearcher = (keywordsArr, websiteArr) => {

    // O(n) --> Get keywords array into an object for O(1) access
    const keywordObject = keywordsArr.reduce((obj, item) => {
        obj[item] = 0;
        return obj
    }, {});

    let start = 0
    let end = 0
    let wordRequirement = keywordsArr.length
    let wordsActiveCounter = 0

    for (let [index,string] of websiteArr.entries()) {

        if (keywordObject[string]) {

            if (keywordObject[string] == 0) {
                wordsActiveCounter += 1
            } 

            keywordObject[string] = index
        } 

        else () {

        }
    }

    
}

googleSearcher(['plane', 'airport', '747'], ['the', 'plane', 'landed', 'at', 'the', 'airport', 'and', 'landed', 'safely', 'this', '747', 'plane', 'was', 'a', 'near', 'miss', 'for', 'the', 'long', 'running', '747', 'capable', 'airport']);