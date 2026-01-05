def display(a,*args, **kwargs):
    print("positional arguments:",a)
    print("arbitrary arguents:",args)
    print("keywords arguments:",kwargs)
display(1,2,3,name="nikhil",age=20)    