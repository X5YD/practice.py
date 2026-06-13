numbers = [numb for numb in range(1, 21)]

cat = {"even_numbers" : [numb for numb in numbers if numb % 2 == 0],
       "odd_numbers" : [numb for numb in numbers if numb % 2 == 1],
       "positive_numb" : [numb for numb in numbers if numb >= 0],
       "negative_numb" : [numb for numb in numbers if numb < 0]}

for key, value in cat.items():
    print(f"{key: <20} : {value}")