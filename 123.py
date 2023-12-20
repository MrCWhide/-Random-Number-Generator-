import tkinter as tk
from tkinter import messagebox
import random

MAX_HISTORY = 3  # 最多保留的历史记录次数

def generate_random_numbers():
    try:
        n = int(entry_n.get())
        min_val = int(entry_min.get())
        max_val = int(entry_max.get())
        allow_repeat = allow_repeat_var.get()
        clear_old_records = clear_old_records_var.get()

        if min_val > max_val:
            messagebox.showerror("错误", "最小值不能大于最大值！TMD小学生吗")
            return

        if not allow_repeat and (max_val - min_val + 1) < n:
            messagebox.showerror("错误", "范围内整数不足以生成指定次数的不同整数！你数学老师谁啊？")
            return

        random_numbers = []
        if allow_repeat:
            random_numbers = [random.randint(min_val, max_val) for _ in range(n)]
        else:
            numbers = list(range(min_val, max_val + 1))
            random_numbers = random.sample(numbers, n)

        messagebox.showinfo("随机数生成器", "嘉奖：" + ' '.join(map(str, random_numbers)))

        if clear_old_records:
            result_text.delete(1.0, tk.END)  # 清除之前的内容

        result_text.insert(tk.END, "生成的随机数：\n")
        for num in random_numbers:
            result_text.insert(tk.END, str(num) + " ")
        result_text.insert(tk.END, "\n\n")

        # 限制历史记录数量
        lines = result_text.get("1.0", tk.END).splitlines()
        if len(lines) > MAX_HISTORY * 4:  # * 4 因为每次生成会有两行内容（数字和空行）
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, '\n'.join(lines[-(MAX_HISTORY * 4):]))

    except ValueError:
        messagebox.showerror("错误", "请输入有效的整数")

# 创建主窗口
root = tk.Tk()
root.title("随机数生成器 Desinged By CWhide")

# 调整主窗口宽度和高度
root.geometry("500x500")

# Frame 1
frame1 = tk.Frame(root)
frame1.pack()

label_n = tk.Label(frame1, text="生成数量：")
label_n.grid(row=0, column=0)
entry_n = tk.Entry(frame1)
entry_n.grid(row=0, column=1)

label_min = tk.Label(frame1, text="最小值：")
label_min.grid(row=1, column=0)
entry_min = tk.Entry(frame1)
entry_min.grid(row=1, column=1)

label_max = tk.Label(frame1, text="最大值：")
label_max.grid(row=2, column=0)
entry_max = tk.Entry(frame1)
entry_max.grid(row=2, column=1)

allow_repeat_var = tk.BooleanVar()
checkbutton_allow_repeat = tk.Checkbutton(frame1, text="允许重复", variable=allow_repeat_var)
checkbutton_allow_repeat.grid(row=3, columnspan=2)

clear_old_records_var = tk.BooleanVar()
checkbutton_clear_old_records = tk.Checkbutton(frame1, text="清除旧记录", variable=clear_old_records_var)
checkbutton_clear_old_records.grid(row=4, columnspan=2)

generate_button = tk.Button(frame1, text="生成随机数", command=generate_random_numbers)
generate_button.grid(row=5, columnspan=2)

# Frame 2
frame2 = tk.Frame(root)
frame2.pack()

# 调整显示随机数的文本框大小
result_text = tk.Text(frame2, height=15, width=50)
result_text.pack()

# 运行主循环
root.mainloop()
