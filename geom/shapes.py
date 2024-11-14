from geom.base import Geom, Point
import turtle
import math

class Line(Geom):
    def __init__(
        self,
        start: Point,
        end: Point,
        speed: float = 1,
        pensize: float = 12,
        arrow: bool = False,
        color: str = "black",
        text: str = None,
    ) -> None:
        super().__init__()
        self.start = start
        self.end = end
        self.turtle = turtle.Turtle()
        self.turtle.speed(speed)
        self.turtle.pensize(pensize)
        self.turtle.hideturtle()
        self.arrow = arrow
        self.color = color
        self.turtle.color(self.color)
        self.text = text

    def show(self):
        x1, y1 = self.start.get_screen_coords()
        x2, y2 = self.end.get_screen_coords()
        self.turtle.penup()
        self.turtle.goto(x1, y1)
        self.turtle.pendown()
        self.turtle.goto(x2, y2)
        self.turtle.penup()
        if self.arrow:
            angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
            self.turtle.setheading(angle)
            self.turtle.stamp()
        if self.text:
            self.turtle.write(
                self.text, 
                font=("Arial", self.fontsize, "normal"), 
                align="right"
            )

    def clear(self):
        self.turtle.clear()


class Function(Geom):
    def __init__(self, func, x_start=-2, x_end=2, steps=100, 
                 color="blue", pensize=1, text=None, text_pos=None,
                 fill=False, fill_color="lightgray"):  # 添加fill选项
        super().__init__()
        self.func = func
        self.x_start = x_start
        self.x_end = x_end
        self.steps = steps
        self.color = color
        self.pensize = pensize
        self.text = text
        self.text_pos = text_pos if text_pos else (self.x_end, self.func(self.x_end))
        self.fill_color = fill_color
        self.fill = fill  # 是否填充
        
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.pensize(pensize)
        self.turtle.hideturtle()

    def fill_area(self):
        """填充函数与X轴之间的区域"""
        if not self.fill:  # 如果不需要填充，直接返回
            return
            
        # 关闭动画效果
        screen = self.turtle.getscreen()
        screen.tracer(0)
        
        self.turtle.color(self.fill_color)
        self.turtle.penup()
        
        # 移动到起始点的x轴位置
        start_point = Point(self.x_start, 0)
        start_x, start_y = start_point.get_screen_coords()
            
        self.turtle.goto(start_x, start_y)
        
        self.turtle.begin_fill()
        
        # 画到函数起点
        first_y = self.func(self.x_start)
        # 增加一个小空白
        if first_y > 0:
            first_y = first_y - 0.01
        else:
            first_y = first_y + 0.01
                            
        first_point = Point(self.x_start, first_y)
        fx, fy = first_point.get_screen_coords()
        self.turtle.goto(fx, fy)
                
        # 绘制函数曲线
        dx = (self.x_end - self.x_start) / self.steps
        for i in range(self.steps + 1):
            x = self.x_start + i * dx
            try:
                y = self.func(x)
                # 增加一个小空白
                if y > 0:
                    y = y - 0.01
                else:
                    y = y + 0.01    
                                    
                point = Point(x, y)
                screen_x, screen_y = point.get_screen_coords()            
                self.turtle.goto(screen_x, screen_y)
            except:
                continue
        
        # 画回x轴
        end_point = Point(self.x_end, 0)
        end_x, end_y = end_point.get_screen_coords()
        self.turtle.goto(end_x, end_y)
        
        # 回到起点
        self.turtle.goto(start_x, start_y)
        
        self.turtle.end_fill()
        
        # 重新启用动画效果
        screen.tracer(1)
        screen.update()

    def show(self):       
        # 再画函数曲线
        self.turtle.color(self.color)
        self.turtle.penup()
        
        # 绘制函数曲线
        dx = (self.x_end - self.x_start) / self.steps
        first_x = self.x_start
        first_y = self.func(first_x)
        start_point = Point(first_x, first_y)
        start_x, start_y = start_point.get_screen_coords()
        self.turtle.goto(start_x, start_y)
        self.turtle.pendown()
        
        for i in range(self.steps + 1):
            x = self.x_start + i * dx
            try:
                y = self.func(x)
                point = Point(x, y)
                screen_x, screen_y = point.get_screen_coords()
                self.turtle.goto(screen_x, screen_y)
            except:
                self.turtle.penup()
                continue
            self.turtle.pendown()

        # 添加文本标签
        if self.text:
            self.turtle.penup()
            text_point = Point(self.text_pos[0], self.text_pos[1])
            text_x, text_y = text_point.get_screen_coords()
            self.turtle.goto(text_x, text_y)
            self.turtle.write(
                self.text, 
                font=("Arial", self.fontsize, "normal"), 
                align="left"
            )
        
        # 最后填充区域
        self.fill_area()
        
    def clear(self):
        self.turtle.clear()


class Rect(Geom):
    def __init__(
        self,
        bottom_left: Point,  # 左下顶点
        top_right: Point,    # 右上顶点
        color="blue",
        pensize=1,
        fill_color="lightgray",
        fill=False,
        text=None,
        text_pos=None
    ):
        super().__init__()
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.color = color
        self.pensize = pensize
        self.fill_color = fill_color
        self.fill = fill
        self.text = text
        # 如果没有指定文本位置，默认放在矩形右上角
        self.text_pos = text_pos if text_pos else (
            top_right.x,
            top_right.y
        )
        
        # 创建背景turtle用于填充
        self.bg_turtle = turtle.Turtle()
        self.bg_turtle.hideturtle()
        self.bg_turtle.speed(0)
        
        # 创建前景turtle用于画线
        self.fg_turtle = turtle.Turtle()
        self.fg_turtle.hideturtle()
        self.fg_turtle.speed(0)
        self.fg_turtle.pensize(pensize)

    def fill_area(self):
        """填充矩形区域"""
        if not self.fill:
            return
            
        screen = self.bg_turtle.getscreen()
        screen.tracer(0)
        
        self.bg_turtle.clear()
        self.bg_turtle.color(self.fill_color)
        self.bg_turtle.penup()
        
        # 获取四个顶点的屏幕坐标
        bl_x, bl_y = self.bottom_left.get_screen_coords()
        tr_x, tr_y = self.top_right.get_screen_coords()
        br_x, br_y = Point(self.top_right.x, self.bottom_left.y).get_screen_coords()
        tl_x, tl_y = Point(self.bottom_left.x, self.top_right.y).get_screen_coords()
        
        # 开始填充
        self.bg_turtle.goto(bl_x, bl_y)
        self.bg_turtle.begin_fill()
        
        # 按顺序绘制四个顶点
        self.bg_turtle.goto(tl_x, tl_y)
        self.bg_turtle.goto(tr_x, tr_y)
        self.bg_turtle.goto(br_x, br_y)
        self.bg_turtle.goto(bl_x, bl_y)
        
        self.bg_turtle.end_fill()
        screen.update()

    def show(self):
        # 先在背景填充
        self.fill_area()
        
        # 在前景画边框
        screen = self.fg_turtle.getscreen()
        screen.tracer(0)
        
        self.fg_turtle.color(self.color)
        self.fg_turtle.penup()
        
        # 获取四个顶点的屏幕坐标
        bl_x, bl_y = self.bottom_left.get_screen_coords()
        tr_x, tr_y = self.top_right.get_screen_coords()
        br_x, br_y = Point(self.top_right.x, self.bottom_left.y).get_screen_coords()
        tl_x, tl_y = Point(self.bottom_left.x, self.top_right.y).get_screen_coords()
        
        # 画矩形边框
        self.fg_turtle.goto(bl_x, bl_y)
        self.fg_turtle.pendown()
        self.fg_turtle.goto(tl_x, tl_y)
        self.fg_turtle.goto(tr_x, tr_y)
        self.fg_turtle.goto(br_x, br_y)
        self.fg_turtle.goto(bl_x, bl_y)
        self.fg_turtle.penup()
        
        # 添加文本标签
        if self.text:
            text_point = Point(self.text_pos[0], self.text_pos[1])
            text_x, text_y = text_point.get_screen_coords()
            self.fg_turtle.goto(text_x, text_y)
            self.fg_turtle.write(
                self.text, 
                font=("Arial", self.fontsize, "normal"), 
                align="left"
            )
        
        screen.update()

    def clear(self):
        """清除所有绘制内容"""
        self.bg_turtle.clear()
        self.fg_turtle.clear()
