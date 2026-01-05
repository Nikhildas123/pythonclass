x=10
def outer_function():
    x=5
    print(x)
    def inner_function():
        x=2
        # print(x)
    inner_function()
outer_function()
print(x)  