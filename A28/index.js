let k = null
let r = undefined

console.log('lets see the value of k and r ' + typeof(k) +' and ' + typeof(r) )

const projectName = 'Learning Js';
let currentTopicIndex = 1;
let isChallengeComplete  = true ;

let nextTopicName = null

currentTopicIndex = 2;
// projectName = 'Mastering JS';

console.log(currentTopicIndex)



// An array of strings (topic names)
const topics = ["Variables", "Operators", "Arrays", "Objects"];

// An array of numbers
const scores = [85, 92, 78, 100];

// An array with mixed types (possible, but often better to keep types consistent)
const mixedData = ["Hello", 10, true, null];


console.log('length of the array ' + topics.length + ' now push somethigs ' +  topics.push("tes"))
console.log(topics);


const user = {
    firstName: "Alex",
    lastName: "Chen",
    age: 30,
    isOnline: true,
    favoriteTopics: ["Arrays", "Objects", "Functions"], // Value can be an array
    address: { // Value can be another object
      street: "123 Main St",
      city: "Anytown"
    }
  };

console.log(user['lastName'] , user.firstName)

let propertyToAccess = 'age';
console.log("Users age is " + user[propertyToAccess])

console.log(user.address.city)









const myPets = ["Dog", "Cat", "Hamster"]

console.log(myPets[1])
myPets.push("Fish")
console.log(myPets)

const book = {
    title : ' The Hobbit',
    author: 'J.R.R Tolkien',
    pageCount: 30
}

console.log(book.author)

book.pageCount = 320;

console.log(book)


function multiply( numA, numB){
    return numA * numB;
}

let productResult = multiply(6,7)

console.log(productResult)

const check = book.pageCount >500 ? "That's a long book!" : "That book is manageable."

console.log(check)

for(let i=0;i<myPets.length;i++){

    console.log('My pet: ' + myPets[i] )
}





const functionName = (param1, param2) => {
    return someValue;
}

const functionName1 = parameter => {
    return someValue;
}




// map = creates a new array - applyy to each element of the array

const numbers = [1, 2, 3, 4, 5, 6];
const users = [
  { id: 1, name: "Alice", isActive: true },
  { id: 2, name: "Bob", isActive: false },
  { id: 3, name: "Charlie", isActive: true }
];

const doubleNumbers = numbers.map(num => num *2)
console.log(doubleNumbers);

const getUserNames = users.map(user => user.name)
console.log(getUserNames);


const evenNumbers = numbers.filter(num => num%2 === 0)
console.log(evenNumbers);

const userBob = users.find(user => user.id === 2)
console.log(userBob)

const coordinates = [10,20,30];

const[x,y,z] = coordinates;
console.log(x,y,z)

const[a , ...rest] = coordinates
console.log(a)
console.log(rest)


// Works with function/method calls too
const adminUser = {
    name: "Admin",
    getPermissions: () => ["read", "write", "delete"]
  };
  const guestUser = {
    name: "Guest"
    // getPermissions method is missing
  };
  
  const adminPerms = adminUser.getPermissions?.(); // Calls the function
  const guestPerms = guestUser.getPermissions?.(); // Doesn't error, returns undefined
  
  console.log("Admin Perms:", adminPerms); // Output: [ 'read', 'write', 'delete' ]
  console.log("Guest Perms:", guestPerms); // Output: undefined


 // Difference from || (Logical OR):
// The || operator returns the right-hand side if the left-hand side is any "falsy" value (null, undefined, 0, "", false, NaN).
// The ?? operator only triggers for null or undefined. This is useful when values like 0 or "" (empty string) are valid inputs that you want to keep.

// Syntax:
// leftOperand ?? rightOperand
  let configValue;

  const animationSpeedOr = configValue ?? 500
  console.log(animationSpeedOr)










const getSquare = number =>{
 return number * number;;
}  

console.log(getSquare(2))

const products = [
    { name: "Laptop", price: 1200 }, 
    { name: "Mouse", price: 25 },
     { name: "Keyboard", price: 75 }
    ];

const getNames = products.map(product => product.name)
console.log(getNames)

const addFilter = products.filter( product => product.price < 100)
console.log(addFilter)


const car = { make: "Toyota", model: "Camry", year: 2021, color: "Blue" };

const {make, model, color: vehicleColor } = car

console.log(make, model,vehicleColor)


const userss = {
    name: "John",
    // address property is missing
    // address: {
    //   street: "456 Park Ave"
    // }
  };


  const streetNew = userss.address ?. street;
  console.log(streetNew)


 const userProfile = {
    name: 'Top',
    // preferences
    //theme
 }

 const userCheck = userProfile.preferences?.theme ?? 'light'
 console.log(userCheck)
 


 const students = [
    { id: 's1', name: 'Alice', major: 'Computer Science', gpa: 3.8 },
    { id: 's2', name: 'Bob', major: 'Physics', gpa: 3.2 },
    { id: 's3', name: 'Charlie', major: 'Computer Science', gpa: 3.9 },
    { id: 's4', name: 'Diana', major: 'Mathematics', gpa: 3.5 }
  ];
