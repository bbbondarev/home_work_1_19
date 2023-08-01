# Создать чат-бот, который отвечает на простые вопросы клиента, например, сколько время,
# какой сегодня день. Придумайте самостоятельно любые 3-5 вопросов. Кроме этого чат бот должен
# уметь выполнять вычисление простейших операций, например, 2 * 3 и др.
# Достаточно операций в одно действие.
import time
from socket import *
from time import *
my_socket = socket(AF_INET, SOCK_STREAM)
my_socket.connect(('localhost', 8011))
answer = input("Для того чтобы узнать точную дату и время - выберите 1\n"
               "Если хотите умножить 5 на 5 - выберите 2\n")
if answer == '1':
    msg = '1'
    my_socket.send(msg.encode('UTF-8')) # отправили серверу набор байт с информацией
    answer = my_socket.recv(100000) # получение данных с указанием объема
    print('Точная дата и время:', answer.decode('UTF-8'))
    my_socket.close()
if answer == '2':
    msg = '5,5'
    my_socket.send(msg.encode('UTF-8')) # отправили серверу набор байт с информацией
    answer = my_socket.recv(100000) # получение данных с указанием объема
    print('Сообщение от сервера:', answer.decode('UTF-8'))
    my_socket.close()