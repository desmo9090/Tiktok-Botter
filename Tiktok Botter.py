from colorama import init
init()
from colorama import Fore
import os
import time
from selenium import webdriver, common
import re
import asyncio

def execute(VIDEO_URL):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disables logging
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(800, 660)
    driver.get('https://vipto.de/')
    print(f"{Fore.MAGENTA}[!] Solve the captcha.{Fore.RESET}")
    done = 0
    while True:
            name = "Followers"
            continue1 = True
            while True:
                try:
                    driver.find_element_by_xpath(
                        '//*[@id="main"]/div/div[1]/div/button'
                    ).click()
                except (
                    common.exceptions.NoSuchElementException,
                    common.exceptions.ElementClickInterceptedException
                ):
                    time.sleep(5)
                    continue
                except (
                    common.exceptions.ElementNotInteractableException
                ):
                    print(f"{Fore.RED}[!] Skipped {name} due to an unsolvable, most-likely temporary error.{Fore.RESET}")
                    continue1 = False
                    break
                break

            try:
              driver.find_element_by_xpath(
                  '//*[@id="sid"]/div/form/div/input'
              ).send_keys(VIDEO_URL)
            except (
                common.exceptions.NoSuchElementException,
                common.exceptions.ElementClickInterceptedException
            ):
                time.sleep(5)
                continue
            except (
                common.exceptions.ElementNotInteractableException
            ):
                print(f"{Fore.RED}[!] Skipped {name} due to an unsolvable, most-likely temporary error.{Fore.RESET}")
                continue1 = False
            else:
              pass

            if continue1:
              while True:
                  try:
                      driver.find_element_by_xpath(
                          '//*[@id="sid"]/div/form/div/div/button'
                      ).click()
                  except (
                      common.exceptions.NoSuchElementException,
                      common.exceptions.ElementClickInterceptedException
                  ):
                      time.sleep(5)
                      continue
                  else:
                      print(f"{Fore.LIGHTBLACK_EX}Attempting to send {name.lower()} to the video...{Fore.RESET}")
                      break

              while True:
                  try:
                      driver.find_element_by_xpath('//*[@id="sid"]/div/form/div/div/button').click()
                      driver.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()
                  except (
                      common.exceptions.NoSuchElementException,
                      common.exceptions.ElementClickInterceptedException
                  ):
                      time.sleep(5)
                      continue
                  else:
                      print(f"{Fore.GREEN}[!] Followers Have Been Sent Successfully!{Fore.RESET}")
                      
                      driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                      break
            # Views
            name = "Views"
            continue2 = True
            while True:
                try:
                    driver.find_element_by_xpath(
                        '//*[@id="main"]/div/div[4]/div/button'
                    ).click()
                except (
                    common.exceptions.NoSuchElementException,
                    common.exceptions.ElementClickInterceptedException
                ):
                    time.sleep(5)
                    continue
                except (
                    common.exceptions.ElementNotInteractableException
                ):
                    print(f"{Fore.RED}[!] Skipped {name} due to an unsolvable, most-likely temporary error.{Fore.RESET}")
                    continue2 = False
                    break
                break
            try:
              driver.find_element_by_xpath(
                  '//*[@id="sid4"]/div/form/div/input'
              ).send_keys(VIDEO_URL)
            except (
                common.exceptions.NoSuchElementException,
                common.exceptions.ElementClickInterceptedException
            ):
                time.sleep(5)
                continue
            except (
                common.exceptions.ElementNotInteractableException
            ):
                print(f"{Fore.RED}[!] Skipped {name} due to an unsolvable, most-likely temporary error.{Fore.RESET}")
                continue2 = False
            else:
              pass

            if continue2:
              while True:
                  try:
                      driver.find_element_by_xpath(
                          '//*[@id="sid4"]/div/form/div/div/button'
                      ).click()
                  except (
                      common.exceptions.NoSuchElementException,
                      common.exceptions.ElementClickInterceptedException
                  ):
                      time.sleep(5)
                      continue
                  else:
                      print(f"{Fore.LIGHTBLACK_EX}Attempting to send {name.lower()} to the video...{Fore.RESET}")
                      break

              while True:
                  try:
                      driver.find_element_by_xpath('//*[@id="sid4"]/div/form/div/div/button').click()
                      driver.find_element_by_xpath('//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/div[1]/div/form/button').click()
                  except (
                      common.exceptions.NoSuchElementException,
                      common.exceptions.ElementClickInterceptedException
                  ):
                      time.sleep(5)
                      continue
                  else:
                      print(f"{Fore.GREEN}[!] Views Have Been Sent Successfully!{Fore.RESET}")
                      
                      driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                      break
            # Shares
            name = "Shares"
            continue3 = True
            while True:
                try:
                    driver.find_element_by_xpath(
                        '//*[@id="main"]/div/div[5]/div/button'
                    ).click()
                except (
                    common.exceptions.NoSuchElementException,
                    common.exceptions.ElementClickInterceptedException
                ):
                    time.sleep(5)
                    continue
                except (
                    common.exceptions.ElementNotInteractableException
                ):
                    print(f"{Fore.RED}[!] Skipped {name} due to an unsolvable, most-likely temporary error.{Fore.RESET}")
                    continue3 = False
                    break
                break
            try:
              driver.find_element_by_xpath(
                  '//*[@id="sid7"]/div/form/div/input'
              ).send_keys(VIDEO_URL)
            except (
                common.exceptions.NoSuchElementException,
                common.exceptions.ElementClickInterceptedException
            ):
                time.sleep(5)
                continue
            except (
                common.exceptions.ElementNotInteractableException
            ):
                print(f"{Fore.RED}[!] Skipped {name} due to an unsolvable, most-likely temporary error.{Fore.RESET}")
                continue3 = False
            else:
              pass

            if continue3:
              while True:
                  try:
                      driver.find_element_by_xpath(
                          '//*[@id="sid7"]/div/form/div/div/button'
                      ).click()
                  except (
                      common.exceptions.NoSuchElementException,
                      common.exceptions.ElementClickInterceptedException
                  ):
                      time.sleep(5)
                      continue
                  else:
                      print(f"{Fore.LIGHTBLACK_EX}Attempting to send {name.lower()} to the video...{Fore.RESET}")
                      break

              while True:
                  try:
                      driver.find_element_by_xpath('//*[@id="sid7"]/div/form/div/div/button').click()
                      driver.find_element_by_xpath('//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/div[1]/div/form/button').click()
                  except (
                      common.exceptions.NoSuchElementException,
                      common.exceptions.ElementClickInterceptedException
                  ):
                      time.sleep(5)
                      continue
                  else:
                      print(f"{Fore.GREEN}[!] Shares Have Been Sent Successfully!{Fore.RESET}")
                      
                      driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                      break

            # Hearts
            name = "Hearts"
            continue4 = True
            while True:
                try:
                    driver.find_element_by_xpath(
                        '//*[@id="main"]/div/div[2]/div/button/i'
                    ).click()
                except (
                    common.exceptions.NoSuchElementException,
                    common.exceptions.ElementClickInterceptedException
                ):
                    time.sleep(5)
                    continue
                except (
                    common.exceptions.ElementNotInteractableException
                ):
                    print(f"{Fore.RED}[!] Skipped {name} due to an unsolvable, most-likely temporary error.{Fore.RESET}")
                    continue4 = False
                    break
                break
            try:
              driver.find_element_by_xpath(
                  '//*[@id="sid2"]/div/form/div/input'
              ).send_keys(VIDEO_URL)
            except (
                common.exceptions.NoSuchElementException,
                common.exceptions.ElementClickInterceptedException
            ):
                time.sleep(5)
                continue
            except (
                common.exceptions.ElementNotInteractableException
            ):
                print(f"{Fore.RED}[!] Skipped {name} due to an unsolvable, most-likely temporary error.{Fore.RESET}")
                continue4 = False
            else:
              pass

            if continue4:
              while True:
                  try:
                      driver.find_element_by_xpath(
                          '//*[@id="sid2"]/div/form/div/div/button'
                      ).click()
                  except (
                      common.exceptions.NoSuchElementException,
                      common.exceptions.ElementClickInterceptedException
                  ):
                      time.sleep(5)
                      continue
                  else:
                      print(f"{Fore.LIGHTBLACK_EX}Attempting to send {name.lower()} to the video...{Fore.RESET}")
                      break
              while True:
                  try:
                      driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/div/button').click()
                      driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()
                  except (
                      common.exceptions.NoSuchElementException,
                      common.exceptions.ElementClickInterceptedException
                  ):
                      time.sleep(5)
                      continue
                  else:
                      print(f"{Fore.GREEN}[!] Hearts Have Been Sent Successfully!{Fore.RESET}")
                      
                      driver.find_element_by_xpath('/html/body/nav/ul/li/a').click()
                      break
            done += 1
            print(f"{Fore.LIGHTBLUE_EX}[!] Times ran: {done}.{Fore.RESET}")

def main():
  print(f"""{Fore.RED}_____ ___ _  _______ ___  _  __  ____   ___ _____ _____ _____ ____  
|_   _|_ _| |/ /_   _/ _ \| |/ / | __ ) / _ \_   _|_   _| ____|  _ \ 
  | |  | || ' /  | || | | | ' /  |  _ \| | | || |   | | |  _| | |_) |
  | |  | || . \  | || |_| | . \  | |_) | |_| || |   | | | |___|  _ < 
  |_| |___|_|\_\ |_| \___/|_|\_\ |____/ \___/ |_|   |_| |_____|_| \_\\
                                                                        


{Fore.BLUE}Made by P3ter.

{Fore.GREEN}[1]{Fore.RESET} Start.
{Fore.GREEN}[2]{Fore.RESET} Close.
  """)
  answer = input("> ")
  if answer == "1":
      print(f"{Fore.LIGHTBLUE_EX}What's the video URL? {Fore.RESET}")
      url = input("")
      execute(url) 
  else:
      exit()

if __name__ == "__main__":
    main()