import os
import re
import sys

def list_markdown_files():
    """
    List all markdown files in the current directory.
    """
    return [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.md')]

def select_markdown_file(markdown_files):
    """
    Prompt the user to select a markdown file.
    """
    if not markdown_files:
        print("No markdown files found in the current directory.")
        sys.exit(1)

    print("Select a markdown file to process:")
    for idx, filename in enumerate(markdown_files):
        print(f"{idx + 1}. {filename}")

    while True:
        try:
            choice = int(input("Enter the number of the file: "))
            if 1 <= choice <= len(markdown_files):
                return markdown_files[choice - 1]
            else:
                print("Invalid number. Please select a valid option.")
        except ValueError:
            print("Please enter a valid number.")

def replace_single_dollar_with_double(content):
    """
    Replace single $ with $$ and ensure that LaTeX is correctly opened and closed.
    """
    # Replace single dollar signs around LaTeX expressions
    updated_content = re.sub(r'(?<!\$)\$(?!\$)', r'$$', content)

    # Split the updated content by lines
    lines = updated_content.splitlines()

    for i, line in enumerate(lines):
        # Ensure that lines with LaTeX start and end with $$
        if line.count("$$") % 2 != 0:
            lines[i] = line + "$$"

    return "\n".join(lines)

def check_valid_markdown(content):
    """
    Checks for valid markdown, specifically ensuring all LaTeX blocks are properly closed.
    """
    dollar_pairs = re.findall(r'\$\$', content)

    if len(dollar_pairs) % 2 != 0:
        print("Warning: Mismatched $$ in LaTeX expressions!")
    else:
        print("All LaTeX expressions are properly closed with $$.")

def process_markdown_file(file_path):
    """
    Read the markdown file, process it, and write the updated content back to the file.
    """
    with open(file_path, 'r') as file:
        content = file.read()

    updated_content = replace_single_dollar_with_double(content)
    check_valid_markdown(updated_content)

    with open(file_path, 'w') as file:
        file.write(updated_content)

if __name__ == "__main__":
    markdown_files = list_markdown_files()
    selected_file = select_markdown_file(markdown_files)
    process_markdown_file(selected_file)
    print(f"Processed file: {selected_file}")
