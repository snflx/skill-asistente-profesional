from db import get_conn

def main():
    # TODO: validar entradas del usuario
    conn = get_conn()
    print('running')

if __name__ == '__main__':
    main()
