# 28.1. ИТОГОВЫЙ ПРОЕКТ ПО АВТОМАТИЗАЦИИ ТЕСТИРОВАНИЯ (PJ-04)

# Итоговый проект по автоматизации тестирования
В рамках выполнения дипломного проекта вам предстоит протестировать новый интерфейс авторизации в личном кабинете от заказчика Ростелеком Информационные Технологии. Вам предоставили требования к сайту, внимательно ознакомьтесь с ними перед началом работы. 

→ Требования по проекту (.doc): https://docs.google.com/document/d/1dep-ZUg3bC8fFEIEmNA96mp0-Yi6o8Jo/edit?usp=share_link&ouid=116615212541011488315&rtpof=true&sd=true

→ Объект тестирования: https://b2c.passport.rt.ru

Обратите внимание, что данный сервис доступен только на территории РФ. Подумайте, каким способом вы можете подключиться к выполнению задания подобного типа, если вы находитесь в другой стране.

Заказчик передал вам следующее задание:

 1. Протестировать требования;
 2. Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна;
 3. Провести автоматизированное тестирование продукта (не менее 15 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub;
 4. Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. (если дефекты не будут обнаружены, то составить описание трех дефектов).


# Ожидаемый результат

 1. Перечислены инструменты, которые применялись для тестирования.
    Почему именно этот инструмент и эту технику.
    Что им проверялось.
    Что именно в нем сделано.

 2. К выполненному заданию прикреплены:
    Набор тест-кейсов.
    Набор автотестов на GitHub. Обратите внимание, что в репозитории должен находиться файл README.md, где будет описано, что именно проверяют данные тестовые сценарии и какие команды необходимо выполнить для запуска тестов. Описанные команды должны работать на любом компьютере с установленными Python3 и PyTest.
    Описание оформленных дефектов.
    
 3. Если что-то не получилось выполнить, то распишите детально, чтобы у нас была возможность дать обратную связь:
    Что именно не получилось?
    Как пробовали решить задачу?
    Что помешало решить?


# Результат

 1. С разработанными тест-кейсами и обнаруженными дефектами можно ознакомиться по ссылке:
    https://docs.google.com/spreadsheets/d/16JltgIVdKtq6fTDGzK8UqOQCxgmzo5EoTp0ZuVyh9fY/edit?usp=share_link
    - протестированы требования и разработаны тест-кейсы на предмет отображения в системе форм и сценариев «Авторизация», «Авторизация по коду», «Восстановление пароля», «Регистрация» - лист «Тест-кейсы»;
    - оформлено описание обнаруженных дефектов – лист «Баги».

 2. С оформленным набором автотестов можно ознакомиться на GitHub по ссылке:
    https://github.com/VladimirYanovskiy/Task-28.1.git
    
 3. Файловая структура автоматизированного проекта тестирования интерфейса авторизации в личном кабинете:
    - в корне проекта находится файл settings.py , в котором записаны валидные и не валидные данные телефона, почты, логина, лицевого счёта и пароля;
    - в корне проекта находится файл api.py , в котором находится интерфейс взаимодействия с сервисом объекта тестирования;
    - в корне проекта находится папка tests, в которой расположен пустой файл __init__.py , который используется для автоматического импорта модулей пакета;
    - в корне проекта находится папка tests, в которой расположен файл test_passport.py с автотестами проекта тестирования продукта. Все автотесты в файле test_passport.py имеют номера, которые соответствуют номеру тест-кейса. Файл test_passport.py запускается из командной строки, командой python -m pytest
