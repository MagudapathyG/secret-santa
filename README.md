# Secret Santa Assignment

## Overview
This Python application automates the Secret Santa assignment process for employees. It follows specific constraints:
- No employee can select themselves.
- No employee can repeat the previous year's assignment.
- Each employee must have exactly one secret child\
- Each secret child should be assigned to only one employee.

## Installation
1. Clone the repository:

git clone https://github.com/your-username/secret-santa.git

2. Navigate to the project directory:

cd secret-santa

3. Install dependencies:

pip install -r requirements.txt


## Usage

1. Prepare `Excel_files\Employee-List.xlsx` and `Secret-Santa-Game-Result-2023.xlsx`.

2. Run the program:

python main.py

3. Run the tests with:

python -m unittest discover tests
