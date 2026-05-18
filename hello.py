# โค้ดสีสำหรับตกแต่ง Terminal
GREEN = "\033[92m"
ORANGE = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

# จัดช่องไฟของ ASCII Art ใหม่ให้สมดุล ไม่โย้ขวา
cat_art = f"""
      |\\___/|
      )     (
     =\     /=
       )   (
      /     \\
      )     (
     /       \\ 
    /         \\_/  
    \\__  __  __/  
       \\(  )/    
        m  m
"""

# แสดงผลแบบมีสีสันและตัวหนา
print(f"{BOLD}{GREEN}Hello World!{RESET}")
print(f"{ORANGE}{cat_art}{RESET}")