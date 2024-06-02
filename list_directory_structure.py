import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        # Skip the venv directory
        dirs[:] = [d for d in dirs if d != 'venv']
        
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{sub_indent}{f}')

if __name__ == "__main__":
    startpath = 'D:\\mlproject'  # Replace with your folder path
    list_files(startpath)

