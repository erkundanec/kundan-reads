---
title: Git and Github
description: A complete guide of how to use git and github
sidebar_position: 2
---
 Git is an open-source distributed version control system, freely available, and is the backbone of all GitHub-related actions that occur locally on your computer. This article compiles the key and commonly used Git commands for quick and convenient reference.

## List of important commands
1. **Initialize git**
    ```bash
    git init
    ```
2. **Stage all changes**
    ```bash
    git add .
    ```
3. **Check status**
    Check the status of your changes and ensure that they are staged.
    ```bash
    git status
    ```
4. **Commit changes**
    ```bash
    git commit -m "Your commit message here”
    ```
5. **List all branches**
    ```bash
    git branch
    ```
6. **Switch branch**
    ```bash
    git switch main
    ```
    or
    ```bash
    git checkout main
    ```
7. **Creates a new branch and switch to it**
    ```bash
    git checkout -b feature-branch
    ```
    or
    ```bash
    git switch -c feature-branch 
    ```
8. **List commit history**
    ```bash
    git log
    ```
9. **List commit history in the branch**
    ```bash
    git log branch_name
    ```

## What is branch?

To list all branches in a Git repository, you can use the following command:
    ```bash
    git branch
    ```

This command will show a list of all local branches in your repository, with an asterisk (**`*`**) next to the currently checked-out branch.

If you want to see both local and remote branches, you can use:

    ```bash
    git branch -a
    ```

This will show all branches, including remote branches. If you're specifically interested in remote branches, you can use:

    ```bash
    git ls-remote --heads origin
    ```

This command lists remote branches without fetching the actual branch data.

1. **View Branch Status:**
To see the status of the current branch, including uncommitted changes, use:
    
    ```bash
    git status
    ```
    
2. **View Commit History:**
To view the commit history of a branch, use the **`git log`** command.
    
    ```bash
    git log
    ```
    
    You can also view the commit history for a specific branch:
    
    ```bash
    git log branch_name
    ```
    
3. **Fetch Remote Branches:**
If there are remote branches, you can fetch them to see the latest changes without merging them into your local branches:
    
    ```bash
    git fetch
    ```
    
    This command fetches the latest changes from the remote repository.
    
4. **Compare Branches:**
To see the difference between two branches, you can use the **`git diff`** command:
    
    ```bash
    git diff branch1..branch2
    ```
    
    This shows the differences between the two branches.
    

## What is staged?

In Git, the term "staged" refers to the process of preparing changes to be included in the next commit. When you make modifications to files in your working directory, Git provides a staging area (also known as the index) where you can selectively choose which changes to include in your next commit.

Here's a basic overview of the staging process in Git:

1. **Working Directory:**
This is the directory on your local machine where you make changes to your project files. After making modifications, your changes are considered to be in the working directory.
2. **Staging Area (Index):**
The staging area is an intermediate area where you can selectively add changes before committing them. It allows you to review and organize your changes before they become part of a commit. The staging area is also referred to as the "index."
3. **Commit:**
Once you have staged the changes you want, you commit them to create a snapshot of your project's current state. Commits are permanent snapshots in the Git history that you can refer to and revert to if needed.

The basic Git commands for staging changes are as follows:

- **`git add`**: This command adds changes in the working directory to the staging area.
    
    ```bash
    git add file1 file2   # Stage specific files
    ```
    
    or
    
    ```bash
    git add .   # Stage all changes in the working directory
    ```
    
- **`git status`**: This command shows the status of changes as untracked, modified, or staged. It helps you understand which changes are ready to be committed.
    
    ```bash
    git status
    ```
    
- **`git diff`**: This command shows the differences between the working directory and the staging area.
    
    ```bash
    git diff
    ```
    

Once you have staged your changes, you can proceed to commit them using the **`git commit`** command. The commit will include only the changes that have been staged.

```bash
git commit -m "Your commit message here"
```

Understanding the staging area is a fundamental aspect of using Git, and it allows you to have fine-grained control over which changes are included in your commits.

## What is stash?

In Git, the **`git stash`** command is used to save changes that are not ready to be committed yet but need to be temporarily set aside. This is particularly useful when you need to switch to another branch or pull in changes from a remote repository without committing your current changes.

Here are some examples of how to use **`git stash`**:

### **Example 1: Stash Uncommitted Changes**

Suppose you have made some changes to your working directory but are not ready to commit them. You realize you need to switch to a different branch. You can stash your changes and switch branches:

```bash
# Stash the changes
git stash

# Switch to a different branch
git checkout another_branch

# Do some work on the new branch

# Switch back to the original branch
git checkout original_branch

# Apply the stashed changes
git stash apply
```

### **Example 2: Stash Uncommitted Changes with a Message**

You can provide a message when stashing changes to help you remember why you stashed them:

```bash
# Stash changes with a message
git stash save "Working on feature X"

or

# Stash changes, including untracked files
git stash -u

or

# Stash changes, keeping the changes in the staging area
git stash -k

# Do some work, switch branches, etc.

# Apply the stashed changes
git stash apply
```

## How to undo all the changes after last commit

If you want to undo all the changes made after the last commit and revert your working directory to the state of the last commit, you can use the **`git reset`** command combined with the **`--hard`** option. Here are the steps:

```bash
bashCopy code
# Undo all changes after the last commit
git reset --hard HEAD
```

Explanation:

- **`git reset`** is used to reset the current branch to a specific commit.
- **`-hard`** option discards all changes in the **working directory and staging area**, reverting them to the specified commit.

Please be cautious when using **`git reset --hard`**, as it permanently discards changes, and there is no easy way to recover them. 

If you have uncommitted changes that you want to keep, consider using **`git stash`** to temporarily save those changes.

If you want to undo only the changes in the working directory but keep the changes staged (i.e., changes that have been added using **`git add`**), you can use:

```bash
# Undo changes in the working directory
git reset --hard HEAD
```

This command will reset the working directory to the last commit, but keep the changes staged.

Always use these commands with caution, especially the **`--hard`** option, as it can result in data loss. 

**If you're uncertain about the changes you want to discard, consider creating a branch or using `git stash` to save your changes temporarily before performing any reset.**