# 导入tkinter模块，用于创建图形用户界面
import tkinter as tk

# 创建一个主窗口对象
window = tk.Tk()

# 设置窗口标题
window.title("消费税计算器")

# 设置窗口大小
window.geometry("500x500")

# 创建一个标签，显示欢迎信息
label_welcome = tk.Label(window, text = "欢迎使用消费税计算器！", font = ("Arial", 16))
# 将标签放置在窗口的上方
label_welcome.pack()

# 创建一个标签，显示提示信息
label_prompt = tk.Label(window, text = "请输入您的消费金额（元）：", font = ("Arial", 12))
# 将标签放置在窗口的中间
label_prompt.pack()

# 创建一个输入框，用于接收用户输入的消费金额
entry_amount = tk.Entry(window, font = ("Arial", 12))
# 将输入框放置在窗口的中间
entry_amount.pack()
# 绑定输入框的获得焦点事件，显示按键输入框架
entry_amount.bind("<Key>", lambda event: on_key_pressed(event))

# 创建一个函数，用于判断按键事件的键值
def on_key_pressed(event):
    # 如果按键事件的键值是回车键
    if event.keysym == "Return":
        # 调用计算消费税的函数，并传递事件对象作为参数
        calculate_tax(event)
    # 否则
    else:
        # 显示按键输入框架
        frame_input.pack()


# 创建一个按钮，用于触发计算消费税的函数
button_calculate = tk.Button(window, text = "计算消费税", font = ("Arial", 12),
                             command = lambda: calculate_tax(None))
# 将按钮放置在窗口的中间
button_calculate.pack()

# 创建一个标签，用于显示计算结果
label_result = tk.Label(window, text = "", font = ("Arial", 12))
# 将标签放置在窗口的下方
label_result.pack()

# 创建一个列表，用于存储用户的消费记录
record_list = []


# 创建一个函数，用于根据用户输入的消费金额计算对应的消费税率和消费税金额
# 创建一个函数，用于根据用户输入的消费金额计算对应的消费税率和消费税金额
def calculate_tax(event):
    # 如果事件对象不为空
    if event:
        # 从事件对象的控件属性中获取用户输入的消费金额
        amount = event.widget.get()
    # 否则
    else:
        # 从输入框中获取用户输入的消费金额
        amount = entry_amount.get()
    # 将用户输入的消费金额转换为浮点数
    amount = float(amount)
    # 定义一个字典，存储消费金额和消费税比例的对应关系
    tax_rate_dict = {10: 0.1, 20: 0.2, 40: 0.3, 80: 0.4, 100: 0.5, 150: 0.6, 200: 0.7, 250: 0.8, 500: 0.9, 1000: 1}
    # 定义一个变量，存储消费税率
    tax_rate = 0
    # 遍历字典，找到消费金额对应的消费税比例
    for key in tax_rate_dict:
        # 如果消费金额小于等于字典中的某个键值，说明找到了对应的消费税比例
        if amount <= key:
            # 将消费税比例赋值给变量
            tax_rate = tax_rate_dict[key]
            # 跳出循环
            break
    # 如果消费金额大于1000，消费税比例为消费金额乘以0.001
    if amount > 1000:
        tax_rate = amount * 0.001
    # 计算消费税金额，保留两位小数
    tax_amount = round(amount * tax_rate, 2)
    # 将消费金额和消费税金额添加到消费记录列表中
    record_list.append((amount, tax_amount))
    # 定义一个变量，存储消费总额
    total_amount = 0
    # 定义一个变量，存储消费税总额
    total_tax = 0
    # 遍历消费记录列表，累加消费总额和消费税总额
    for record in record_list:
        total_amount += record[0]
        total_tax += record[1]
    # 生成计算结果的字符串，包括当前消费金额对应的消费税率、消费税金额，以及消费总额和消费税总额
    result = "您的消费金额为{0:.2f}元\n消费税率为{1:.2f}\n消费税金额为{2:.2f}元。\n\n您的消费总额为{3:.2f}元\n消费税总额为{4:.2f}元".format(
        amount, tax_rate, tax_amount, total_amount, total_tax)
    # 将计算结果显示在标签上
    label_result.config(text = result)
    # 清空输入框内的数字
    entry_amount.delete(0, tk.END)



# 创建一个按键输入框架，用于显示数字键盘
frame_input = tk.Frame(window)
# 将按键输入框架放置在窗口的下方
frame_input.pack()

# 创建一个列表，存储数字键的文本
number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]

# 创建一个循环，用于生成数字键
for i in range(11):
    # 创建一个按钮，用于显示数字键的文本
    button_number = tk.Button(frame_input, text = number_list[i], font = ("Arial", 12),
                              command = lambda x = number_list[i]: add_number(x))
    # 将按钮放置在按键输入框架中的合适位置
    if i < 10:
        button_number.grid(row = i // 3, column = i % 3, padx = 10, pady = 10)
    else:
        button_number.grid(row = 3, column = 1, padx = 10, pady = 10)

# 创建一个按钮，用于清除输入框中的数字
button_clear = tk.Button(frame_input, text = "清除", font = ("Arial", 12),
                         command = lambda: clear_number())
# 将按钮放置在按键输入框架中的合适位置
button_clear.grid(row = 4, column = 0, padx = 10, pady = 10)

# 创建一个按钮，用于确认输入框中的数字，并触发计算消费税的函数
button_confirm = tk.Button(frame_input, text = "确认", font = ("Arial", 12),
                           command = lambda: confirm_number())
# 将按钮放置在按键输入框架中的合适位置
button_confirm.grid(row = 4, column = 1, columnspan = 2, padx = 10, pady = 10, sticky = tk.E + tk.W)

# 创建一个函数，用于将数字添加到输入框中
def add_number(number):
    # 获取输入框中的原有内容
    original = entry_amount.get()
    # 在原有内容的末尾添加新的数字
    new = original + number
    # 将新的内容显示在输入框中
    entry_amount.delete(0, tk.END)
    entry_amount.insert(0, new)

# 创建一个函数，用于清空输入框中的数字
def clear_number():
    # 将输入框中的内容全部删除
    entry_amount.delete(0, tk.END)

# 创建一个函数，用于确认输入框中的数字，并触发计算消费税的函数
def confirm_number():
    # 调用计算消费税的函数
    calculate_tax(entry_amount.get())
    # 隐藏按键输入框架
    frame_input.pack_forget()


# 启动主窗口的循环
window.mainloop()
