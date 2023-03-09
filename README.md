# sportShop

This project containes two seperate projects inside the **projects** directory:

**sportShop** directory is a backend API created with **Python Django REST** frame work.

**sportShopBot** directory is a **telegram bot** created with **Pyrogram** library in Python.
This telergam bot communicates with end points from the backend project.
It also has a rich ui.

The backend API project is aimed to handle a sport shop **management** dashboard in Python; While the Telegram bot serves as a ui to save the sport products in to the database.

The backend API also has a celery task which publishes products in the user`s **Instagram** page every day at specific times.
