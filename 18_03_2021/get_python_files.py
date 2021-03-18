import os
import re
for i in os.listdir():
    if re.findall(".py", i) == ['.py']:
        print(i)
