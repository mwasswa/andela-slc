"""
Breakfast
print("Get the ingredients")
print("Mix the ingredients")
print("Pour into the heated pan")
print("Flip to the other side")
breakfast = "-----Yummy egg------"

print("Get the ingredients")
print("Mix the ingredients")
print("Pour into the heated pan")
print("Flip to the other side")
breakfast = "-----Yummy pancake------"
"""

def breakfast(kind,ingredients):
    out_str = ""
    for item in ingredients:
        out_str += item + ", "
    print("Get the ingredients: " + out_str)
    print("Mix the ingredients")
    print("Pour into the heated pan")
    print("Flip to the other side")
    meal = "-----Yummy " + kind + " with " + out_str + "------"
    return meal

print(breakfast("egg",['rolex','test', 'test']))
print(breakfast("pancake",['rolex','test', 'test']))
