# this is the program to run.


from http.client import PROCESSING
import _main 

task_manager = _main.TasksManager('Developer', 'kasero_the_pythonista.')

print()


while True:

    print('|---------------------------------------------------|')
    print('|                                                   |')
    print('| THIS IS A TO-DO-LIST APP.                         |')
    print('|                                                   |')
    print('| 1. Add a task.                                    |')
    print('| 2. View all task.                                 |')
    print('| 3. Delete all task.                               |')
    print('| 4. EXIT.                                          |')
    print('|                                                   |')
    print('|---------------------------------------------------|')

    choice = int(input('Choose 1/2/3: '))

    if choice == 1:
        print()
        print('ADD A TASK HERE: ')
        _title = input('1. Title: ')
        _description = input('2. Description: ')
        _dute_date = input('3. date(dd/mm/year): ')

        task_manager.add_task(_title, _description, _dute_date)
        print()

        print('----------DONE-----------')
        print()

    elif choice == 2:
        print()
        print('VIEW ALL TASKS.')
        print()
        print('Bellow are your tasks:')
        print()
        all_tasks = task_manager.view_tasks()
        print(all_tasks)
        print()


    elif choice == 3:
        print()
        print('DELETE ALL TASK AVAILABLE.')
        task_manager.delete_tasks()
        print()
        print('---------DONE----------')
        print()

    elif choice == 4:
        print()
        print('---------PROGRAM TERMINATED-----------')
        print()
        break

    else:
        print()
        print('---------INVALID INPUT-----------')
        print()

