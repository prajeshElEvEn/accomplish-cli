print("-----------------------------------------")
print("Welcome to Accomplish")
print("-----------------------------------------")
# print('\n')


instructions = """
[?] How to Use? 🤔

-----------------------------------------
      [commands]  |     [Usage]
-----------------------------------------
[+]       a       |    add a task
[+]       d       |    delete a task
[+]       v       |    view all tasks
[+]       h       |    help
[+]       q       |    quit
-----------------------------------------
"""
print(instructions)
# print("[*] Type 'h' for help.")

todo = []

running = True
while (True):
    cmd = input("> ").lower()
    if (cmd == 'a'):
        task = input("task: ")
        todo.append(task)
        print("[*] Task added!")
    elif cmd == 'd':
        if todo:
            print("Tasks:")
            for task in todo:
                print("[*] ", task)
            task = input("Enter a task to delete: ")
            if task in todo:
                todo.remove(task)
                print("Task deleted", task)
            else:
                print("Task not found")
        else:
            print("No tasks to delete")
    elif cmd == 'v':
        if todo:
            print("-----------------------------------------")
            print("Tasks")
            print("-----------------------------------------")
            for task in todo:
                print("[+] ", task)
            print("-----------------------------------------")
        else:
            print("-----------------------------------------")
            print("[!] No tasks found!\n[*] Type 'a' to add a task.")
            print("-----------------------------------------")

    elif cmd == 'h':
        print(instructions)
    elif cmd == 'q':
        break
    else:
        print("[!] Wrong Command\n[*] Type 'h' to know all the commands.")
goodbye = '''
-----------------------------------------
See Ya! Have good one!
-----------------------------------------
'''
print(goodbye)
