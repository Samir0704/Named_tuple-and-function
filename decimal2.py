from math import ceil, floor
# print(floor(4.999))  # -> o'zidan kichik songa (chap tomonga) yaxlitlaydi
# print(ceil(9.0000000000001))  # ->  o'zidan katta songa (o'ng tomonga) yaxlitlaydi
# print(round(11.5))#-> agar (0.5) holatlarda o'ng tomonga yaxlitlaydi
#

# from decimal import Decimal
# Pul hisob-kitobining aniq natijasini hisoblash
# price = Decimal('19.99')
# tax_rate = Decimal('0.07')
# total = price * (1 + tax_rate)
# print(total)


from decimal import Decimal
# # Hisoblash natijasini `float` va `Decimal` bilan solishtirish
# x = 0.1 + 0.1 + 0.1
# y = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
# print(x == 0.3)
# print(y == Decimal('0.3'))