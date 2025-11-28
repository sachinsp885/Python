def read_file(file_name):
    try:
        with open(file_name,'r') as f:
            data = f.read()
            print(data)
    except Exception as e:
        print("File not found")
    finally:
        print("file has completed")

file_name='C:/Git files/My git files/Python/Python/file operation/example1.txt'
read_file(file_name)