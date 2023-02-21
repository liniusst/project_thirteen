admins_db = ['Linas', 'Antanas', 'Tomas']

def check(name: str) -> str:
    if name in admins_db:
        print(f'Welcome admin: {name}')
    else:
        print('Access denied! We cant found admin with this name')