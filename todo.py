import os

fpath = 'todo.txt'

print("-----------------------------------------")
print("Welcome to Accomplish")
print("-----------------------------------------")


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

todo = []

running = True
while (True):
    cmd = input("> ").lower()
    if (cmd == 'a'):
        task = input("task: ")
        # todo.append(task)
        f = open("todo.txt", "a")
        f.write("{}\n".format(task))
        f.close()
        print("[*] Task added!")
    elif cmd == 'd':
        if os.stat(fpath).st_size != 0:
            print("-----------------------------------------")
            print("Tasks")
            print("-----------------------------------------")
            f = open("todo.txt", "r")
            for task in f:
                print("[+] ", task)
            print("-----------------------------------------")
            tasktodel = input("Enter a task to delete: ")
            f = open("todo.txt", "r")
            lines = f.readlines()
            f = open("todo.txt", "w")
            for line in lines:
                if line.strip() != tasktodel:
                    f.write(line)
            f.close()
            print("[*] Task deleted.")
        else:
            print("-----------------------------------------")
            print("[!] No tasks found!\n[*] Type 'a' to add a task.")
            print("-----------------------------------------")
        f.close()
    elif cmd == 'v':
        f = open("todo.txt", "r")
        if os.stat(fpath).st_size != 0:
            print("-----------------------------------------")
            print("Tasks")
            print("-----------------------------------------")
            for task in f:
                print("[+] ", task)
            print("-----------------------------------------")
        else:
            print("-----------------------------------------")
            print("[!] No tasks found!\n[*] Type 'a' to add a task.")
            print("-----------------------------------------")
        f.close()
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
