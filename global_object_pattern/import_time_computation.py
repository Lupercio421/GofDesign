INFINITY = float('inf')
print(INFINITY)

# COPY_BUFSIZE = 1024 * 1024 if _WINDOWS else 16 * 1024

def _f(): pass

FunctionType = type(_f)
print(FunctionType)