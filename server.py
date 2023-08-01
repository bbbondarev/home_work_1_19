from socket import *
import time

my_socket = socket(AF_INET, SOCK_STREAM) # создали объект сокет, работающий по протоколу TCP
my_socket.bind(("", 8011)) # настроили сокет так, чтобы он принимал запросы
# по локальному IP: 127.0.0.1 и по порту 8010
my_socket.listen(5) # переходим в режим ожидания запроса (допускаем максимум 5 запросов одновременно)
while True:
    client, addr = my_socket.accept() # принимаем запрос на соединение
    data = client.recv(100000) # получили данные от клиента
    ans = data.decode('UTF-8')
    if ans == '1':
        print(f"Получен запрос на коннект по адресу: {str(addr)}")
        answer = time.ctime() + "\n" # информация для клиента о времени коннекта к серверу
        client.send(answer.encode('UTF-8')) # преобразовали строковый ответ в байты и отправляем ответ клиентк
        client.close() # завершили работу с клиентом
    if ans == '5,5':
        nums = ans.split(",")
        res = int(nums[0]) * int(nums[1])
        answer = f'Произведение = {res}'
        client.send(answer.encode('UTF-8'))
        print('Сервер решил задачу и отправил ответ клиенту')
        my_socket.close()