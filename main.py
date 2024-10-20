import os
from colorama import init, Fore
    
# clear crap
clear = lambda: os.system('clear')

class Taskiy():
    def __init__(self) -> None:
        self.tasks = []
        self._run()
    
    def _run(self):
        while True:
            self.view_choices()
    
    def view_tasks(self):
        """
        A function to view all the tasks, if there are no tasks then it will prompt the userto make one!
        """
        
        if len(self.tasks) != 0:
        
            print("\nHere are all of the tasks!\n")

            for i in range(len(self.tasks)):
                print(f"{i + 1}. - {Fore.GREEN}{self.tasks[i].capitalize()}{Fore.RESET}")
                
        else:
            print("Looks like there are no tasks! Make one!")
            
            
            
    def add_task(self):
        """ 
        Adds a task of the users choice and capitalizes it. You can type in exit to go back to main menu
        """
        
        clear()
        
        print("Type in the name of the task or type in exit to go back to the main screen")
        _new_task_name: str = input()
        
        if _new_task_name.lower() != "exit":
            print("Adding the task " + Fore.GREEN + _new_task_name.capitalize() + Fore.RESET)
            self.tasks.append(_new_task_name.lower())
        else:
            clear()
        
        
    def delete_task(self):
        """
        Delete a Task of any choice; you can type in the task number or the task name itself.
        """
        
        if len(self.tasks) != 0:
            print("What task would you like to delete? You can type in the name or the number of the tasks.")
            print("Keep in mind you can type 'exit' to go to the main menu.")
            self.view_tasks()
        
        
            while True:
                _which_task_to_delete: str = input(f"\n {Fore.RED}TASK TO DELETE - ")
                print(Fore.RESET)
                
                if _which_task_to_delete.lower() == "exit":
                    break
                    
                # Check if the input is a task name
                if _which_task_to_delete in self.tasks:
                    _given_input = input(f"Are you sure you want to delete '{_which_task_to_delete}'? (yes/y to confirm) ")
                    
                    if _given_input.lower() in ["yes", "y"]:
                        self.tasks.remove(_which_task_to_delete)
                        print(f"Task '{_which_task_to_delete}' has been deleted.")
                    else:
                        print("Deletion cancelled.")
                        
                else:
                    # Otherwise, try to check for the number
                    try:
                        task_index = int(_which_task_to_delete)
                        if 0 <= task_index < len(self.tasks):
                            task_to_delete = self.tasks[task_index]
                            _given_input = input(f"Are you sure you want to delete '{task_to_delete}'? (yes/y to confirm) ")
                            
                            if _given_input.lower() in ["yes", "y"]:
                                self.tasks.pop(task_index)  # Use pop to remove by index
                                print(f"Task '{task_to_delete}' has been deleted.")
                            else:
                                print("Deletion cancelled.")
                        else:
                            print("Please enter a valid task number.")
                            
                    except ValueError:
                        print("Please enter a valid task number or make sure the spelling of the task is correct.")

                    
                clear()
                print(f"{Fore.GREEN} Removed task! {Fore.RESET}")
                break
        else:
            print("There are no tasks so nothing to delete")
        
    
    def view_choices(self):
        print("\n1. View Tasks    .")
        print("2. Change a task .")
        print("3. Add a task    .")
        print("4. Delete a task .")
        print("5. Exit          .")

        _given_input: str = input("What would you like to do? - " + Fore.MAGENTA)
        print(Fore.RESET)

        match _given_input.lower():
            case "1":
                clear()
                self.view_tasks()
            
            case "2":
                pass
            
            case "3":
                clear()
                self.add_task()
            
            case "4":
                clear()
                self.delete_task()
            
            # Exiting will have 2 for different inputs
            
            case "5":
                clear()
                print("Byeee")
                exit()
            
            case "exit":
                clear()
                print("Byeee")
                exit()
            
            # If the user did not input anything
            
            case _:
                clear()
                print(Fore.RED + "ERROR: Please type in a valid number" + Fore.RESET)
            
                
    
            
            
def main():
    taskiy = Taskiy()
    pass

main()

