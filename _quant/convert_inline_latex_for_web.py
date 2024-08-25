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
    Replace single $ with $$, ignoring blocks already enclosed in $$.
    """
    lines = content.splitlines()
    in_block = False
    updated_lines = []

    for line in lines:
        if line.strip().startswith("$$") and line.strip().endswith("$$") and not in_block:
            # Skip replacing in lines that are already fully enclosed in $$
            updated_lines.append(line)
        elif line.strip().startswith("$$") and not in_block:
            # Start of a $$ block
            in_block = True
            updated_lines.append(line)
        elif line.strip().endswith("$$") and in_block:
            # End of a $$ block
            in_block = False
            updated_lines.append(line)
        elif in_block:
            # Inside a $$ block, do not replace
            updated_lines.append(line)
        else:
            # Outside any $$ block, replace single $ with $$
            updated_line = re.sub(r'(?<!\$)\$(?!\$)', r'$$', line)
            updated_lines.append(updated_line)

    return "\n".join(updated_lines)

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
