

"""
Write a Python program to get OS name, platform and release information.
"""

import sys
import os
import platform

a = os.name
print("OS name : ", a)

platform_type = platform.system()
print("platform_type : ", platform_type)

release_info = platform
print("release information :", platform.release())

x = sys.platform
print("platform : ", x)
