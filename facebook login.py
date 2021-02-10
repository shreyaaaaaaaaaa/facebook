from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from getpass import getpass

driver = webdriver.Chrome(executable_path= "D:\Drivers\chromedriver")

driver.get("https://www.facebook.com/")
print('Welcome to Facebook!')
sleep(5)


user = input('Enter Email ID: ')
print("Email Id has been successfully entered by the user")
password =input('Enter password: ')
print("Password has been entered by the user")


username_value = driver.find_element_by_id('email')
username_value.send_keys(user)


password_value = driver.find_element_by_id('u_0_b')
password_value.send_keys(password)


print ("Done")
input('Press anything to quit')
driver.quit()




