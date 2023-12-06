import os

def process_line(line):
    # Split the line based on single quotes
    parts = line.split("'")

    # If the line contains "Name" and is structured as expected
    if "Name" in parts[0] and len(parts) == 3:
        value_inside_quotes = parts[1]
        return f"Name\n\ttesting\nName {value_inside_quotes}\n"
    else:
        return line

def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    with open(output_file_path, 'w') as output_file:
        for line in lines:
            processed_line = process_line(line)
            output_file.write(processed_line)

def process_folder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)
            process_file(input_file_path, output_file_path)

if __name__ == "__main__":
    input_folder = r"C:\Users\danie\Documents\Python\Diverse øvelser\Test_project01\Change smartproperty"  # Replace with the actual path to your input folder
    output_folder = r"C:\Users\danie\Documents\Python\Diverse øvelser\Test_project01\Change smartproperty\Output"  # Replace with the actual path to your output folder

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    process_folder(input_folder, output_folder)
