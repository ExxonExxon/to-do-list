import os
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Cross-platform terminal clear
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class Taskiy:
    def __init__(self) -> None:
        self.tasks = []
        self._run()
    
    def _run(self):
        while True:
            self.view_choices()
    
    def view_tasks(self, extra_prompt: bool = False):
        """View all tasks, prompt to create one if none exist.
            the variable 'extra_prompt' is so it can say, here are all of the tasks before deletion.
        """
        clear()
        
        if self.tasks:
            if extra_prompt == True:
                print(Fore.LIGHTMAGENTA_EX + "Because you are about to delete all of the tasks here they are just to view them before deletion. " + Fore.RESET)
                
                
            print(Fore.CYAN + "\nHere are all of the tasks:\n" + Fore.RESET)
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. - {Fore.GREEN}{task.capitalize()}{Fore.RESET}")
        else:
            print(Fore.RED + "Looks like there are no tasks! Create one!" + Fore.RESET)
        
        if extra_prompt == True:
            input(Fore.YELLOW + "\nPress Enter to continue..." + Fore.RESET)
        else:
    
            input(Fore.YELLOW + "\nPress Enter to return to the main menu..." + Fore.RESET)
        clear()
            
    def add_task(self):
        """Adds a task from user input, can exit to main menu."""
        clear()
        print(Fore.CYAN + "Type the name of the task or type 'exit' to go back." + Fore.RESET)
        
        while True:
            _new_task_name: str = input(Fore.LIGHTYELLOW_EX + "New Task: " + Fore.RESET).strip()

            if _new_task_name.lower() == "exit":
                clear()
                break
            elif _new_task_name:
                self.tasks.append(_new_task_name.lower())
                print(Fore.GREEN + f"Task '{_new_task_name.capitalize()}' added successfully!" + Fore.RESET)
                time.sleep(1)
                clear()
                break
            else:
                print(Fore.RED + "Task name cannot be empty!" + Fore.RESET)
        
    def delete_task(self):
        """Delete a task by typing its number; prompt if no tasks exist."""
        clear()
        
        if self.tasks:
            while True:
                self.view_tasks(True)
                try:
                    _task_to_delete: str = input(Fore.RED + "Enter the task number to delete (or type 'exit' to cancel): " + Fore.RESET).strip()

                    if _task_to_delete.lower() == 'exit':
                        clear()
                        break
                    
                    _task_to_delete = int(_task_to_delete) - 1

                    if 0 <= _task_to_delete < len(self.tasks):
                        _task = self.tasks[_task_to_delete]
                        confirmation = input(f"Are you sure you want to delete '{Fore.GREEN}{_task.capitalize()}{Fore.RESET}'? (y/n): ").lower()
                        
                        if confirmation == 'y':
                            self.tasks.pop(_task_to_delete)
                            print(Fore.GREEN + f"Task '{_task.capitalize()}' deleted successfully!" + Fore.RESET)
                        else:
                            print(Fore.YELLOW + "Task not deleted." + Fore.RESET)
                        time.sleep(1)
                        clear()
                        break
                    else:
                        print(Fore.RED + "Invalid task number!" + Fore.RESET)
                except ValueError:
                    print(Fore.RED + "Please enter a valid number." + Fore.RESET)
                time.sleep(1)
                clear()
        else:
            print(Fore.RED + "There are no tasks to delete!" + Fore.RESET)
            time.sleep(1)
            clear()
    
    def view_choices(self):
        """Displays menu options and processes user input."""
        print(Fore.LIGHTMAGENTA_EX + "\n1. View Tasks")
        print("2. Add a Task")
        print("3. Delete a Task")
        print("4/exit. Exit" + Fore.RESET)
        
        _given_input = input(Fore.MAGENTA + "\nWhat would you like to do? - " + Fore.RESET).strip()

        match _given_input:
            case "1":
                self.view_tasks()
            case "2":
                self.add_task()
            case "3":
                self.delete_task()
            case "4" | "exit":
                print(Fore.YELLOW + "Goodbye!" + Fore.RESET)
                exit()
            case _:
                clear()
                print(Fore.RED + "ERROR: Please type in a valid number" + Fore.RESET)
            
def main():
    taskiy = Taskiy()

if __name__ == "__main__":
    main()
