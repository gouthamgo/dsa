// Define the structure of a Habit
interface Habit {
    id: number;
    name: string;
    frequency: Frequency;
    completedDays: number;
    totalDays: number;
  }
  
  // Define possible frequencies for habits using an Enum
  enum Frequency {
    Daily = "Daily",
    Weekly = "Weekly",
  }
  
  // Array to store all habits
  let habits: Habit[] = [];
  
  // Function to add new habits
  function addHabit(name: string, frequency: Frequency, totalDays: number): void {
    const newHabit: Habit = {
      id: habits.length + 1,
      name,
      frequency,
      completedDays: 0,
      totalDays,
    };
    habits.push(newHabit);
    console.log(`Habit "${name}" added successfully!`);
  }
  
  // Function to mark a habit as completed for one day
  function markHabitCompleted(id: number): void {
    const habit = habits.find((habit) => habit.id === id);
  
    if (!habit) {
      console.log(`Habit with ID ${id} not found.`);
      return;
    }
  
    if (habit.completedDays < habit.totalDays) {
      habit.completedDays++;
      console.log(`Habit "${habit.name}" marked as completed for one day.`);
    } else {
      console.log(`Habit "${habit.name}" is already fully completed.`);
    }
  }
  
  // Function to view progress for all habits
  function viewProgress(): void {
    console.log("Habit Progress:");
    habits.forEach((habit) => {
      const progress = ((habit.completedDays / habit.totalDays) * 100).toFixed(2);
      console.log(`${habit.name}: ${progress}% completed`);
    });
  }
  
  // Example usage:
  addHabit("Exercise", Frequency.Daily, 30);
  addHabit("Read", Frequency.Daily, 15);
  markHabitCompleted(1);
  viewProgress();
  