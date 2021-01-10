shops = { 'piekarnia': ['Chleb ' , 'Pączek ' , 'Bułka ' ], 'warzywniak' : [ 'Marchew ' , 'Seler ' , 'Rukola ']       
}

for key, value in shops.items():
        print (f'Idę do sklepu {key} i kupuję tu następujące rzeczy: {value}')

ctr = sum(map(len, shops.values()))
print("W sumie kupuję ",ctr, "produktów" )





for i in range(1,100):
       if i % 5 == 0: 
        print(i, "jest podzielne przez 5")
        print(i**3 ,"jest szescianem liczby", i )
