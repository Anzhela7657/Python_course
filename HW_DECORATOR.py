#1.Write a decorator that ensures a function is only called by users with a specific role.
def is_admin(func):
    def wrapper(*args, **kwargs):
        user_type = kwargs.get('user_type')
        match user_type:
            case 'admin':
                return func(*args, **kwargs)
            case _:
                raise ValueError('Permission denied')
    return wrapper
@is_admin
def show_customer_receipt(user_type: str):
    print("Showing customer receipt...")
show_customer_receipt(user_type='admin')
#2.
def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            error = f"Found 1 error during execution of your function: KeyError no such key as {e}"
            print(error)
    return wrapper
@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])

some_function_with_risky_operation({'foo': 'bar'})

