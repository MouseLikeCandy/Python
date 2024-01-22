# 等待输入
name = input('请输入您的姓名：')
# 通过f-string方法格式化字符串并通过print方法输出字符串
print(f'{name}, 欢迎回来')


# 简单的机器人聊天程序
print('你好，我是机器人小A')

# 无限循环，会一直执行
while True:
    question = input('我：')
    answer = question.replace('吗？', '')
    print(answer)
