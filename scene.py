from manim import *

class intro(Scene):
    def construct(self):
        bkgc = '#FDF6E3'
        self.camera.background_color = bkgc
        txtc = '#A89E84'
        tmap = Text("Map", color=txtc, size=2).set_y(1)
        bl1 = Rectangle(width=16, height=4, color=bkgc, fill_opacity=1).set_y(2).set_x(16)
        tmaths = Text("Maths", color=txtc, size=2).set_y(-1).flip(LEFT)
        bl2 = Rectangle(width=16, height=4, color=bkgc, fill_opacity=1).set_y(-2)
        div1 = Line(start=8 * LEFT, end=8 * RIGHT).set_color(txtc).set_x(16).set_z_index(100)
        div2 = Line(start=2 * LEFT, end=2 * RIGHT).set_color(txtc).set_x(-10)
        self.add(tmap, tmaths, bl2, div2)
        self.play(Group(bl2, div1, bl1).animate.shift(LEFT * 16), run_time=1)
        self.wait(1)
        self.play(Group(div1, bl1).animate.shift(LEFT * 16), run_time=1)
        self.wait(1)
        self.play(div2.animate.shift(RIGHT * 20), run_time=1)
        self.play(div2.set_x(-10).animate.shift(RIGHT * 10), run_time=3/4)
        self.play(Flash(ORIGIN, line_length=0.5, flash_radius=2.5))

class intropic4x3(Scene):
    def construct(self):
        self.camera.background_color = '#FDF6E3'
        txtc = '#A89E84'
        tmap = Text("Map", color=txtc, size=2).set_y(1)
        tmaths = Text("Maths", color=txtc, size=2).set_y(-1).flip(LEFT)
        div = Line(start=8 * LEFT, end=8 * RIGHT).set_color(txtc)
        self.add(tmap, tmaths, div)

class intropic1x1(Scene):
    def construct(self):
        self.camera.pixel_height = 480
        self.camera.pixel_width = 480
        self.camera.frame_width = 8
        self.camera.frame_height = 8
        self.camera.background_color = '#FDF6E3'
        txtc = '#A89E84'
        tmap = Text("Map", color=txtc, size=3).set_y(1.5)
        tmaths = Text("Maths", color=txtc, size=3).set_y(-1.5).flip(LEFT)
        div = Line(start=4 * LEFT, end=4 * RIGHT).set_color(txtc).set_stroke(width=10)
        self.add(tmap, tmaths, div)
        
