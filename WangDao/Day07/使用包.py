import wd_message
"""
包中的_init__.py文件控制包内的文件是否可见
"""
wd_message.send_message.send()
txt = wd_message.receive_message.receive()
print(txt)
