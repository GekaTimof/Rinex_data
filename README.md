# О системе
Система состоит из загрузчика данных, сервера, имитирующего поток данных в реальном времени, брокера и клиента.
[Архитектура системы](https://drive.google.com/file/d/1ccF2m9qk55W5cU35HN8JWhvvj8k0Ixh4/view?usp=sharing)

![Архитектура системы](https://github.com/GekaTimof/Rinex_data/tree/master/illustrations/Frame1.png)


# cron setings to get data

comand 
~/$ crontab -e

text for cron
24 20 * * * cd /home/evgeniy/PycharmProjects/Rinex_data/Get_data && python3 get_data_demon.py
