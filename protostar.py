import manim as mn
from manim import *

class theory(Scene):
    def construct(self):
        t = MathTex(
            r"\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0"
        ).scale(3)

        t.set_color_by_tex(r"\rho", YELLOW)
        t.set_color_by_tex(r"\nabla", BLUE)

        bg = ImageMobject("theory.png")
        bg.scale_to_fit_width(config.frame_width)
        bg.move_to(ORIGIN)

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
        self.play(FadeIn(bg, shift=RIGHT), run_time=1.5)
        self.play(FadeOut(bg))

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

        eq1 = MathTex(r"\frac{\partial \rho}{\partial t}", r"+")
        eq2 = MathTex(r"\nabla \cdot (\rho \mathbf{v})", r"= 0")
        eq1.scale(2)
        eq2.scale(2)
        eq2.next_to(eq1, DOWN, buff=0.5)

        eq1[0].set_color(YELLOW)
        eq2[0].set_color(BLUE)

        bg = ImageMobject("theory2.jpg").scale(2.3)
        bg.move_to(ORIGIN)

        t1 = Text("Mass conservation").scale(0.8)
        t1.shift(UP * 2)
        t2 = Text("ensures that the density profile").scale(0.8).next_to(t1, DOWN, buff=0.2)
        t3 = Text("(which influences temperature via").scale(0.8).next_to(t2, DOWN, buff=0.2)
        t4 = Text("energy coupling) is consistent as gas").scale(0.8).next_to(t3, DOWN, buff=0.2)
        t5 = Text("flows into the shock front.").scale(0.8).next_to(t4, DOWN, buff=0.2)

        text_group = VGroup(t1, t2, t3, t4, t5)
        rect = SurroundingRectangle(text_group, color=BLUE, fill_opacity=0.1, buff=0.3)

        self.play(Create(eq1), run_time=2)
        self.wait(0.3)
        self.play(eq1.animate.scale(1.1).set_color(RED))
        self.wait(0.3)
        self.play(Create(eq2), run_time=2)
        self.wait(0.3)
        self.play(eq2.animate.scale(1.1).set_color(RED))
        self.wait(0.5)

        self.play(FadeOut(eq1), FadeOut(eq2))
        self.play(FadeIn(bg, shift=RIGHT), run_time=1.5)
        self.wait(0.5)
        self.play(FadeOut(bg))

        self.play(FadeIn(t1, shift=UP))
        self.wait(0.2)
        self.play(FadeIn(t2, shift=UP))
        self.wait(0.2)
        self.play(FadeIn(t3, shift=UP))
        self.wait(0.2)
        self.play(FadeIn(t4, shift=UP))
        self.wait(0.2)
        self.play(FadeIn(t5, shift=UP))
        self.wait(0.3)

        self.play(Create(rect))
        self.wait(2)

        self.play(FadeOut(text_group), FadeOut(rect))
        self.wait(0.5)

class theory3(Scene):
    def construct(self):
        eq1 = MathTex(
            r"\frac{\partial e}{\partial t}",
            r"+",
            r"\nabla \cdot (e \mathbf{v})",
            r"=",
            r"-p \nabla \cdot \mathbf{v}"
        ).scale(1.5)
        eq2 = MathTex(
            r"- c \kappa_P \left( a_R T^{4} - E_r \right)"
        ).scale(1.5)
        eq2.next_to(eq1, DOWN, buff=1.0)

        eq1[0].set_color(YELLOW)
        eq1[2].set_color(BLUE)
        eq2.set_color(RED)

        bg = ImageMobject("theory3.png").scale(5)
        bg.move_to(ORIGIN)

        t1 = Text("This governs the heating and cooling", font_size=34)
        t1.shift(UP * 3)
        t2 = Text("of the gas. On the graph,", font_size=34).next_to(t1, DOWN, buff=0.5)
        t3 = Text("the matter temperature 'T' increases", font_size=34).next_to(t2, DOWN, buff=0.5)
        t4 = Text("in the post-shock region because", font_size=34).next_to(t3, DOWN, buff=0.5)
        t5 = Text("this equation couples compression work", font_size=34).next_to(t4, DOWN, buff=0.5)
        t6 = Text("and radiation heating.", font_size=34).next_to(t5, DOWN, buff=0.5)

        text_group = VGroup(t1, t2, t3, t4, t5, t6)
        rect = SurroundingRectangle(text_group, color=BLUE, fill_opacity=0.1, buff=0.5)

        self.play(Create(eq1), run_time=2)
        self.wait(0.4)
        self.play(eq1.animate.scale(1.1).set_color(RED))
        self.wait(0.4)
        self.play(Create(eq2), run_time=2)
        self.wait(0.4)
        self.play(eq2.animate.scale(1.1).set_color(YELLOW))
        self.wait(0.6)
        self.play(FadeOut(eq1), FadeOut(eq2))

        self.play(FadeIn(bg, shift=RIGHT), run_time=1.5)
        self.wait(0.6)
        self.play(FadeOut(bg))

        self.play(FadeIn(t1, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t2, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t3, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t4, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t5, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t6, shift=UP))
        self.wait(0.4)

        self.play(Create(rect))
        self.wait(2)
        self.play(FadeOut(text_group), FadeOut(rect))
        self.wait(0.5)

class theory4(Scene):
    def construct(self):
        eq1 = MathTex(
            r"\frac{\partial E_r}{\partial t}", r"+", r"\nabla \cdot (E_r \mathbf{v})", r"=", r"- \nabla \cdot \mathbf{F}"
        ).scale(1.4)
        eq2 = MathTex(
            r"- \mathbf{P} : \nabla \mathbf{v}", r"+", r"c \kappa_P \left( a_R T^{4} - E_r \right)"
        ).scale(1.4)
        eq2.next_to(eq1, DOWN, buff=1.0)

        eq1[0].set_color(YELLOW)
        eq1[2].set_color(BLUE)
        eq2[0].set_color(RED)
        eq2[2].set_color(GREEN)

        bg = ImageMobject("theory4.png").scale(1.8)
        bg.move_to(ORIGIN)

        t1 = Text("The radiation energy evolves", font_size=34)
        t1.shift(UP * 3)
        t2 = Text("alongside gas energy.", font_size=34).next_to(t1, DOWN, buff=0.5)
        t3 = Text("The green dashed line (radiation temperature)", font_size=34).next_to(t2, DOWN, buff=0.5)
        t4 = Text("in the graph follows from this equation,", font_size=34).next_to(t3, DOWN, buff=0.5)
        t5 = Text("showing how radiation diffuses", font_size=34).next_to(t4, DOWN, buff=0.5)
        t6 = Text("and balances with the gas.", font_size=34).next_to(t5, DOWN, buff=0.5)

        text_group = VGroup(t1, t2, t3, t4, t5, t6)
        rect = SurroundingRectangle(text_group, color=BLUE, fill_opacity=0.1, buff=0.5)

        self.play(Create(eq1), run_time=2)
        self.wait(0.4)
        self.play(eq1.animate.scale(1.1).set_color(RED))
        self.wait(0.4)
        self.play(Create(eq2), run_time=2)
        self.wait(0.4)
        self.play(eq2.animate.scale(1.1).set_color(YELLOW))
        self.wait(0.6)
        self.play(FadeOut(eq1), FadeOut(eq2))

        self.play(FadeIn(bg, shift=RIGHT), run_time=1.5)
        self.wait(0.6)
        self.play(FadeOut(bg))

        self.play(FadeIn(t1, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t2, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t3, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t4, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t5, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t6, shift=UP))
        self.wait(0.4)

        self.play(Create(rect))
        self.wait(2)
        self.play(FadeOut(text_group), FadeOut(rect))
        self.wait(0.5)

class theory5(Scene):
    def construct(self):
        eq1 = MathTex(
            r"\mathbf{F}", r"=", r"- \frac{c \lambda}{\kappa_R}", r"\nabla E_r"
        ).scale(1.8)
        eq1[0].set_color(YELLOW)
        eq1[2].set_color(BLUE)
        eq1[3].set_color(RED)

        bg = ImageMobject("theory5.png").scale(2)
        bg.move_to(ORIGIN)

        t1 = Text("This describes how quickly", font_size=34)
        t1.shift(UP*3)
        t2 = Text("radiation energy flows.", font_size=34).next_to(t1, DOWN, buff=0.5)
        t3 = Text("In the graph, radiation spreads", font_size=34).next_to(t2, DOWN, buff=0.5)
        t4 = Text("ahead of the shock", font_size=34).next_to(t3, DOWN, buff=0.5)
        t5 = Text("(raising the pre‑shock temperature)", font_size=34).next_to(t4, DOWN, buff=0.5)
        t6 = Text("because of diffusion governed by this relation.", font_size=34).next_to(t5, DOWN, buff=0.5)

        text_group = VGroup(t1, t2, t3, t4, t5, t6)
        rect = SurroundingRectangle(text_group, color=BLUE, fill_opacity=0.1, buff=0.5)

        self.play(Create(eq1), run_time=2)
        self.wait(0.4)
        self.play(eq1.animate.scale(1.1).set_color(RED))
        self.wait(0.6)
        self.play(FadeOut(eq1))

        self.play(FadeIn(bg, shift=RIGHT), run_time=1.5)
        self.wait(0.6)
        self.play(FadeOut(bg))

        self.play(FadeIn(t1, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t2, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t3, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t4, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t5, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(t6, shift=UP))
        self.wait(0.4)

        self.play(Create(rect))
        self.wait(2)
        self.play(FadeOut(text_group), FadeOut(rect))
        self.wait(0.5)

