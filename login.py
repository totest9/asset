import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # 使用ttk模块增强样式

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("用户登录")  # 设置窗口标题
        self.root.geometry("400x300")  # 初始窗口大小
        self.root.resizable(False, False)  # 禁止调整窗口大小
        self.center_window()  # 窗口居中显示

        # 布局设置
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        for i in range(5):
            self.root.rowconfigure(i, weight=1)

        # 标题
        self.title_label = tk.Label(
            root,
            # text="用户登录",
            font=('微软雅黑', 20, 'bold'),  # 字体样式
            fg='#333',  # 文字颜色
            bg='#f0f0f0',  # 背景颜色
            padx=20,  # 内边距
            pady=10
        )
        self.title_label.grid(
            row=0, column=0, columnspan=3,  # 跨三列
            sticky='ew'  # 东西方向扩展
        )

        # 用户名输入框
        self.username_var = tk.StringVar()
        self.username_var.set("请输入用户名")
        self.username_entry = tk.Entry(
            root,
            textvariable=self.username_var,
            font=('微软雅黑', 12),
            bg='#f8f8f8',  # 输入框背景色
            bd=0,  # 无边框
            insertbackground='black'  # 光标颜色
        )
        self.username_entry.bind(
            "<FocusIn>",
            self.clear_placeholder_username  # 聚焦时清除占位符
        )
        self.username_entry.bind(
            "<FocusOut>",
            self.restore_placeholder_username  # 失焦时恢复占位符
        )
        self.username_entry.grid(
            row=1, column=0, columnspan=3,
            padx=20, pady=5, sticky='ew'
        )

        # 密码输入框
        self.password_var = tk.StringVar()
        self.password_var.set("请输入密码")
        self.password_entry = tk.Entry(
            root,
            textvariable=self.password_var,
            font=('微软雅黑', 12),
            bg='#f8f8f8',
            bd=0
        )
        self.password_entry.bind(
            "<FocusIn>",
            self.clear_placeholder_password
        )
        self.password_entry.bind(
            "<FocusOut>",
            self.restore_placeholder_password
        )
        self.password_entry.grid(
            row=2, column=0, columnspan=3,
            padx=20, pady=5, sticky='ew'
        )

        # 登录按钮
        self.login_btn = tk.Button(
            root,
            text="登录",
            command=self.check_login,
            bg='#87CEEB',  # 淡蓝色背景
            fg='white',  # 文字颜色
            font=('微软雅黑', 12),
            relief='flat',  # 平面样式
            activebackground='#6495ED',  # 悬停背景色
            bd=0,  # 无边框
            padx=20, pady=10
        )
        self.login_btn.grid(
            row=3, column=0, columnspan=2,
            padx=20, pady=10, sticky='ew'
        )
        self.login_btn.bind(
            "<Enter>",
            lambda e: e.widget.config(bg='#6495ED')  # 鼠标进入改变颜色
        )
        self.login_btn.bind(
            "<Leave>",
            lambda e: e.widget.config(bg='#87CEEB')  # 鼠标离开恢复颜色
        )

        # 退出按钮
        self.exit_btn = tk.Button(
            root,
            text="退出",
            command=root.quit,
            bg='#87CEEB',
            fg='white',
            font=('微软雅黑', 12),
            relief='flat',
            activebackground='#6495ED',
            bd=0,
            padx=20, pady=10
        )
        self.exit_btn.grid(
            row=3, column=2,
            padx=20, pady=10, sticky='ew'
        )
        self.exit_btn.bind(
            "<Enter>",
            lambda e: e.widget.config(bg='#6495ED')
        )
        self.exit_btn.bind(
            "<Leave>",
            lambda e: e.widget.config(bg='#87CEEB')
        )

    def center_window(self):
        """将窗口居中显示"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 400
        window_height = 300
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def clear_placeholder_username(self, event):
        """清除用户名输入框的占位符"""
        if self.username_var.get() == "请输入用户名":
            self.username_var.set("")
            self.username_entry.config(fg='black')

    def restore_placeholder_username(self, event):
        """恢复用户名输入框的占位符"""
        if self.username_var.get() == "":
            self.username_var.set("请输入用户名")
            self.username_entry.config(fg='gray')

    def clear_placeholder_password(self, event):
        """清除密码输入框的占位符"""
        if self.password_var.get() == "请输入密码":
            self.password_var.set("")
            self.password_entry.config(fg='black', show='*')  # 显示密码为*

    def restore_placeholder_password(self, event):
        """恢复密码输入框的占位符"""
        current_text = self.password_var.get()
        if current_text == "请输入密码" or current_text == "":
            self.password_var.set("请输入密码")
            self.password_entry.config(fg='gray', show='')
        else:
            self.password_entry.config(show='*')

    def check_login(self):
        """验证登录信息"""
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        # 检查是否为占位符文本
        if username == "请输入用户名" or password == "请输入密码":
            messagebox.showerror("错误", "请输入用户名和密码")
        elif username == "admin" and password == "123456":
            messagebox.showinfo("提示", "登录成功！")
        else:
            messagebox.showerror("错误", "用户名或密码错误")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()