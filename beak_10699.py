from datetime import datetime

now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
print(date_str)