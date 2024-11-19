from santa.file_handler import FileHandler
from santa.secret_santa import SecretSanta

def main():
    employees_file = r"D:\Digit\Excel_files\Employee-List.xlsx"
    previous_assignments_file = r"D:\Digit\Excel_files\Secret-Santa-Game-Result-2023.xlsx"
    output_file = "secret_santa_assignments.xlsx"

    try:
        employees = FileHandler.load_employees(employees_file)
        previous_assignments = FileHandler.load_previous_assignments(previous_assignments_file)

        secret_santa = SecretSanta(employees, previous_assignments)
        assignments = secret_santa.assign()

        FileHandler.save_assignments(assignments, output_file)
        print(f"Secret Santa assignments saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
