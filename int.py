num = 10


#-----------------------
#bit_length() = Returns the number of bits required to represent an integer in binary,
#excluding the sign and leading zeros.
#-----------------------
print(num.bit_length())

#----------------------------
#bit_count() = Returns the number of 1s in the binary representation of an integer.
#----------------------------

print(num.bit_count())

#---------------------
#num.to_bytes() = Converts an integer into bytes.
#---------------------
num = 65
result = num.to_bytes(2, byteorder="big")
print(result)

#------------------
#int.from_bytes() = Converts bytes into an integer.
#------------------
data = b'\x00A'

result = int.from_bytes(data, byteorder="big")

print(result)

#-------------------
#as_integer_ratio() = Returns the integer as a fraction (numerator, denominator).
#-------------------
num = 25

print(num.as_integer_ratio())
