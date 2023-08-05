# Problem Statement

## Creating a Task Tree with Subtasks and Grouping Tasks by Parent Class

Imagine we are developing a todo app with tasks, and we have already created a basic `Task` class to represent individual tasks. For example, we have a task called "Learn how the internet works," and everything seems fine at this point.

However, as we progress, we encounter a challenge when we want to add subtasks to existing tasks. Each subtask is an instance of the class `Task` and also has a `subtasks` attribute, allowing us to create a nested task tree.

Currently, our solution allows us to loop through one or two levels of subtasks, but it becomes limited when we need to go deeper into the nested subtasks.

Hardcoding the solution to obtain subtasks is one approach, but it restricts our ability to traverse an unlimited number of levels in the task tree.

In the file [tasks.py](./task.py), we provide a breakdown of our solution to tackle this issue. We aim to create a flexible and scalable solution that allows us to work with tasks and their subtasks at any level, avoiding the need for hardcoded limitations.
