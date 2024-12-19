# def print_items(n):
#     for i in range(n):
#         print(f"numero: {i}") # O(n)
    
#     for j in range(n):
#         print(f"numero: {i}") # O 2(n) Drop constant and it becomes O(n)
# print_items(7)

def print_items2(n): #0(n2square)
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items2(3)