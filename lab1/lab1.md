# **COMPSCI 235 - LAB 1**
###### Name: Dylan Choy             UPI: dcho282

## **Notes**

Software Versioning:
- Easy versioning convention that allows programmers to differentiate each published software
- Typical versioning format is x.y.z, where:
    - x = Major release that is not backwards compatible with previous versions
    - y = Minor release that adds additional features to current software release which is backwards compatible
    - z = Patch that includes bug fixes for the current software release
- Many packages have dependency/minimal version requirements, meaning that in order to install and use said packages, you must have a specific minimum software version installed

IDE & Debugging:
- IDE stands for Integerated Development Environment, an all-in-one enviornment software that allows you to edit and debug your code 
- There are many IDEs, including popular ones such as IDLE, PyCharm or VS Code
- Each IDE has their own pros, cons, and features. It all comes down to personal preference
- Has a debugging feature that allows you to insert breakpoints into your code to stop your program from executing further beyond that
- There are controls that allow you to traverse your code at a breakpoint:
    - Step over takes you to the next line of code, regardless of whether the highlighted line have calls to methods or not
    - Step into takes you within the method and shows you how the method works
    - Step out takes you out of the method back to the caller method

Terminal:
- Getting familiar with using terminal and terminal commands is a good way to become a better developer, since this is the easiest way to interact with a server
- Additionally, most servers do not have a graphical UI that users can interact with

Basic commands:
```bash
# Navigate to 'home' directory
cd ~

# Create a folder called "workspace"
mkdir workspace

# Rename / move "workspace" to "my_projects"
mv workspace my_projects

# Remove "my_projects" folder; '-r' for recursive
rm -r my_projects

# Check if Python is installed
python --version
python3 --version

# Check if Anaconda is installed
conda --version

# Check if pip is installed
pip --version
```

Virtual Environment:
- A virtual instance of a specific Python version and its installed packages 
- This is useful for developing projects that are built on specific packages version in the long term, as those packages won't automatically update unless you manually update it yourself
- virtualenv is an environment manager, and pip is a package installer
    - conda is both of these combined
- If you want to allow other users to collaborate with your project, you can save the package info that retains each package version that is compatible

Pip and Conda commands:
```bash
# List all created env
conda env list

# Create an env called "cs235" using Python 3.9
conda create -n cs235 python=3.9

# Activate and deactivate "cs235" env 
conda activate cs235
conda deactivate

# Install package from channel conda-forge
conda install -c conda-forge packageName

# Remove "cs235" env
conda env remove -n cs235

# Once you have activated your env:
# Save all package dependencies to 'requirements.txt'
pip freeze > requirements.txt

# Install package dependencies from 'requirements.txt'
pip install -r requirements.txt
```

Git & GitHub
- Version control system that supports collaborative software development across multiple users
- There are many online service providers that implement Git for you, one of the most popular being GitHub
    - a cloud-based service aimed to help developers manage their code effectively in a collaborative environment

## **Hands-on Lab Activity:**

### Virtual Environments

requirements.txt file contents:
```
certifi @ file:///private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_884c889c-96af-444f-bd6d-daddb5e9a462ykj3l5n_/croots/recipe/certifi_1655968814730/work/certifi
numpy @ file:///Users/runner/miniforge3/conda-bld/numpy_1626682195712/work
```

### Debugging

**Question 1:** What is the probability of winning a game?
> The probability of winning a game is 1/100, or 0.01.

**Question 2:** Using the debugging feature, WITHOUT changing any code, it is possible to win every game. What line did you insert the breakpoint at? 
> I inserted the breakpoint at line 50.

**Question 3:** Using the debugging feature only, is it possible the user can win every game by guessing "42"?
> No, it is not possible. Since the program grabs a random number between 1 and 100 inclusive every game, there is a 1 in 100 chance that the number to guess is in fact "42". Using the debugging feature will only allow you to see what number the computer has randomly selected.

### GitHub
> My GitHub Account: https://github.com/ghxstling
