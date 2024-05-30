# This script reads a requirements.txt file, removes version constraints, and writes the unfreezed requirements to a new file.

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
