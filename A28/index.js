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










