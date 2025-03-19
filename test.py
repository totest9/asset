class Car:
    """
    Car类代表一个汽车对象。
    它封装了汽车的相关信息，如颜色和型号。
    """

    def __init__(self, color, model):
        """
        初始化Car对象。
        
        参数:
        color (str): 汽车的颜色。
        model (str): 汽车的型号。
        """
        self.color = color
        self.model = model

    def __str__(self):
        """
        返回Car对象的字符串表示。
        
        返回:
        str: 描述Car对象的字符串。
        """
        return f"Car(model={self.model}, color={self.color})"


# 创建一个Car对象，并打印该对象
my_car = Car("红色", "SUV")
print(my_car)