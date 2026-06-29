import os

# # 1: Imp Commands 
# print(os.getcwd()) # get current working directory
# print(os.path.abspath(__file__)) # get absolute path of the current directory
# print(os.path.dirname(os.path.abspath(__file__))) # get the directory name of this file
# print(os.listdir()) # list all the directories


## 2: File or Folder 
# for content in os.listdir():
#     if os.path.isfile(content):
#         print(f"{content} is a File")
#     elif os.path.isdir(content):
#         print(f"{content} is a directory")    

# # 3: Loading data 
file_loc = "data\orders.csv"
with open(file_loc, 'r') as file:
    content = file.read()

print(content)


