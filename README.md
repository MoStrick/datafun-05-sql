# datafun-05-sql

This project demonstrates the ability to interact with a SQL database using Python. The script includes creating a database, defining a schema, and executing various SQL commands. Logging is incorporated to document the process and provide user feedback.

## A. Create Virtual Environment

### 1. GitHub Repository Setup
- Create a GitHub repository and add `README.md`, `.gitignore`, and `requirements.txt` files.
- Clone the GitHub repository in VS Code.

### 2. Activate Virtual Environment
Navigate to your project directory and run the following commands:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```sh
pip install requests
pip install pandas pyarrow
pip freeze > requirements.txt
cat requirements.txt
```

### 3.1 Unfreeze requirements
```sh
def unfreeze_requirements(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    with open(output_file, 'w') as outfile:
        for line in lines:
            # Split the line at the first occurrence of any of these version specifiers
            package = line.split('==')[0].split('>=')[0].split('<=')[0].split('>')[0].split('<')[0].strip()
            outfile.write(f"{package}\n")

# Specify the input and output file paths
input_file = 'requirements.txt'
output_file = 'unfrozen_requirements.txt'

# Unfreeze the requirements
unfreeze_requirements(input_file, output_file)

print(f"Unfrozen requirements written to {output_file}")
```


### 4. Git
```sh
git init
git add .
git commit -m "initial commit"
git push -u origin master

```


