import os

def main():
    filename = input('Enter the filename to open or create: ').strip()
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
            
           



