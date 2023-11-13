# User Task Manager (to-do-list)
# this programe that should allow users to 
# 1. add
# 2. view
# 3. update
# 4. delete
# tasks.


class TasksManager:


    # class variable
    # dictionary to store all the tasks
    _all_tasks = {}


    # object intialization
    def __init__(self, username, password):
       self.username = username
       self.password = password
    

    # this function will add a task to a file
    def add_task(self, title, description, due_date):
        self._all_tasks['title'] = title
        self._all_tasks['description'] = description
        self._all_tasks['due_date'] = due_date

        
        # adding tasks to a file for future retreaval 
        database = open('C:/Users/user/Desktop/Python_Learning/projectOne/database.txt', '+a')

        index = 1
        for key in self._all_tasks:
            database.write(f'{self._all_tasks[key]}\n')
            index += 1

            if index == 4:
                database.write(f'---------------------------------------------------\n')
            else:
                continue

        database.close()


    # contents of the file opened is stored in this function
    def view_tasks(self):
        database = open('C:/Users/user/Desktop/Python_Learning/projectOne/database.txt', '+r')
        return database.read()


    def update_task(self, title):
        pass


    def delete_tasks(self):

        # open the file that hold the tasks
        database = open('C:/Users/user/Desktop/Python_Learning/projectOne/database.txt', 'w')
        database.write('')
        database.close

        print()
        print('All tasks deleted. You can start a fresh.')
        print()

