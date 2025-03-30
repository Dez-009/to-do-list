import json

FILENAME = "tasks.json"

def get_tasks():
    """Get tasks from user and store them in a list of dictionaries."""
    tasks = []
    while True:
        task = {
            'task': input("Enter task: "),
            'priority': input("Enter priority (high, medium, low): ").lower(),
            'completed': False  # New tasks start as not completed
        }
        tasks.append(task)
        cont = input("Would you like to add another task? (yes/no): ").strip().lower()
        if cont != "yes":
            break
    return tasks

def write_tasks_to_file(tasks, filename=FILENAME):
    """Write tasks to a file."""
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def read_tasks_from_file(filename=FILENAME):
    """Read tasks from a file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def display_tasks(tasks):
    """Display all tasks with numbers and completion status."""
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):  # Ensure tasks are numbered
        status = "✓" if task.get("completed", False) else "✗"
        print(f"{i}. [{status}] {task['task']} (Priority: {task['priority']})")

def get_task_from_user(tasks):
    """Prompt user to select a task safely."""
    if not tasks:
        print("No tasks available.")
        return None

    display_tasks(tasks)

    while True:
        task_num = input("\nEnter the task number: ").strip()

        if not task_num.isdigit():
            print("Invalid input. Please enter a valid task number.")
            continue  # Ask again

        task_num = int(task_num) - 1  # Convert after validation

        if 0 <= task_num < len(tasks):
            return tasks[task_num]
        else:
            print("Invalid task number. Please choose a valid task.")

def delete_task(filename=FILENAME):
    """Delete a specific task."""
    tasks = read_tasks_from_file(filename)
    task_to_delete = get_task_from_user(tasks)
    if task_to_delete:
        tasks = [task for task in tasks if task != task_to_delete]
        write_tasks_to_file(tasks, filename)
        print("Task deleted successfully.")

def mark_task_as_complete(filename=FILENAME):
    """Mark a task as completed."""
    tasks = read_tasks_from_file(filename)
    task_to_mark = get_task_from_user(tasks)
    if task_to_mark:
        for task in tasks:
            if task == task_to_mark:
                task['completed'] = True
        write_tasks_to_file(tasks, filename)
        print("Task marked as completed!")

def main():
    """Main function for the program."""
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add tasks")
        print("2. Delete task")
        print("3. Mark task as completed")
        print("4. View tasks")
        print("5. Save and Exit")

        choice = input("What would you like to do? ").strip()

        if choice == "1":
            new_tasks = get_tasks()
            tasks = read_tasks_from_file()
            tasks.extend(new_tasks)
            write_tasks_to_file(tasks)
        elif choice == "2":
            delete_task()
        elif choice == "3":
            mark_task_as_complete()
        elif choice == "4":
            tasks = read_tasks_from_file()
            display_tasks(tasks)
        elif choice == "5":
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

