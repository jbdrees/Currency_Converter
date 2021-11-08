print("\n"
      "CENTRAL AMERICAN CURRENCY CONVERTER TO USD\n"
      "(Includes Mexico and Peru)"
      "\n")
print("Tip: Input 'currency' for a list of available currencies and 'quit' to end the program."
      "\n")
currency = input('Currency: ').lower()
x = "quit"


while currency != x:
    if currency == "colones":
        colones = int(input('Colones: '))
        dollars = colones / 640.40
        print(f'{colones} Colones = ${dollars}')
        currency = input('Currency: ').lower()
    elif currency == "balboas":
        balboas = int(input('Balboas: '))
        dollars = balboas / 1
        print(f'${dollars}')
        currency = input('Currency: ').lower()
    elif currency == "soles":
        soles = int(input('Soles: '))
        dollars = soles * .25
        print(f'{soles} Soles = ${dollars}')
        currency = input('Currency: ').lower()
    elif currency == "cordobas":
        cordobas = int(input('Cordobas: '))
        dollars = cordobas * .028
        print(f'{cordobas} Cordobas = ${dollars}')
        currency = input('Currency: ').lower()
    elif currency == "pesos":
        pesos = int(input('Pesos: '))
        dollars = pesos * .049
        print(f'{pesos} Pesos = ${dollars}')
        currency = input('Currency: ').lower()
    elif currency == "quetzals":
        quetzals = int(input('Quetzals: '))
        dollars = quetzals * .13
        print(f'{quetzals} Quetzals = ${dollars}')
        currency = input('Currency: ').lower()
    elif currency == "b dollars":
        b_dollars = int(input('Belize Dollars: '))
        dollars = b_dollars * .50
        print(f'{b_dollars} Belize Dollars = ${dollars}')
        currency = input('Currency: ').lower()
    elif currency == "es colones":
        es_colones = int(input('El Salvador Colones: '))
        dollars = es_colones * .11
        print(f'{es_colones} El Salvador Colones = ${dollars}')
        currency = input('Currency: ').lower()
    elif currency == "lempiras":
        lempiras = int(input('Lempiras: '))
        dollars = lempiras * .041
        print(f'{lempiras} Lempiras = ${dollars}')
        currency = input('Currency: ').lower()

# List of currencies to display
    elif currency == 'currency':
        print("\n"
              "CENTRAL AMERICA:\n"
              "\n"
              "Balboas (from Panama)\n"
              "B Dollars (from Belize)\n"
              "Colones (from Costa Rica)\n"
              "Cordobas (from Nicaragua)\n"
              "ES Colones (from El Salvador)\n"
              "Lempiras (from Honduras)\n"
              "Quetzals (from Guatemala)\n"
              "\n"
              "NORTH AMERICA:\n"
              "\n"
              "Pesos (from Mexico)\n"
              "\n"
              "SOUTH AMERICA:\n"
              "\n"
              "Soles (from Peru)\n")
        currency = input('Currency: ').lower()
    else:
        print("Please input correct currency names.\n"
              "Remember that you can pull up a list of included currencies by entering 'currency'.\n"
              "Be sure to only include the currency name as spelled prior to where the currency is from.\n"
              "For example to convert Panamanian Balboas into U.S. Dollars, input 'Balboas'.")
        currency = input('Currency: ').lower()



