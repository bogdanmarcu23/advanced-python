# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Structural Pattern Matching

# Dry Clean: [garment, size, starch, same_day]
#   garments are shirt, pants, jacket, dress
#   each item is 12.95, plus 2.00 for starch
#   same day service adds 10.00 per same-day item
# Wash and Fold: [description, weight]
#   4.95 per pound, with 10% off if more than 15 pounds
# Blankets: [type, dryclean, size]
#   type is "comforter" or "cover"
#   Flat fee of 25.00
# ---
# Output:
# Order Total Price

test_orders = [
    [
        ["shirt", "L", True, False],
        ["shirt", "M", True, False],
        ["shirt", "L", False, True],
        ["pants", "M", False, True],
        ["pants", "S", False, False],
        ["pants", "S", False, False],
        ["jacket", "M", False, False],
        ["jacket", "L", False, True]
    ],
    [
        ["dress", "M", False, True],
        ["whites", 5.25],
        ["darks", 12.5]
    ],
    [
        ["shirts and jeans", 28.0],
        ["comforter", False, "L"],
        ["cover", True, "L"],
        ["shirt", "L", True, True]
    ]
]

# TODO: process each order

for order in test_orders:
    print(f"--------------------")
    total = 0
    for garment in order:
        match garment:
            case "shirt" | "pants" | "jacket" | "dress" as type, size, starch, sameday:
                print(f"Dry Clean: ({size}), {type}", "Starched" if starch is True else "", "same-day" if sameday is True else "")
                total += 12.95
                if starch:
                    total += 2
                if sameday:
                    total +=10
            case "comforter" | "cover" as type, dryclean, size:
                print(f"Blanket: ({size}), {type}", "Dry clean" if dryclean == True else "")
                total = total + 25
            case str() as description, weight:
                print(f"Wash/Fold: {description}, weight: {weight}")
                if weight < 15:
                    total = total + 4.95 * weight
                else:
                    total = total + 4.95*90/100 * weight
            case _:
                print("Invalid item format")

    print(f"Order Total: {total:.2f}")
    #print("%.2f" % a)
    print(f"--------------------")        