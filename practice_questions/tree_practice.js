// https://gist.git.generalassemb.ly/katie/2e6cba493e85502ccf38923aa7feb7e1

class Employee {
    constructor(name) {
        this.name = name
        this.subordinates = []
    }

    getName() {
        return this.name
    }

    addSubordinate(person) {
        this.subordinates.push(person)
    }

    getSubordinates() {
        return this.subordinates
    }
}

const janine = new Employee('Janine');
const fred = new Employee('Fred');
const sarah = new Employee('Sarah');
const damian = new Employee('Damian');
const brianna = new Employee('Brianna');
const mary = new Employee('Mary');
const sally = new Employee('Sally');
const alexis = new Employee('Alexis');
const george = new Employee('George');
const bob = new Employee('Bob');

janine.addSubordinate(fred);
janine.addSubordinate(sally);
janine.addSubordinate(bob);

fred.addSubordinate(sarah);
fred.addSubordinate(damian);
fred.addSubordinate(mary);

sally.addSubordinate(alexis);
sally.addSubordinate(george);

damian.addSubordinate(brianna);

// console.log(janine);
// const countEmployees = (employee) => {

//     if (employee.subordinates.length < 1) {
//         return 1
//     }

//     let subCount = employee.subordinates.reduce( (total, subordinate) => {
//         return total + countEmployees(subordinate);
//     }, 0);

//     return 1 + subCount;
// }


const countEmployees = (employee) => {

    subCount = employee.subordinates.reduce( (total, subordinate) => {
        return total + countEmployees(subordinate);
    }, 1);

    return subCount;
}

// console.log(countEmployees(janine));


// Company Structure
const listEmployees = (employee, indent = 0) => {

    // Print the current node.
    console.log(" ".repeat(indent),"-",employee.getName())

    // Go through each child and call the recursion on it. 
    employee.subordinates.forEach(subordinate => {
        listEmployees(subordinate, indent + 1)
    });
}

// listEmployees(janine);

// Respect my level
const levelEmployees = (employee) => {

    const queue = [];
    queue.unshift(employee);

    let penultimateNode = employee;
    let depthLevel = 0;


    while (queue.length !== 0) {
        person = queue.pop()

        console.log(`Level ${depthLevel}: ` + person.getName())

        for (subordinates of person.subordinates) {
            queue.unshift(subordinates)
        }

        // Use the queue structure 
        if (penultimateNode === person) {
            depthLevel ++;
            penultimateNode = queue[0];
        }
    }
}

levelEmployees(janine);

