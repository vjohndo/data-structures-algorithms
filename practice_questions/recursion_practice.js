const stars = (n) => {
    // log rows of stars to the console at half stars
    if ( n <= 1 ) {
        console.log('*')
        return
    }

    console.log('*'.repeat(n))

    return stars(Math.floor(n / 2));
}

// stars(100);

const countStar = (n) => {
    
    if ( n <= 1 ) {
        return 1
    } 

    return n + countStar(Math.floor(n / 2));
}

// console.log(countStar(100));

// const isBalanced = (string, currentIndex = 0, stack = []) => {
//     // Base case
//     if ( currentIndex === string.length  && stack === 0) {
//         return true
//     } 

//     if (stack.length === 0) { 
//         stack.push(string[currentIndex]) // Add string to stack if empty
//     } else if (stack[stack.length-1] === string[currentIndex]) {
//         stack.push(string[currentIndex]) // Add string to stack if not the same
//     } else {
//         stack.pop() // Get rid of previous if not the same
//     }

//     // 
//     console.log(stack);
//     return isBalanced(string, currentIndex + 1, stack)
// }

const isBalanced1 = (string) => {

    // O(n^2) time complexity

    // Base case
    if ( string === "()" ) {
        return true
    } else if ( !string.includes("()") ) { //O(n)
        return false
    }

    // Remove inner most bracket
    return isBalanced(string.replace("()",""))
}


const isBalanced2 = (string) => {

    // O(n^2) time complexity

    // Base case
    if ( string === "()" ) {
        return true
    }

    if ( !string.includes("()") ) { //O(n)
        return false
    }

    // Remove inner most bracket
    return isBalanced(string.replace("()","")) //O(n)
}


const inBalancedRecursion = (string) => {
    const charArr = string.split("");
    return isBalanced(charArr);
}

const isBalanced = (arr, startIndex = 0, currentIndex = 0) => {
    // This implementation is O(n). 
    // The trick for this is instead of keeping a stack, we can keep track the number of unbalanced brackets (current index).
    // Should we find enough we can remove

    // if we've reached the end of the array and have accounted for every item in the array 
    // The current Index will be 0, i.e. all brackets accounted for or bracket > 0. there was a misssing open bracket
    // Base case 1 & 2
    if (startIndex === arr.length) {
        return (currentIndex === 0) 
    }

    // if the current index every goes below zero there was a missing closing braket
    // Base case 3
    if (currentIndex < 0) {
        return false
    }

    // If we have an opening braket, we'll need to eventually find a closing bracket to match, current Index + 1
    if (arr[startIndex] == "(") {
        return isBalanced(arr, startIndex + 1, currentIndex + 1);
    
    // If we have an closing braket, we'll need to eventually find a closing bracket to match, current Index - 1
    } else if (arr[startIndex] == ")") {
        return isBalanced(arr, startIndex + 1, currentIndex - 1);
    }

}


console.log(isBalanced("()((())())"));
console.log(isBalanced("(()"));