import manim as mn
from manim import *

class theory(Scene):
    def construct(self):
        t = MathTex(
            r"\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0"
        ).scale(3)

        t.set_color_by_tex(r"\rho", YELLOW)
        t.set_color_by_tex(r"\nabla", BLUE)

        t2 = Text("Mass conservation ensures that the density profile").scale(0.8)
        t3 = Text("(which influences temperature via energy coupling)").scale(0.8).next_to(t2, DOWN, buff=0.2)
        t4 = Text("is consistent as gas flows into the shock front.").scale(0.8).next_to(t3, DOWN, buff=0.2)

        text_group = VGroup(t2, t3, t4)
        rect = SurroundingRectangle(text_group, color=BLUE, fill_opacity=0.1, buff=0.3)

        self.play(Create(t), run_time=2)
        self.wait(0.5)
        self.play(t.animate.scale(1.2).set_color(RED), run_time=1)
        self.wait(0.5)

        self.play(FadeOut(t))

        #Reveals the text lines one by one with upward motion
        self.play(FadeIn(t2, shift=UP), run_time=1)
        self.wait(0.3)
        self.play(FadeIn(t3, shift=UP), run_time=1)
        self.wait(0.3)
        self.play(FadeIn(t4, shift=UP), run_time=1)
        self.wait(0.5)

        #Highlights the text group with a rectangle
        self.play(Create(rect), run_time=1.2)
        self.wait(2)


        self.play(FadeOut(t2), FadeOut(t3), FadeOut(t4), FadeOut(rect))
        self.wait(0.5)

class theory2(Scene):
    def construct(self):
        eq = MathTex(
            r"\frac{\partial (\rho \mathbf{v})}{\partial t}",
            r"+",
            r"\nabla \cdot (\rho \mathbf{v} \mathbf{v})",
            r"+",
            r"\nabla p",
            r"+",
            r"\lambda \nabla E_r",
            r"=",
            r"\frac{\kappa_P}{c} \mathbf{F}_*",
            r"-",
            r"\rho \nabla \Phi"
        ).scale(1.0)

        eq[0].set_color(YELLOW)
        eq[2].set_color(BLUE)
        eq[4].set_color(GREEN)
        eq[6].set_color(PURPLE)
        eq[8].set_color(RED)
        eq[10].set_color(ORANGE)

        eq.to_edge(UP, buff=0.5)

        t1 = Text("This equation describes the forces acting on the gas:", font_size=28).next_to(eq, DOWN, buff=1)
        t2 = Text("Inertia, pressure, radiation pressure, stellar radiation, and gravity.", font_size=26).next_to(t1, DOWN, buff=0.3)
        t3 = Text("It governs the acceleration and dynamics of gas in massive star formation.", font_size=26).next_to(t2, DOWN, buff=0.3)

        text_group = VGroup(t1, t2, t3)
        rect = SurroundingRectangle(text_group, color=BLUE, fill_opacity=0.1, buff=0.4)

        self.play(Create(eq), run_time=3)
        self.wait(0.5)
        self.play(FadeIn(t1, shift=DOWN))
        self.wait(0.3)
        self.play(FadeIn(t2, shift=DOWN))
        self.wait(0.3)
        self.play(FadeIn(t3, shift=DOWN))
        self.wait(1.5)
        self.play(Create(rect))
        self.wait(2)
        self.play(FadeOut(eq), FadeOut(text_group), FadeOut(rect))

class theory3(Scene):
    def construct(self):
        eq1 = MathTex(
            r"\frac{\partial(\rho e)}{\partial t}",
            r"+",
            r"\nabla \cdot (\rho e \mathbf{v} + P \mathbf{v})",
            r"=",
            r"-\kappa_P \rho c (a_R T^{4} - E_r)"
        ).scale(0.9)

        eq2 = MathTex(
            r"+ \lambda \left( 2 \frac{\kappa_P}{\kappa_R} - 1 \right) \mathbf{v} \cdot \nabla E_r",
            r"-",
            r"\nabla \cdot \mathbf{F}_*"
        ).scale(0.9)
        eq2.next_to(eq1, DOWN, buff=0.7)

        eq1[0].set_color(YELLOW)
        eq1[2].set_color(BLUE)
        eq1[4].set_color(RED)
        eq2[0].set_color(GREEN)
        eq2[2].set_color(PURPLE)

        t1 = Text("This equation governs the internal energy of the gas.", font_size=30)
        t1.shift(UP * 3)
        t2 = Text("It shows how compression and motion", font_size=30).next_to(t1, DOWN, buff=0.4)
        t3 = Text("interact with radiation absorption and emission.", font_size=30).next_to(t2, DOWN, buff=0.4)
        t4 = Text("On the graph, regions of heating and cooling", font_size=30).next_to(t3, DOWN, buff=0.4)
        t5 = Text("can be traced back to these terms,", font_size=30).next_to(t4, DOWN, buff=0.4)
        t6 = Text("linking gas dynamics with radiation transfer.", font_size=30).next_to(t5, DOWN, buff=0.4)

        text_group = VGroup(t1, t2, t3, t4, t5, t6)
        rect = SurroundingRectangle(text_group, color=BLUE, fill_opacity=0.1, buff=0.4)

        self.play(Create(eq1), run_time=2)
        self.wait(0.4)
        self.play(eq1.animate.scale(1.05).set_color(RED))
        self.wait(0.4)
        self.play(Create(eq2), run_time=2)
        self.wait(0.4)
        self.play(eq2.animate.scale(1.05).set_color(YELLOW))
        self.wait(0.6)
        self.play(FadeOut(eq1), FadeOut(eq2))

        self.play(FadeIn(t1, shift=UP))
        self.wait(0.2)
        self.play(FadeIn(t2, shift=UP))
        self.wait(0.2)
        self.play(FadeIn(t3, shift=UP))
        self.wait(0.2)
        self.play(FadeIn(t4, shift=UP))
        self.wait(0.2)
        self.play(FadeIn(t5, shift=UP))
        self.wait(0.2)
        self.play(FadeIn(t6, shift=UP))
        self.wait(0.4)

        self.play(Create(rect))
        self.wait(2)
        self.play(FadeOut(text_group), FadeOut(rect))
        self.wait(0.5)

class theory4(Scene):
    def construct(self):
        eq1 = MathTex(
            r"\frac{\partial E_r}{\partial t}",
            r"-",
            r"\nabla \cdot \left(\frac{c \lambda}{\kappa_R \rho} \nabla E_r\right)",
            r"=",
            r"-\nabla \cdot \left(\frac{3-f}{2} E_r \mathbf{v}\right)"
        ).scale(0.8)

        eq2 = MathTex(
            r"+ \kappa_P \rho c (a_R T^{4} - E_r)",
            r"-",
            r"\lambda \left(2 \frac{\kappa_P}{\kappa_R} - 1\right)\mathbf{v} \cdot \nabla E_r"
        ).scale(0.8)
        eq2.next_to(eq1, DOWN, buff=0.7)

        eq1[0].set_color(YELLOW)
        eq1[2].set_color(BLUE)
        eq1[4].set_color(RED)
        eq2[0].set_color(GREEN)
        eq2[2].set_color(PURPLE)

        t1 = Text("This equation governs the evolution of radiation energy.", font_size=30)
        t1.shift(UP * 3)
        t2 = Text("It includes diffusion, advection, and coupling", font_size=30).next_to(t1, DOWN, buff=0.4)
        t3 = Text("with the gas through emission and absorption.", font_size=30).next_to(t2, DOWN, buff=0.4)
        t4 = Text("On the graph, the radiation field responds", font_size=30).next_to(t3, DOWN, buff=0.4)
        t5 = Text("to these processes, smoothing out", font_size=30).next_to(t4, DOWN, buff=0.4)
        t6 = Text("temperature gradients across regions.", font_size=30).next_to(t5, DOWN, buff=0.4)

        text_group = VGroup(t1, t2, t3, t4, t5, t6)
        rect = SurroundingRectangle(text_group, color=BLUE, fill_opacity=0.1, buff=0.4)

        self.play(Create(eq1), run_time=2)
        self.wait(0.4)
        self.play(eq1.animate.scale(1.05).set_color(RED))
        self.wait(0.4)
        self.play(Create(eq2), run_time=2)
        self.wait(0.4)
        self.play(eq2.animate.scale(1.05).set_color(YELLOW))
        self.wait(0.6)
        self.play(FadeOut(eq1), FadeOut(eq2))

        self.play(FadeIn(t1, shift=UP))
        self.wait(0.2)
        self.play(FadeIn(t2, shift=UP))
        self.wait(0.2)
        self.play(FadeIn(t3, shift=UP))
        self.wait(0.2)
        self.play(FadeIn(t4, shift=UP))
        self.wait(0.2)
        self.play(FadeIn(t5, shift=UP))
        self.wait(0.2)
        self.play(FadeIn(t6, shift=UP))
        self.wait(0.4)

        self.play(Create(rect))
        self.wait(2)
        self.play(FadeOut(text_group), FadeOut(rect))
        self.wait(0.5)

