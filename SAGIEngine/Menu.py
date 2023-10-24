"""
    Copyright (c) 2023 Muhammad Shariq Ayaz
    All rights reserved.
    
    This code is the intellectual property of Muhammad Shariq Ayaz, and it is protected by
    copyright law. Unauthorized use or copying of this code, in whole or in part,
    is strictly prohibited without the express written consent of "Muhammad Shariq Ayaz".
    
    For inquiries about licensing or use of this code, please contact:
    
    Github: /shariqayaztech
    Email: gr8shariq@gmail.com
"""
import os
import time
import threading
from termcolor import colored, cprint
from dotenv import load_dotenv, set_key, get_key
# list of applications
from FlaskSRV import FlaskSRV
import multiprocessing
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Menu():

    webserver_socketio = False
    sagi_server = False

    def __init__(self, p1=None, p2=None, p3=None):
        self.run()

    def run(self):
        flask_server = FlaskSRV()
        pr = None

        while True:

            if flask_server.running_state() == True:
                self.webserver_socketio = True
            else:
                self.webserver_socketio = False

            load_dotenv()
            self.clear()
            print(colored("".center(40, " "), 'white', "on_red"))
            print(colored("SAGIENGINE CONSOLE".center(40, " "), 'white', "on_red"))
            print(colored("".center(40, " "), 'white', "on_red"))
            self.envfilechk()
            # MEMU
            self.MENU()
            input_str = input("\nKindly Enter > ")

            if input_str == "1":
                # toggle: server run | terminate
                if self.webserver_socketio is not True:
                    self.queue = multiprocessing.Queue()
                    pr = multiprocessing.Process(
                        target=FlaskSRV._run_flask, args=(self.queue,))
                    pr.start()
                    flask_server.RUNNING_STATE = True
                    time.sleep(1)
                else:
                    pr.terminate()
                    pr.join()
                    flask_server.RUNNING_STATE = False

            elif input_str == "2":
                input("\nSAGI SERVER NOT INITIALISED\n")
                
            elif input_str == "3":
                input("\nSAGI SERVER NOT INITIALISED\n")
                
            elif input_str == "0":
                if pr is not None:
                    pr.terminate()
                    pr.join()
                    flask_server.RUNNING_STATE = False
                break

    def MENU(self):
        print(
            f"[1] Webserver: SocketIO \t \033[3m{colored('Running','green', attrs=['underline']) if self.webserver_socketio==True else colored('Stopped','red', attrs=['underline','bold'])}\033[0m")
        print(
            f"    Message Broker: Redis\t \033[3m{colored('Running','green', attrs=['underline']) if self.webserver_socketio==True else colored('Stopped','red', attrs=['underline','bold'])}\033[0m")
        print(
            f"[2] SAGI Engine \t\t \033[3m{colored('Running','green', attrs=['underline']) if self.sagi_server==True else colored('Stopped','red', attrs=['underline','bold'])}\033[0m")
        print(colored("[0] Exit", 'red', attrs=['bold']))

# CHK environment variables
    def envfilechk(self):
        if not os.path.isfile('.env'):
            load_dotenv()
            print("\n")
            print(colored("Warning...\n", 'red') + "\tThe .env file not found.\n" + colored(
                "\tCreated with empty fields.", 'white', attrs=['bold'])+colored(" \u2713", 'green', attrs=['bold']))
            with open('.env', 'w') as f:
                f.write('DB_HOST=\n')
                f.write('DB_DATABASE=\n')
                f.write('DB_PORT=\n')
                f.write('DB_USER=\n')
                f.write('DB_PASSWORD=\n')
                f.write('WEBSOCKET_URL=\n')
            print("\n")

        inp_DB_HOST = os.getenv("DB_HOST")
        inp_DB_DATABASE = os.getenv("DB_DATABASE")
        inp_DB_PORT = os.getenv("DB_PORT")
        inp_DB_USER = os.getenv("DB_USER")
        inp_DB_PASSWORD = os.getenv("DB_PASSWORD")
        inp_WEBSOCKET_URL = os.getenv("WEBSOCKET_URL")

        if not inp_DB_HOST:
            inp_DB_HOST = input(
                "\nValue of key: DB_HOST not found.\n\t Kindly Enter Value of DB_HOST: ")
            set_key('.env', 'DB_HOST', inp_DB_HOST)

        if not inp_DB_DATABASE:
            inp_DB_DATABASE = input(
                "\nValue of key: DB_DATABASE not found.\n\t Kindly Enter Value of DB_DATABASE: ")
            set_key('.env', 'DB_DATABASE', inp_DB_DATABASE)

        if not inp_DB_PORT:
            inp_DB_PORT = input(
                "\nValue of key: DB_PORT not found.\n\t Kindly Enter Value of DB_PORT: ")
            set_key('.env', 'DB_PORT', inp_DB_PORT)

        if not inp_DB_USER:
            inp_DB_USER = input(
                "\nValue of key: DB_USER not found.\n\t Kindly Enter Value of DB_USER: ")
            set_key('.env', 'DB_USER', inp_DB_USER)

        if not inp_DB_PASSWORD:
            inp_DB_PASSWORD = input(
                "\nValue of key: DB_PASSWORD not found.\n\t Kindly Enter Value of DB_PASSWORD: ")
            set_key('.env', 'DB_PASSWORD', inp_DB_PASSWORD)

        if not inp_WEBSOCKET_URL:
            inp_WEBSOCKET_URL = input(
                "\nValue of key: WEBSOCKET_URL not found.\n\t Kindly Enter Value of inp_WEBSOCKET_URL: ")
            set_key('.env', 'WEBSOCKET_URL', inp_WEBSOCKET_URL)
# clean screen

    def clear(self):
        # window only | disable if mac or linux just remove blow lines and put pass instead
        os.system('cls' if os.name == 'nt' else 'clear')
