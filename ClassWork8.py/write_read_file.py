# модуль ввода-вывода 


def write_file(data):
    with open('file.csv','a') as file:
        file.writelines(data)
        
def read_file():
    with open('file.csv','r') as file:
        return file.readlines()

def write_file(data):
    with open('file.json','a') as file:
        file.writelines(data)
        
def read_file():
    with open('file.json','r') as file:
        return file.readlines()        