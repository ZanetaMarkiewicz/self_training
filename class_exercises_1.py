# https://www.w3resource.com/python-exercises/class-exercises/
# Write a Python class to convert an integer to a roman numeral


class Conversion:

    def int2roman(num):
        num_map = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX",
                   5: "V", 4: "IV", 1: "I"}
        roman = ''
        while num > 0:
            for k, v in num_map.items():
                while num >= k:
                    roman += v
                    num -= k
        return roman


print(Conversion.int2roman(4000))
