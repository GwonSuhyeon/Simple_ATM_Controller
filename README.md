# Simple_ATM_Controller
Implemented and tested simple ATM controller.

## Requirement
- Python (Tested at version 3.9.18)

## Installation
First, clone the repository :
```
git clone https://github.com/GwonSuhyeon/Simple_ATM_Controller.git
```
Second, change directory :
```
cd Simple_ATM_Controller
```
## Run
```
python run_controller.py
```
Test Case (Test Code) :
```
Please insert your card (y/n) : y

Please input your pin number (only number 0~9) : 12345

1. 100-1234-56789
2. 100-2233-99999
Please select your account (only list number) : 1

0. exit
1. balance check
2. deposit
3. withdraw
Please select the task you want (only list number) : 1

100-1234-56789 current balance : USD2,024

0. exit
1. balance check
2. deposit
3. withdraw
Please select the task you want (only list number) : 2

100-1234-56789 current balance : USD2,024
Please enter the amount to be deposited (only number 0~9) : 1000
100-1234-56789 new balance : USD3,024

0. exit
1. balance check
2. deposit
3. withdraw
Please select the task you want (only list number) : 3

100-1234-56789 withdrawable amount : USD3,024
Please enter the amount to be withdrawn (only number 0~9) : 500
100-1234-56789 new balance : USD2,524

0. exit
1. balance check
2. deposit
3. withdraw
Please select the task you want (only list number) : 1

100-1234-56789 current balance : USD2,524

0. exit
1. balance check
2. deposit
3. withdraw
Please select the task you want (only list number) : 0
Exit
```
