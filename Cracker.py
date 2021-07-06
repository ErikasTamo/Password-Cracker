import itertools
import string
import time
import os
import sys

def guess_common_passwords(password):
    with open('common_passwords.txt', 'r') as passwords:
        data = passwords.read().splitlines()
    
    for i, match in enumerate(data):
        if match == password:
            return f'''__________________________

[+] Password was Found!
Password: {match}
Attempt: #{i+1}
__________________________
                    '''
    return 0

def brute_force(password, min_len=4, max_len=9):
    start = time.time()
    attempts = 0
    chars = string.ascii_letters + string.digits
    for password_len in range(min_len, max_len):
        for guess in itertools.product(chars, repeat=password_len):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                f = open('common_passwords.txt', 'a')
                f.write(f"\n{guess}")
                return f'''
__________________________

[+] Password was Cracked!
Password: {guess}
Time: {round(time.time()-start, 2)} Seconds
Attempt: #{attempts}
__________________________
                        '''
            print(f"[{attempts}] [-] Password Failed - {guess}")

def main(password):
    common = guess_common_passwords(password)
    return brute_force(password) if common == 0 else common
try:
    os.system('cls')
    print(main(sys.argv[1]))
except:
    print("[-] No Password was Entered")