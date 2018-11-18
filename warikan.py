amount = 1500
number_of_people = 3

print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")

amount = 2000
number_of_people = 3

print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")

amount = 3647
number_of_people = 4

print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")


# table1 :1500 3
# table2 : 2000 3
# table3 : 3647 4
def warikan(amout, number_of_people):
    print(f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円")


print(warikan(amount=1500, number_of_people=3))
print(warikan(amount=2000, number_of_people=3))
print(warikan(amount=3000, number_of_people=4))
