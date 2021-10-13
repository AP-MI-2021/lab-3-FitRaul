def show_menu():
    print("1. Citire lista")
    print("2. Det cea mai lunga secv cu prop ca numerele sunt pare")
    print("3. Det cea mai lunga subsecv cu prop numerele sunt formate din cifre prime")
    print("4. Exit")

def read_list():
    lst = []
    lst_str = input ("Introduceti numerele prin spatiu:")
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst

def is_even(n):
    """
    determina daca un nr este par sau nu
    """
    if n%2==1:
        return 0
    return 1

def get_longest_all_even(lst):
    """
    determina subsecventa cea mai lunga de numere pare
    """
    l = len(lst)
    result = []
    for i in range (l):
        for j in range (i,l):
            all_even = True
            for num in lst[i:j+1]:
                if is_even(num) == False:
                    all_even = False
                    break
            if all_even:
                if j-i+1 >len(result):
                    result = lst[i:j+1]
    return result



def test_is_even():
    assert is_even(123) == False
    assert is_even(2) == True
    assert is_even(12321) == False
    assert is_even(24) == True
    assert is_even(87) == False


def prime_digits(n):
    """
    determina daca numarul e format din cifre prime
    """
    ok = 1
    copy = n
    while copy!=0:
        c=copy%10
        if c==1 or c==4 or c==6 or c==8 or c==9: ok=0
        copy=copy//10

    if ok==0:
        return 0
    return 1

def get_longest_prime_digits(lst):
    """
    determina cea mai lunga subsecv de numere formate din cifre prime
    """
    l = len(lst)
    result = []
    for i in range (l):
        for j in range (i,l):
            k = prime_digits(lst[i])
            all_prime_digits = True
            for num in lst[i:j+1]:
                if prime_digits(num) != k :
                    all_prime_digits = False
                    break
            if all_prime_digits:
                if j-i+1 >len(result):
                    result = lst[i:j+1]
    return result

def test_prime_digits():
    assert prime_digits(23) == True
    assert prime_digits(24) == False
    assert prime_digits(35) == True
    assert prime_digits(68) == False



def main():
    lst=[]
    while True:
        show_menu()
        opt = int(input("Introduceti optiunea: "))
        if opt == 1 :
            lst = read_list()
        elif opt == 2:
            print("Cea mai lunga subsecv de numere pare  este ",  get_longest_all_even(lst))
        elif opt == 3:
            numar= get_longest_prime_digits(lst)
            print("Cea mai lunga subsecv de nr formate din cifre prime  ", numar)
        elif opt == 4:
            break
        else:
            print("Optiunea invalida")

if __name__ == '__main__':
    test_is_even()
    test_prime_digits()
    main ()