import sys
import os

# 添加项目根目录到系统路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# 现在导入应该可以工作了
from geom import Geom, Point, Line, Function, Rect, Text
import math
import turtle

def main():
    # 设置全局默认值
    Geom.set_defaults(origin_x=-1, origin_y=-0.5, scale=300, fontsize=24)

    # 创建坐标轴
    x_axis = Line(Point(-0.2, 0), Point(2, 0), 
                speed=0, pensize=3, 
                color="gray", text="x",
                arrow=True)
    y_axis = Line(Point(0, -0.2), Point(0, 1.2), 
                speed=0, pensize=3,
                color="gray", text="y",
                arrow=True)

    # 显示坐标轴
    x_axis.show()
    y_axis.show()

    # 绘制被积函数
    sin_func = Function(
        math.sin,
        x_start=0, 
        x_end=0.5*math.pi,
        color="black", 
        pensize=5,
        text="sin(x)",
        fill=True,
        fill_color="azure"
        #text_pos=(0, 1)  # 在 (0,1) 位置显示文本
    )
    sin_func.show()

    # 计算黎曼和
    N = 10
    dx = 0.5*math.pi/N
    
    S = 0
    for i in range(N):
        x_l = i*dx
        x_r = (i+1)*dx 
        x_i = x_l
        y_i = math.sin(x_i)
        A_i = y_i * (x_r - x_l)
        S = S + A_i
        
        rect1 = Rect(
            bottom_left=Point(x_l, 0),
            top_right=Point(x_r, y_i),
            color="blue",
            pensize=1,
            fill_color="lightblue",
            fill=True
        )
        rect1.show()
    
    if 'text' in locals():
        text.clear()
        
    text = Text(
        position=Point(0.6, 1.1),
        text=f'S({N}) = {S:.2f}',
        color="green",
        align="center",
        bold=True,
        italic=True
    )        
    text.show()
    
    turtle.done()

if __name__ == "__main__":
    main() 
