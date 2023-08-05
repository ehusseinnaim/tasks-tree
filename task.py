
# We have to use a global variable to store the tasks tree otherways it will rest and give us only the top parent Task instance and its subtasks 
TASKS = {}

# A class to make a nested loop for the tasks works as a manager for the tasks 
class TaskTree:
    # tasks is a list of Task|s
    def __init__(self,tasks) -> None:
        self.tasks = tasks
        # Calling the group_tasks method in the __init__ magic function | method since  we don't need to do anything else with this class 
        self._group_tasks(self.tasks)
    
    
    # Return the global TASKS variable
    def get_tasks(self):
        
        return TASKS

    # Class logic to solve the problme 
    def _group_tasks(self,tasks):
        
        # Loop on the tasks 
        for task in tasks:
            # Check if is the task instance a Parent or a subtask
            # If the task not a subtask instance we well append subtasks to it since we want 
            # To group tasks by parent 
            if task.parent is None:
                # if the task is already in the TASKS dict we just need to append the subtask 
                if TASKS.get(task.id):
                    # Make sure to not add a dublicated subtasks 
                    if not task.subtasks in TASKS[task.id]['subtasks']:
                        
                        TASKS[task.id]['subtasks'].append(task.subtasks)
                
                # If the task is not int the TASKS variavle as a parent we can initalize the values 
                # then return to the condation (if  TASKS.get(task.id) ) to append new sub tasks
                else:
                    TASKS[task.id] = {
                        "task":task,
                        "parent":task.parent,
                        "subtasks":task.subtasks
                    }
                # Recalling the _group_tasks method inside itself to loop on the subtasks objects 
                # in another word we're doing nested loop and this is the solution of our problem 

            # If the task is a subtask we will search for its parent in the TASKS and modify its values in this case only the subtasks list 
            else:
                # we'll make the same conditions in the first condition when the task is not a subtask 
                if TASKS.get(task.parent.id):
                    if not task in TASKS[task.parent.id]['subtasks']:
                        TASKS[task.parent.id]['subtasks'].append(task)
                
                else:
                    TASKS[task.parent.id] = {
                        "task":task.parent,
                        "parent":None,
                        "subtasks":[task]
                    }
                                    
                # Nested loop : we'll recall the function for each task.subtasks 
                self._group_tasks(task.subtasks)
            
        # Return the TASKS object tree
        
        return TASKS



# A basice Task class
class Task:
    
    
    def __init__(self,task,parent=None) -> None:
        
        self.parent = parent
            
        self.subtasks = []
    
        self.task = task
    
        self.id = str(self.task).replace(" ","_")
    
        self.tasktree = TaskTree([self]).get_tasks()
        

    
    def __repr__(self) -> str:
        
        return self.id

    def add_subtask(self,task):
        
        assert isinstance(task,self.__class__) == True, "task arg should be a Task instance "
    
        task.parent = self
    
        self.subtasks.append(task)
        
        return self

    def add_subtasks(self,tasks:list):
        task_list = []
        for task in tasks:
            
            if not isinstance(task,self.__class__):
                
                raise ValueError("Each item in the tasks list should be a Task instance ")
        
        for _ in tasks:
            
            _.parent = self
            
            task_list.append(_)

        
        self.subtasks.extend(task_list)
        
        return self

internet = Task("The Internet")

# Internet  subtasks
what_is_the_internet = Task('what is the internet',internet)
# what_is_the_internet subtasks
htttp_protocol = Task("What is an HTTP protocol ")
ssl_protocol = Task("What is a SSL protocol ")
udp_protocol = Task("What is a UDP protocol ")

# set what_is_the_interent subtasks
what_is_the_internet.add_subtasks([htttp_protocol,ssl_protocol,udp_protocol])


# Set the parent subtasks 
internet_subtasks = [what_is_the_internet]
internet.add_subtasks(internet_subtasks)

print(internet.tasktree)


