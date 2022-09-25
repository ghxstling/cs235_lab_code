# **COMPSCI 235 - LAB 2**
###### Name: Dylan Choy
###### UPI: dcho282

## **Notes**

Why use Git?
- Git keeps a record of all the changes you and your collaborators make, regardless of whether you are working on the same file or not
    - This makes it easier to keep track of what was updated and revert back to any file version should you need to
- To configure your Git username and email, you use the following commands in terminal:
```
git config --global user.name <usernamne>
git config --global user.email <email_address>
```

Linking an SSH key to your GitHub account
- Because GitHub does not allow authentication via passwords, you must generate a Secure Shell Protocol key pair from your computer, and link the public key to your GitHub account
    - An SSH key is an encrypted hardware string of letters and characters that is uniquely identifiable to you, like a more secure password
    - An SSH key consists of a public key (.pub file) that allows others to identify who you are, and a private key (no extension) linked to the former that should never be given out

Using Git
- After setting up a remote repository and cloning it to your system, you can interact with it by using the git command lines in terminal

Basic Git Commands:
```t
# Clone your Git repository to your computer from GitHub
git clone git@github.com:your-repository/repo.git

# Check current local status of working tree
git status

# Grab updates from remote repository
git pull

# Stage all files for updating; '-A' for all
git add -A
git commit -m "Insert message here"

# Update your remote repository
git push

# Create a branch
git branch <branch_name>

# Navigate to a branch
git checkout <branch_name>

# Merge your branch with the main branch
git merge <branch_name>

# Delete a branch
git branch -d <branch_name>
```

Gitignore
- Because Git cannot track binary files such as plots generated from your code as PNG files, you need to add .gitignore files to ensure that GitHub does not read these files at all

Best Practice
- Always test your code first before committing the code
- Never commit unfinished work to the main branch, do this in a temporary branch
- Ensure commit messages are concise and meaningful
- Always commit after completing every task, whether it be updating a function or adding a new file. Never commit large number of files at once
- Ensure that you maintain the styling convention consistently across the project
- Be nice to your collaborators :)

## **Hands-on Lab Activity:**

### Git Repository

**Question 1.** In a scenario, where you work with others as a team. You wrote some code using the lab machine, but the code isn't working. You decide to continue working on the code from home. What's the best way to commit your unfinished code to GitHub without interrupt others? What commands do you need to achieve that?
> The best way to commit unfinished code is to create a new temporary branch, visit that branch and commit the code there as usual. The command lines are:
```t
git branch <branch_name>
git checkout <branch_name>
```

**Question 2.** Explain the difference between merge and fork. Give an example for each use case.
> Merging is when you combine your committed code in a temporary branch with the main branch, thus updating the code in the main repository accordingly. Forking is when you make a copy of an existing repository to your local machine for your own use.
> An example of merging is when collaborating on code with another programmer on a repo, to avoid messing up the code in the main branch, each programmer can create a temporary branch of the code to amend changes or further develop on a section of a code without interferring or breaking the main branch in the repo. Once they have fully tested their code, they can them merge their branch into main and finally commit and push the changes
> An example of forking is if someone is to view another person's open source project, and would like to propose some changes, they can make a copy of the repository and clone them locally to make their own changes with their own copy. Once finished, they can make a pull request to the original owner with their proposed repo changes