"""
Let's analyze the following snipped of code and make sure that argument passing works as
we've seen today...
"""


def change_p(p_param):
    p_param = 0
    print("In function p_param value={}".format(p_param))


p = 5
change_p(p)
print("In caller p value={}".format(p))


"""
What about a mutable type?
"""
a_list = [10, 20]
print("List before invocation={}".format(a_list))


def duplicate_last_element(input_list):
    last_el = input_list[-1]
    input_list.append(last_el)


duplicate_last_element(a_list)
print("List after invocation={}".format(a_list))