def categorize_number(n):
    categories = []
    if n % 1 == 0:
        categories.append("bulat")
    else:
        categories.append("pecahan")
    if n > 0:
        categories.append("cacah")
    if n < 0:
        categories.append("negatif")
    if n == 0:
        categories.append("nol")
    if n > 0:
        categories.append("asli")
    if n > 1:
        if n % 2 == 0:
            categories.append("genap")
        else:
            categories.append("ganjil")
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                categories.append("komposit")
                break
        else:
            categories.append("prima")
    return categories

number = int(input("Ketik angka: "))
print(categorize_number(number))
