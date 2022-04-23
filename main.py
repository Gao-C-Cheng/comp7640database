

def main():
    string = f'''Welcome to our retail database
    choose your identity
    1.costumer
    2.supplyer
    3.exit
    Enter your value:'''
    val = input(string)
    if val==1:
        print('costumer')
    elif val==2:
        print('supplyer')
    else:
        print('exit')


if __name__ == '__main__':
    main()