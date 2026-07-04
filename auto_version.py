import re
import os

# App ki build.gradle file ka path
filepath = 'mobile/android/app/build.gradle' 

if not os.path.exists(filepath):
    print("Error: build.gradle file nahi mili! Check your project structure.")
    exit()

with open(filepath, 'r') as file:
    content = file.read()

# 1. Version Code ko +1 karne ka function
def increment_code(match):
    current_code = int(match.group(1))
    new_code = current_code + 1
    print(f"[OK] Version Code updated: {current_code} -> {new_code}")
    return f"versionCode {new_code}"

# 2. Version Name (Patch) ko +1 karne ka function (e.g. 1.0.1 se 1.0.2)
def increment_name(match):
    parts = match.group(1).split('.')
    if len(parts) == 3:
        major, minor, patch = parts
        new_patch = int(patch) + 1
        new_version = f"{major}.{minor}.{new_patch}"
        print(f"[OK] Version Name updated: {match.group(1)} -> {new_version}")
        return f'versionName "{new_version}"'
    return match.group(0)

# Code mein purane numbers dhoond kar naye numbers se replace karna
content = re.sub(r'versionCode\s+(\d+)', increment_code, content)
content = re.sub(r'versionName\s+"(\d+\.\d+\.\d+)"', increment_name, content)

# File ko wapis save karna
with open(filepath, 'w') as file:
    file.write(content)

print("Version automatically update ho gaya hai! Ab aap naya APK bana sakte hain.")
