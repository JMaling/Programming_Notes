period = "B"

# parameters are inputs to the function
# they are assigned locally (scope)


def hello(name = "Parker"):  # this sets a default name for the program, which will print if you do not specify one
    '''
    Says hello to the name, and introduces itself as your module
    :param name: Name
    :return: None
    '''
    print("Hello There")
    print("I Am Your Module")
    print("Hello There,", name, ".")


def product_sum(n1, n2):
    '''
    The product and sum of two numbers
    :param n1: Number 1
    :param n2: Number 2
    :return: None
    '''
    product = n1 * n2
    sum = n1 + n2
    return product, sum


if __name__ == "__main__":
    print("Hello B Period!")
    print(product_sum(4, 5))
