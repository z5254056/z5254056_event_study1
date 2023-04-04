# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Downloads Qantas share price beginning 1 January 2020
import yfinance as df
df.download("QAN.AX", '2020-01-01', None).to_csv('qan_stk_prc.csv')

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
result = list(set(num for num in numbers if num % 2 == 0))
