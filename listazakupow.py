shops = { 'piekarnia': ['Chleb ' , 'Pączek ' , 'Bułka ' ], 'warzywniak' : [ 'Marchew ' , 'Seler ' , 'Rukola ']       
}

for key, value in shops.items():
        print (f'Idę do sklepu {key} i kupuję tu następujące rzeczy: {value}')

ctr = sum(map(len, shops.values()))
print("W sumie kupuję ",ctr, "produktów" )
