
# In[1]:

from __future__ import division

# ^^ what's this about?


# In[2]:

def pretty_print_fp(x):
    print "---------------------------------------------"
    print "Floating point structure for %r" % x
    print "---------------------------------------------"
    import struct
    s = struct.pack("d", x)
    print "Hex pattern:", " ".join("%02x" % ord(i) for i in s[::-1])

    def get_bit(i):
        byte_nr, bit_nr = divmod(i, 8)
        return int(bool(
            ord(s[byte_nr]) & (1 << bit_nr)
            ))

    def get_bits(lsb, count):
        return sum(get_bit(i+lsb)*2**i for i in xrange(count))

    # https://en.wikipedia.org/wiki/Double_precision_floating-point_format

    print "Sign bit (1:negative):", get_bit(63)
    exponent = get_bits(52, 11)
    print "Exponent: %d (unshifted: %d = 0x%x)" % (exponent - 1023, exponent, exponent)
    fraction = get_bits(0, 52)
    print "Fraction:", hex(fraction)
    significand = fraction + 2**52
    print "Significand:", hex(significand)
    print "Shifted significand:", repr(significand / (2**52))


# In[3]:

pretty_print_fp(1)


# Out[3]:

#     ---------------------------------------------
#     Floating point structure for 1
#     ---------------------------------------------
#     Hex pattern: 3f f0 00 00 00 00 00 00
#     Sign bit (1:negative): 0
#     Exponent: 0 (unshifted: 1023 = 0x3ff)
#     Fraction: 0x0
#     Significand: 0x10000000000000
#     Shifted significand: 1.0
# 

# Examples to try:
# 
# - 1
# - 1+2**-52
# - 0
# - 1+2**-53
# - 1-2**-52
# - 1-2**-53
# - NaN
# - What value should we try to see a denormal?
# 
