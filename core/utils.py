def generate_prefix(app_prefix=None, func):
    if not app_prefix:
        raise ValueError("Must provide an string for app_prefix")
    def wrapper(*args, **kwargs):
        args_list = list(args)
        args_list[0] = str(app_prefix) + '/' + args_list[0]
        new_args = tuple(args_list)
        print(new_args)
        if 'distill_file' in kwargs.keys():
            print(kwargs['distill_file'])
        return func(*args, **kwargs)
    return wrapper

