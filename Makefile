CC=python3

debug_db:
	$(CC) database.py postgres 111 postgres 127.0.0.1 5432

configs:
	sudo apt-get update
	sudo apt-get install python-pip
	sudo apt-get install libpq-dev python-dev
	sudo pip install psycopg2
	sudo pip install pyTelegramBotAPI
	sudo pip install telebot
	sudo pip install Pillow
	sudo pip install schedule

start_bot:
	sudo systemctl daemon-reload
	sudo systemctl enable bot
	sudo systemctl start bot
	sudo systemctl status bot

stop_bot:
	sudo systemctl stop bot
	sudo systemctl status bot

restart_bot: 
	sudo systemctl start bot
	sudo systemctl status bot

clean:
	rm -Rfv bot_swiss