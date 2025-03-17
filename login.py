import tkinter as tk  # 导入Tkinter库并重命名
from tkinter import messagebox  # 导入消息框模块用于提示信息

class LoginApp:  # 创建登录界面类
    def __init__(self, root):  # 类初始化方法
        self.root = root
        self.root.title("登录界面")  # 设置窗口标题
        self.root.geometry("300x200")  # 设置窗口大小
        
        # 创建用户名标签和输入框
        self.username_label = tk.Label(root, text="用户名:", font=('Arial', 12))  # 创建标签组件
        self.username_label.place(x=50, y=50)  # 设置标签位置
        self.username_entry = tk.Entry(root, font=('Arial', 12))  # 创建输入框组件
        self.username_entry.place(x=120, y=50)  # 设置输入框位置
        
        # 创建密码标签和输入框
        self.password_label = tk.Label(root, text="密码:", font=('Arial', 12))  # 创建密码标签
        self.password_label.place(x=50, y=90)  # 设置密码标签位置
        self.password_entry = tk.Entry(root, show="*", font=('Arial', 12))  # 创建密码输入框（*隐藏密码）
        self.password_entry.place(x=120, y=90)  # 设置密码输入框位置
        
        # 创建登录按钮
        self.login_btn = tk.Button(root, 
                                  text="登录", 
                                  command=self.check_login,  # 绑定登录验证方法
                                  bg='green', 
                                  fg='white', 
                                  font=('Arial', 12))  # 设置按钮样式
        self.login_btn.place(x=70, y=140)  # 设置登录按钮位置
        
        # 创建退出按钮
        self.exit_btn = tk.Button(root, 
                                 text="退出", 
                                 command=root.quit,  # 绑定退出方法
                                 bg='red', 
                                 fg='white', 
                                 font=('Arial', 12))  # 设置按钮样式
        self.exit_btn.place(x=180, y=140)  # 设置退出按钮位置

    def check_login(self):  # 登录验证方法
        username = self.username_entry.get().strip()  # 获取用户名输入
        password = self.password_entry.get().strip()  # 获取密码输入
        
        # 验证逻辑（示例：固定用户名密码）
        if username == "admin" and password == "123456":
            messagebox.showinfo("提示", "登录成功！")  # 显示成功提示
        else:
            messagebox.showerror("错误", "用户名或密码错误")  # 显示错误提示

if __name__ == "__main__":  # 程序入口
    root = tk.Tk()  # 创建主窗口对象
    app = LoginApp(root)  # 初始化应用
    root.mainloop()  # 进入主事件循环