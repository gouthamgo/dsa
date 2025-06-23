/**
 * adds static types 
 * 
 */


let config : string = "Adding to SFSC";

let number = 50 ;

console.log(typeof(number))

// function call 
function addContact(name:string, id:number) {
    console.log(`adding contact ${name} with ${id}`)
}

addContact("Trevor",30);
addContact("check") // error as there are not enought arguments 


function printId(id: number | string){

    console.log(`the id is ${id}`)
}

printId(100)

let mixedValue: string | boolean;
mixedValue = "hello"; // OK
mixedValue = true;    // OK
// mixedValue = 123;  // Error


function processId(id: number | string ){
    if(typeof id === "string"){
        console.log(id.toUpperCase())
    }
    else{
        console.log(id.toFixed(2))
    }
}


processId("abc-123"); // Prints: ABC-123
processId(45.678);   // Prints: 45.68



let scores = [];
scores = [1,2,3,4]

let flags : Array<boolean> = [ true, true]



function checkSum(a:number, b: number) : number {
    return a + b;
}

let checkTheType: number = checkSum(2,3);

function getUserName(id:number) : string{

    if(id === 1){
        return "Trev"
    }else{
        return 'not known'
    }
}

let userName : string  = getUserName(1);
console.log(userName);


function logMessage(message: string) : void {

    console.log(message)
}

logMessage("its gone")


type NumerCallback = (n: number ) => void;

function processNumbers(numbers: number [], callback: NumerCallback): void {
    numbers.forEach(num => {
        callback(num);
    })
}

const logNumber : NumerCallback = (n) => {
    console.log(`${n}`)
}


//Interface 

interface Person{
    firstName: string;
    age:number
}


let person1 : Person = {
    firstName: 'Clark',
    age:23
}

interface Employee extends Person{
    employeeId: number;
    department: string
}

