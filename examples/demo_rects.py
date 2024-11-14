import sys
import os

# 添加项目根目录到系统路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# 现在导入应该可以工作了
from geom import Geom, Point, Line, Function, Rect
import math
import turtle

def main():
    # 设置全局默认值
    Geom.set_defaults(origin_x=0, origin_y=0, scale=100, fontsize=16)

    # 创建坐标轴
    x_axis = Line(Point(-1, 0), Point(3, 0), 
                  speed=0, pensize=1, 
                  color="gray", text="x")
    y_axis = Line(Point(0, -1), Point(0, 3), 
                  speed=0, pensize=1,
                  color="gray", text="y")

    # 创建一个矩形
    rect = Rect(
        bottom_left=Point(0.5, 0.5),
        top_right=Point(1.5, 1.5),
        color="red",
        pensize=2,
        fill_color="pink",
        fill=True,
        text="R1"
    )

    # 显示所有元素
    rect.show()
    x_axis.show()
    y_axis.show()

    turtle.done()

if __name__ == "__main__":
    main() 