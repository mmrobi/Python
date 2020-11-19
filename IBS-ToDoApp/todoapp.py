import sys

def print_usage():
    print("Command Line ToDo Application\n=============================\n\nCommand line arguments:\n  -l  Lists all the tasks\n  -a  Adds a new task\n  -r  Removes a task\n  -c  Completes a task")



def list_tasks():
    try:
        tasklist= open("list.txt","r")
        print_tasks=tasklist.readlines()
        if len(print_tasks)==0:
            print("There aren't any tasks for today")
        else:
            lines=0
            for task in print_tasks:
                lines +=1
                print(str(lines)+" " + "-"+ " " +task,end='')
    except NameError:
        print("Unable to read list.txt")



def add_task(task):
    try:
        writetask=open("list.txt", "a")
        writetask.write("[ ] " + str(task) +"\n")
    except NameError:
        print("Unable to read list.txt")


def remove_task(index):
    try:
        readfile=open("list.txt","r")
        tasks=readfile.readlines()
        tasks[int(index)-1]=""
        writefile=open("list.txt","w")
        for task in tasks:
            writefile.write(task)
    except NameError:
        print("Unable to read list.txt")
    except IndexError:
        print("Unable to remove: index is out of bound")
    except ValueError:
        print("Unable to remove: index is not a number")

def check_out_task(index):
    try:
        readfile=open("list.txt", "r")
        list_tasks= readfile.readlines()
        checklist=[]
        for tasks in list_tasks:
            if tasks == list_tasks[int(index) - 1]:
                tasks=tasks.replace("[ ] ","[x] ")
                checklist.append(tasks)
            else:
                checklist.append(tasks)
        writefile=open("list.txt","w")
        for task in checklist:
            writefile.write(task)
    except NameError:
        print("Unable to read list.txt")
    except IndexError:
        print("Unable to check: index is out of bound")
    except ValueError:
        print("Unable to check: index is not a number")




if len(sys.argv)==1:
    print_usage()

elif len(sys.argv)>3 or (sys.argv[1] != "-l" and sys.argv[1] != "-a" and sys.argv[1] != "-r" and sys.argv[1] !=  "-c"):
    print("\nUnsupported argument\n\n")
    print_usage()

elif len(sys.argv)==2 and sys.argv[1]== "-l":
    list_tasks()

elif len(sys.argv)==3 and sys.argv[1]== "-a":
    task= str(sys.argv[2])
    add_task(task)

elif len(sys.argv)==2 and sys.argv[1]== "-a":
    print(" Unable to add: no task provided")

elif len(sys.argv)==3 and sys.argv[1]== "-r":
    index=sys.argv[2]
    remove_task(index)

elif len(sys.argv)==2 and sys.argv[1]== "-r":
    print("Unable to remove: no index provided")

elif len(sys.argv)==3 and sys.argv[1]== "-c":
    index=sys.argv[2]
    check_out_task(index)

elif len(sys.argv)==2 and sys.argv[1]== "-c":
    print("Unable to check: no index provided")

else:
    print("It's not done yet")

