import os

def split_file(input_file, output_dir, lines_per_file=1000):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    num_files = (total_lines + lines_per_file - 1) // lines_per_file  # Ceiling division
    
    for i in range(num_files):
        start = i * lines_per_file
        end = min(start + lines_per_file, total_lines)
        chunk = lines[start:end]
        
        output_file = os.path.join(output_dir, f"part_{i+1:03d}.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(chunk)
        
        print(f"Created {output_file} with {len(chunk)} lines")

if __name__ == "__main__":
    input_file = r"c:\Users\tomis\Documents\vscode-loc\i18n\vscode-language-pack-vi\translations\main.i18n.json"
    output_dir = r"c:\Users\tomis\Documents\vscode-loc\split_files"
    split_file(input_file, output_dir)