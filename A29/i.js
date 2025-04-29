// --- Data ---
const initialTasks = [
    { id: 1, text: 'Learn HTML', completed: true },
    { id: 2, text: 'Learn CSS', completed: true },
    { id: 3, text: 'Learn Core JavaScript', completed: false },
    { id: 4, text: 'Practice JavaScript', completed: false }
];
let tasks = [...initialTasks]; // Mutable copy

// --- DOM References ---
const taskListElement = document.querySelector('#taskList');
const addTaskForm = document.querySelector('#addTaskForm'); // Get the form
const newTaskInput = document.querySelector('#newTaskInput'); // Get the input field

// --- Functions ---
function displayTasks(tasksToDisplay) {
    taskListElement.innerHTML = '';
    tasksToDisplay.forEach(task => {
        const listItem = document.createElement('li');
        listItem.textContent = task.text;
        if (task.completed) {
            listItem.classList.add('completed');
        }
        // We'll add data attributes later for identifying tasks
        taskListElement.appendChild(listItem);
    });
}

/**
 * Handles the submission of the 'Add Task' form.
 * @param {Event} event - The event object from the form submission.
 */
const handleAddTask = (event) => {
    // Concept: Prevent default form submission behavior (page reload)
    event.preventDefault();

    // Concept: Read the value from the input field, trim whitespace
    const taskText = newTaskInput.value.trim();

    // Concept: Basic Validation - check if the input is not empty
    if (taskText) {
        // Concept: Create a new task object
        // Simple way to generate a unique-ish ID for this example
        const newTask = {
            id: Date.now(), // Using timestamp as a simple unique ID
            text: taskText,
            completed: false
        };

        // Concept: Add the new task to our tasks array (mutate the array)
        tasks.push(newTask);

        // Concept: Re-render the list to show the new task
        displayTasks(tasks);

        // Concept: Clear the input field after adding
        newTaskInput.value = '';
    } else {
        // Optional: Provide user feedback if the input is empty
        alert('Please enter a task!');
    }
};

// --- Event Listeners ---
// Concept: Add an event listener to the form to call handleAddTask on submit
addTaskForm.addEventListener('submit', handleAddTask);

// --- Initial Setup ---
displayTasks(tasks); // Display initial tasks

