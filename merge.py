import os
import glob

def merge_files(output_dir, output_file):
    # Find all part files and sort them
    part_files = glob.glob(os.path.join(output_dir, "part_*.json"))
    part_files.sort()
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for part_file in part_files:
            with open(part_file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
    
    print(f"Merged into {output_file}")

if __name__ == "__main__":
    output_dir = r"c:\Users\tomis\Documents\vscode-loc\split_files"
    output_file = r"c:\Users\tomis\Documents\vscode-loc\i18n\vscode-language-pack-vi\translations\main.i18n.json"
    merge_files(output_dir, output_file)