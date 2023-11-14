# Global lists for tasks
tasks = []
tasks_priority = []
tasks_date = []
tasks_status = []

# Function to save tasks to a text file
def save_tasks_to_file(filename):
    with open(filename, 'w') as file:
        for i in range(len(tasks)):
            file.write(f"{tasks[i]},{tasks_priority[i]},{tasks_date[i]},{tasks_status[i]}\n")

# Function to load tasks from a text file
def load_tasks_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                tasks.append(data[0])
                tasks_priority.append(data[1])
                tasks_date.append(data[2])
                tasks_status.append(data[3])
    except FileNotFoundError:
        # Handle the case when the file does not exist
        pass

# Load tasks from a file on startup
load_tasks_from_file('tasks.txt')

def add_task():
    t1 = input("Enter new task name: ")
    tasks.append(t1)
    t2 = input("Enter task priority (H-High, M-Medium, L-Low): ")
    tasks_priority.append(t2)
    t3 = input("Enter due date for task: ")
    tasks_date.append(t3)
    print("Task has been added successfully")
    tasks_status.append("No")
    update_file_after_changes()

def view_task():
    if len(tasks) == 0:
        print("No Tasks")
    else:
        print("Sl No.    Task Name              Task Priority          Due Date         Status")
        for i in range(len(tasks)):
            sl_no = i + 1
            task_name = tasks[i]
            task_priority = tasks_priority[i]
            due_date = tasks_date[i]
            status = tasks_status[i]
            print(f"{sl_no:<8} {task_name:<21} {task_priority:<20} {due_date:<15} {status}")

def mark_task():
    ch = int(input("Enter task number which is completed: "))
    tasks_status[ch - 1] = "Yes"
    update_file_after_changes()

def delete_task():
    if len(tasks) == 0:
        print("No tasks to be deleted")
    else:
        print("Tasks:")
        for i in range(len(tasks)):
            print(tasks[i])
        choice = int(input("Enter the task number to delete: "))

        if 0 < choice <= len(tasks):
            del tasks[choice - 1]
            del tasks_priority[choice - 1]
            del tasks_date[choice - 1]
            del tasks_status[choice - 1]
            print("Task deleted successfully.")
            update_file_after_changes()
        else:
            print("Invalid Task Number")

# Function to update the file after any changes
def update_file_after_changes():
    save_tasks_to_file('tasks.txt')

def main():
    while True:
        print('\n======== To-Do-List Application ========')
        print("1. Add Task")
        print("2. View Task")
        print("3. Delete Task")
        print("4. Mark as Complete")
        print("5. Quit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            mark_task()
        elif choice == 5:
            print("Exiting")
            break
        else:
            print("Invalid Choice, Please Try again")

if __name__ == "__main__":
    main()

# Save tasks to the file before exiting
update_file_after_changes()
