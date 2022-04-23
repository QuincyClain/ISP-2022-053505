import types

co_list = ( 
    'co_argcount',
    'co_kwonlyargcount',
    'co_nlocals',
    'co_stacksize',
    'co_flags',
    'co_code',
    'co_consts',
    'co_names',
    'co_varnames',
    'co_filename',
    'co_name',
    'co_firstlineno',
    'co_lnotab',
    'co_freevars',
    'co_cellvars'
    )
    

def serialize(obj):
    my_dict = {}
    if isinstance(obj, bool):
        return bool(obj)
    elif isinstance(obj, (int, float, str)):
        return obj
    elif isinstance(obj, tuple):
        key = 'tuple'
        temp = []
        for i in obj:
            temp.append(serialize(i))
        my_dict[key] = temp
    elif isinstance(obj, list):
        key = 'list'
        temp = []
        for i in obj:
            temp.append(serialize(i))
        my_dict[key] = temp
    elif isinstance(obj, dict):
        key = 'dict'
        temp = {}
        for obj_key, val in obj.items():
            temp[serialize(obj_key)] = serialize(val)
        my_dict[key] = temp
    elif isinstance(obj, bytes):
        key = 'bytes'
        my_dict[key] = obj.hex()
    elif isinstance(obj, types.FunctionType):
        key = 'func'
        my_dict[key] = serialize(obj.__code__)
    elif isinstance(obj, types.CodeType):
        key = 'code'
        temp = {}
        sorted_list = list()
        my_list = dir(obj)
        for item in my_list:
            if item.startswith('_'):
                continue
            else:
                sorted_list.append(item)
        for attr in sorted_list:
            temp[attr] = serialize(obj.__getattribute__(attr))
        my_dict['code'] = temp
    return my_dict


def deserialize(serialized_obj):
    my_dict = {}
    if isinstance(serialized_obj, dict):
        for key, val in serialized_obj.items():
            if key == 'func':
                import __main__
                globals().update(__main__.__dict__)
                def func(): ...
                func.__code__ = deserialize(val)
                return func
            elif key == 'code':
                temp = []
                for co_item in co_list:
                    if isinstance(deserialize(val[co_item]), list):
                        temp.append(tuple(deserialize(val[co_item])))
                    else:
                        temp.append(deserialize(val[co_item]))
                temp_tuple = tuple(temp)
                return types.CodeType(*temp_tuple)
            elif key == 'bytes':
                return bytes.fromhex(val)
            elif isinstance(val, (int, float, str)):
                return val
            elif key == 'dict':
                return val
            elif key == 'tuple':
                my_list = []
                for i in val:
                    my_list.append(deserialize(i))
                my_tuple = tuple(my_list)
                my_dict[deserialize(key)] = my_tuple
                return my_tuple
            elif isinstance(val, list):
                my_list = []
                for i in val:
                    my_list.append(deserialize(i))
                my_dict[deserialize(key)] = my_list
            else:
                my_dict[deserialize(key)] = deserialize(val)
    elif isinstance(serialized_obj, list):
        my_list = []
        for item in serialized_obj:
            my_list.append(deserialize(item))
        return my_list
    elif isinstance(serialized_obj, tuple):
        my_tuple_list = []
        for item in my_tuple_list:
            my_tuple_list.append(deserialize(item))
        my_tuple = tuple(my_tuple_list)
        return my_tuple
    elif isinstance(serialized_obj, (bool, int, float, str)):
        return serialized_obj
    return my_dict
            

        