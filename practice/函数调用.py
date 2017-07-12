def hello_world():
    print('函数调用')
def there_hellos():
    for i in range(3):
        hello_world()

there_hellos()