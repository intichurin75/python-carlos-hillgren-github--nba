listan = ["London","banan","handen","kon","kille","armen","Rom"]
#listan.pop(2)
print(type(listan[4]))
if "London" in listan:
    print(f"yepp, {listan[0]}  finns i listan")
    print()

print(f"första loopen: ")
for i in range(len(listan)):
    print(listan[i])
print()
print("andra loopen: ")
for element in listan:
    print(element)
print()
print("tredje loopen: ")
i = 0
while i < len(listan):
    print(listan[i])
    i = i +1
print()
print("fjärde loopen: ")
[print(x) for x in listan]
print()
print("femte loopen med ny lista")
nyaListan = []
for x in listan:
    if "a" in x:
        nyaListan.append(x)

print(nyaListan)
print()
print("sjätte loopen med skapa en ny lista")
nListan = [x for x in listan if "n" in x]
print(nListan)
print()
print()

priser = {"äpple": 29,"bananer": 24,"apelsiner":19,"vindruvor": 29}
priser_bananer = priser["bananer"]
print("hela lexikonet: ",priser)
print(f"Bananpris: {priser_bananer} kr/kg" )