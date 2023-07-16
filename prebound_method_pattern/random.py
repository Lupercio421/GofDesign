from datetime import datetime

_seed = datetime.now().microsecond % 255 + 1

def set_seed(value):
    global _seed
    _seed = value

def random():
    global _seed
    _seed, carry = divmod(_seed, 2)
    if carry:
        _seed ^= 0xb8
    return _seed

#Problems with this approach
## impossible to ever instantiate a second copy of this random number generator
## difficult to decouple your random number generator tests from each other if the gnerator's state is global
## this approach abandons encapsulation and can detract from readability

