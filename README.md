# Hidden-Import-DLL(HID) Tool
**Hidden-Import-DLL(HID)** is a tool that scan any Portable Execuation (PE) or dll file and get all hidden DLL imports, 
Even if the malware auother used Techniques to hide DLL imports during runtime the HID tool can catch them all, HID also automaticlly save a copy from every result as Text file

# Real Example on Ransomware
This is a real example on LockBit Ransomware:

![Screenshot (407)](https://user-images.githubusercontent.com/72650499/131379700-31900b8a-5767-4399-87cc-b5040b461214.png)

We can Notice that 0 import from Kernel32.dll but let's look deeper by using **HID**:

![Screenshot (408)](https://user-images.githubusercontent.com/72650499/131379910-230f11e9-5a50-4f39-bc25-4033d410460e.png)

There are +50 hidden imports from Kernel32.dll only

# Contact With Auother 
