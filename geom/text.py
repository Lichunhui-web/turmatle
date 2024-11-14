from geom.base import Geom, Point
import turtle

class Text(Geom):
    def __init__(
        self,
        position: Point,          # 文本位置
        text: str,               # 显示的文本内容
        color: str = "black",    # 文本颜色
        fontname: str = "Arial", # 字体名称
        fontsize: int = None,    # 字体大小（如果不指定则使用Geom默认值）
        align: str = "left",     # 对齐方式：'left', 'center', 'right'
        bold: bool = False,      # 是否加粗
        italic: bool = False,    # 是否斜体
    ) -> None:
        super().__init__(fontsize=fontsize)
        self.position = position
        self.text = text
        self.color = color
        self.fontname = fontname
        self.align = align
        
        # 设置字体样式
        style = "normal"
        if bold and italic:
            style = "bold italic"
        elif bold:
            style = "bold"
        elif italic:
            style = "italic"
        self.style = style
        
        # 创建turtle对象
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.turtle.color(self.color)

    def show(self):
        """显示文本"""
        # 使用tracer加速
        screen = self.turtle.getscreen()
        screen.tracer(0)
        
        # 移动到指定位置
        x, y = self.position.get_screen_coords()
        self.turtle.penup()
        self.turtle.goto(x, y)
        
        # 写入文本
        self.turtle.write(
            self.text,
            align=self.align,
            font=(self.fontname, self.fontsize, self.style)
        )
        
        screen.update()

    def clear(self):
        """清除文本"""
        self.turtle.clear() 