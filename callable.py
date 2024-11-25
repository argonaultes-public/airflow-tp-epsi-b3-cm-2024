def return_10():
    print(10)

def print_hello():
    print('hello')
    return return_10

a = print_hello()
print(a)
b = print_hello
print(b)
b()
#print_hello

def call_print_hello(a_function_printing_hello):
    a_function_printing_hello()

call_print_hello(print_hello())

