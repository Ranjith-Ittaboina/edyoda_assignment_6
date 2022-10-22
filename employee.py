import json
file = "C:\\Users\Admin\\OneDrive\\Desktop\\edy_assignment\\assignment6\\employee.json"
with open(file) as json_file:
    json_data = json.load(json_file)
    python_lst = [json_data]

print(json_data)
print(python_lst)