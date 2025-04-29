//  initialise array

const initialTasks  = [
    {id:1, text: 'Learn A', completed:true},
    {id:2, text: 'Learn B', completed:true},
    {id:3, text: 'Learn C', completed:false},
    {id:4, text: 'Learn D', completed:false},
]



let tasks = [...initialTasks];

console.log(tasks)

const taskListElement = document.querySelector('#taskList');


function displayTasks(tasksToDisplay){
    taskListElement.innerHTML = ' '

        tasksToDisplay.forEach(task => {
            const listItem  =  document.createElement('li');

            listItem.textContent = task.text;

            if(task.completed){
                listItem.classList.add('completed');
            }

            taskListElement.appendChild(listItem)
    });
}

displayTasks(tasks);
