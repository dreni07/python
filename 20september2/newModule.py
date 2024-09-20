from typing import Optional,Union

# def get_name(name:Optional[str] = None)->str:
#     if name:
#         return name
#     return 'Anonim'
#
# print(get_name('Dren'))

def process_value(value:Union[int,str]) -> str:
    if isinstance(value,int):
        return f'number is {value}'
    elif isinstance(value,str):
        return f'{value}'
    elif isinstance(value,float):
        return ValueError('Not A Float')

print(process_value(3.2))

def proccessAnything(vlera:str) -> str:
    return f'{vlera}'

