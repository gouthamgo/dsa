let numbers: number[] = [1,2,3,4]

// let varName: <type> = value 

let mixed: any[] = [1, 'ra', 23, true]

// numbers.push('seven') -- not allowed 

/**
 * Tuple 
 
 */

let personTuple: [string, number, boolean] = ['check', 30 , true]


/**
 * Objects
 */


let person : {
    name: string,
    location: string,
    isPlayer: boolean;
};

person={
    name : 'Alice',
    location:'USA',
    isPlayer: true
}


// person.isPlayer = 'Yes' - not allowed 

// cant add new object without all properties 

// person={
//     name: 'te',
//     location: 'Den'
// }


interface Person{
    name : String[] = 
}



