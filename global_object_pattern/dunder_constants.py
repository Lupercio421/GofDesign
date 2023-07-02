import os
import bz2
import inspect
here = os.path.dirname(__file__)
print(here)

bz2.__author__ = "Nadeem Vawda <nadeem.vawda@gmail.com>"

inspect.__author__ = ('Ka-Ping Yee <ping@lfw.org>',
              'Yury Selivanov <yselivanov@sprymix.com>')

print("bz2 author example: "+ bz2.__author__)
print("inspect author example: "+ str(inspect.__author__))