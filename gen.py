file = open("a.csv", 'w')

print("Provide number of users: ", end='')
users = int(input())

from hmac import digest
import secrets
import string
import random

name_length = 5
job_length = 10
  

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com","cisco.com"]

small_letters = string.ascii_lowercase
capital_letters = string.ascii_uppercase

letters = small_letters + capital_letters

others = '@_#!$%^&*()?><'
digits = string.digits


all = others + letters+digits

def get_random_domain():
    return random.choice(domains)

def get_random_ename(length):
    return ''.join(random.choice(small_letters) for i in range(length))

def get_random_name(length1, length2):
    f1 = secrets.choice(capital_letters)
    f2 = secrets.choice(capital_letters)
    f1 += ''.join(secrets.choice(small_letters) for _ in range(length1-1))
    f2 += ''.join(secrets.choice(small_letters) for _ in range(length2-1))
    return f1,f2

def generate_random_email():
    return get_random_ename(random.randint(5,10)) + '@' + get_random_domain()

def get_random_job(length):
    return ''.join(secrets.choice(small_letters) for _ in range(length))

def get_random_password():
    len1 = random.randint(5,20)
    len2 = random.randint(3,13)
    return ''.join(secrets.choice(all) for _ in range(len1)) + random.choice(others) + ''.join(secrets.choice(all) for _ in range(len2))

def get_random_username(length):
    return ''.join(secrets.choice(small_letters+'_') for _ in range(length))

file.write("first_name,last_name,name,job,email,username,password")

for _ in range(users):
    first_name, last_name = get_random_name(random.randint(3,7),random.randint(3,7))
    name = first_name + ' ' + last_name
    job = get_random_job(10)
    email = generate_random_email()
    username = get_random_username(random.randint(5,7))
    password = get_random_password()
    
    file.write('\n')
    file.write(first_name+','+last_name+','+name+',' + job+',' + email+','+username+','+password)
    