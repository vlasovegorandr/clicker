Приложение представляет из себя простую игру-кликер, написанную на языке Python с использованием фреймворка Django 1.11, с:

	- поддержкой пользовательских аккаунтов
	
	- возможностью изменять некоторые визуальные элементы игры
	
	- таблицей рекордов пользователей
	

Открыть приложение можно перейдя по url 'http://vlasovegorandr.pythonanywhere.com/'
	

Для запуска потребуются Python3.6, Django 1.11.16.

Порядок установки (проверено на Ubuntu 16.04 LTS):

	1. Загрузить файлы приложения с github:
		'$ git clone https://github.com/vlasovegorandr/clicker'
		
	2. Установить виртуальную среду virtualenv с помощью команды
		'$ python3.6 -m venv virtualenv'
		
	3. Запустить виртуальную среду:
		'$ source virtualenv/bin/activate'
		
	4. Перейти в папку с приложением:
		'$ cd clicker/ '
		
	5. Установить требуемые библиотеки, список которых можно найти в приложенном файле 'requirements.txt':
		'$ pip install -r requirements.txt'

После этого приложение можно запустить на локальном сервере с помощью команды:
	'$ python manage.py runserver'
	
	
Открыть его в браузере можно, перейдя по url 'localhost:8000'


В файле 'accounts/tests.py' есть тесты для проверки функциональностей регистрации 
	новых пользователей и их входа в систему, для запуска которых потребуются selenium 3.14,
	установленный при выполнении шага 5, и geckodriver, найти последнюю версию которого можно
	по ссылке 'https://github.com/mozilla/geckodriver/releases'



