
# We need to use a global variable to store the tasks tree; otherwise, it will reset and give us only the top parent Task instance and its subtasks
TASKS = {}

# A class to manage the tasks and create a nested loop for the tasks
class TaskTree:
    # tasks is a list of Task instances
    def __init__(self, tasks) -> None:
        self.tasks = tasks
        # Call the group_tasks method in the __init__ magic function | method since we don't need to do anything else with this class
        self._group_tasks(self.tasks)

    # Return the global TASKS variable
    def get_tasks(self):
        return TASKS

    # Class logic to solve the problem
    def _group_tasks(self, tasks):
        # Loop through the tasks
        for task in tasks:
            # Check if the task instance is a Parent or a subtask
            # If the task is not a subtask instance, we will append subtasks to it since we want
            # to group tasks by parent
            if task.parent is None:
                # If the task is already in the TASKS dict, we just need to append the subtask
                if TASKS.get(task.id):
                    # Make sure not to add duplicated subtasks
                    if not task.subtasks in TASKS[task.id]['subtasks']:
                        TASKS[task.id]['subtasks'].append(task.subtasks)
                # If the task is not in the TASKS variable as a parent, we can initialize the values
                # then return to the condition (if TASKS.get(task.id)) to append new subtasks
                else:
                    TASKS[task.id] = {
                        "task": task,
                        "parent": task.parent,
                        "subtasks": task.subtasks
                    }
                # Recursively call the _group_tasks method to loop on the subtasks objects
                # This nested loop is the solution to our problem
            # If the task is a subtask, we will search for its parent in the TASKS and modify its values, in this case, only the subtasks list
            else:
                # We'll apply the same conditions as in the first condition when the task is not a subtask
                if TASKS.get(task.parent.id):
                    if not task in TASKS[task.parent.id]['subtasks']:
                        TASKS[task.parent.id]['subtasks'].append(task)
                else:
                    TASKS[task.parent.id] = {
                        "task": task.parent,
                        "parent": None,
                        "subtasks": [task]
                    }
                # Recursively call the function for each task.subtasks to handle nested subtasks
                self._group_tasks(task.subtasks)
            
        # Return the TASKS object tree
        return TASKS

# A basic Task class
class Task:
    def __init__(self, task, parent=None) -> None:
        self.parent = parent
        self.subtasks = []
        self.task = task
        self.id = str(self.task).replace(" ", "_")
        self.tasktree = TaskTree([self]).get_tasks()

    def __repr__(self) -> str:
        return self.id

    def add_subtask(self, task):
        assert isinstance(task, self.__class__) == True, "task arg should be a Task instance "
        task.parent = self
        self.subtasks.append(task)
        return self

    def add_subtasks(self, tasks: list):
        task_list = []
        for task in tasks:
            if not isinstance(task, self.__class__):
                raise ValueError("Each item in the tasks list should be a Task instance ")
        for _ in tasks:
            _.parent = self
            task_list.append(_)

        self.subtasks.extend(task_list)
        return self

# Example Usage:

internet = Task("The Internet")

# Internet subtasks
what_is_the_internet = Task('what is the internet', internet)
# Set the parent subtasks
internet_subtasks = [what_is_the_internet]
internet.add_subtasks(internet_subtasks)

# what_is_the_internet subtasks
http_protocol = Task("What is an HTTP protocol ")
ssl_protocol = Task("What is an SSL protocol ")
udp_protocol = Task("What is a UDP protocol ")

# set what_is_the_internet subtasks
what_is_the_internet.add_subtasks([http_protocol, ssl_protocol, udp_protocol])



print(internet.tasktree)
