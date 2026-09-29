n1 = float(input())       
n2 = float(input())    
n3 = float(input())  


current_fuel = n1 * (n2 / 100)

distance_left = current_fuel * n3

print(f"You can drive another {distance_left:.1f} kilometers.")

if distance_left >= 200:
    print("Next refueling after 200 kilometers.")
    print("You can wait until the next station.")
else:
    print("Next refueling after 200 kilometers.")
    print("FILL IN NOW!")