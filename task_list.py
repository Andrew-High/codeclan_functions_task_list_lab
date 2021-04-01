import pdb

tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# define a function for tasks uncompleted
# set function parameters for tasks
# if task is false, add to new list
# print that new list

def uncompleted_tasks(list):
    task_list = []
    for task in list:
        if task["completed"] == False:
            task_list.append(task["description"])
    return task_list

# print(uncompleted_tasks(tasks))


def completed_tasks(list):
    task_list = []
    for task in list:
        if task["completed"] == True:
            task_list.append(task["description"])
    return task_list

# print(completed_tasks(tasks))


def all_tasks(list):
    task_list = []
    for task in list:
        task_list.append(task["description"])
    return task_list

# print(all_tasks(tasks))

# define a function for tasks over a given time, paramter for time input
# if task time is equal or greater to time input
# add task to new list

def tasks_over_certain_time(list, time):
    task_list = []
    for task in list:
        if task["time_taken"] >= time:
            task_list.append(task["description"])
    return task_list

# print(tasks_over_certain_time(tasks, 30))

def find_task(list, description):
    #pdb.set_trace()
    task_list = []
    for task in list:
        if task["description"] == description:
            task_list.append(task)
    return task_list

#print(find_task(tasks, "Walk Dog"))


# define a function to change a task to complete
# for each task, if false change to true
# return tasks

def mark_as_complete(list, task_tick):
    # pdb.set_trace()
    for task in list:
        if task["description"] == task_tick:
            if task["completed"] == False:
                task["completed"] = True
                return task
            else: 
                statement = "Already completed"
                return statement

#print(mark_as_complete(tasks, "Walk Dog"))

def add_task_to_list(list, description, completed, time_taken):
    list.append({
        "description": description,
        "completed": completed,
        "time_taken": time_taken
    })
    return tasks
    #list.append(task_to_be_added)

print(add_task_to_list(tasks, "Hoover", True, 20))