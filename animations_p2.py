from manim import *
import numpy as np

class ThinkingMuBot(Scene):
    def construct(self):
        # title = MathTex(
        #     r'\text{``Symmetry brings balance in nature``}',
        #     font_size=48
        # ).set_color_by_gradient(BLUE, GREEN).to_edge(UP)
        # self.play(FadeIn(title))

        # Thought bubbles (dots leading to cloud)
        dot1 = Dot(radius=0.08, color=WHITE).move_to(2*DL).shift(1.5*LEFT + 0.5*UP)
        dot2 = Dot(radius=0.12, color=WHITE).next_to(dot1, UR, buff=0.2)
        dot3 = Dot(radius=0.16, color=WHITE).next_to(dot2, UR, buff=0.2)

        # Thinking cloud (Rounded Rectangle)
        thinking_cloud = RoundedRectangle(width=7, height=2.5, corner_radius=0.3, color=WHITE, fill_opacity=0.2)
        thinking_cloud.next_to(dot3, UR)

        tex1 = Tex("What happens in 3D ?").scale(0.8).arrange(DOWN).move_to(thinking_cloud.get_center())
        tex2 = Tex("Can we still prove the result ?")
        tex2.arrange(DOWN)

        tex2.scale(0.8).move_to(thinking_cloud.get_center())
        self.play(FadeIn(VGroup(dot1, dot2, dot3, thinking_cloud)))
        self.play(Write(tex1))
        self.play(Transform(tex1, tex2))
        self.wait(2)
        # self.add(title, dot1, dot2, dot3, thinking_cloud)

# -----------------------------
# 2D panel (math left, space right)
# -----------------------------
class Vector2D(Scene):
    def construct(self):
        title = Tex("2D (unit circle)", font_size=40).to_edge(UP)
        unit_vec = MathTex(
            r"\text{Unit vector: } (\cos\theta,\; \sin\theta)", r"\theta = [0, 2\pi)", font_size=38
        ).arrange(DOWN).next_to(title, DOWN)
        sum_eq = MathTex(
            r"\sum_{k=0}^{n-1}\left(\cos\!\frac{2\pi k}{n},\;\sin\!\frac{2\pi k}{n}\right)"
            r"\;=\;(0,0)",
            font_size=38,
            color=BLUE
        ).to_edge(DOWN)
        self.play(FadeIn(title))
        self.play(
                Write(unit_vec)
        )
        self.wait()
        self.play(Write(sum_eq))
        self.wait(10)

class Vector3D(Scene):
    def construct(self):
        title = Tex("3D (unit sphere)", font_size=40).to_edge(UP)

        unit_vec = MathTex(
            r"\text{Unit vector: } (\sin\phi\cos\theta,\;\sin\phi\sin\theta,\;\cos\phi)", r"\phi = [0, \pi] ; \theta = [0, 2\pi)",
            font_size=36
        ).arrange(DOWN).next_to(title, DOWN)

        sum_eq = MathTex(
            r"\sum_{p=0}^{m}\;\sum_{k=0}^{n-1}\Big("
            r"\sin\!\frac{\pi p}{m}\cos\!\frac{2\pi k}{n},\;"
            r"\sin\!\frac{\pi p}{m}\sin\!\frac{2\pi k}{n},\;"
            r"\cos\!\frac{\pi p}{m}\Big)\;=\;(0,0,0)",
            font_size=33,
            color=BLUE
        ).to_edge(DOWN)

        self.play(FadeIn(title))
        self.play(
                Write(unit_vec))
        self.wait()
        self.play(Write(sum_eq))
        self.wait()

class Loading1(Scene):
    def construct(self):
        # Parameters
        n, m = 8, 6
        delta_theta, delta_phi = 45, 30
        theta_vals = [i * delta_theta for i in range(n+1)]  # 0 → 360
        phi_vals = [i * delta_phi for i in range(m+1)]      # 0 → 180

        # Header (static info)
        header = MathTex(
            rf"n = {n},\; m = {m},\; \Delta\theta = {delta_theta}^\circ,\; \Delta\phi = {delta_phi}^\circ"
        ).scale(0.9).to_edge(UP)

        # Initial display for theta and phi
        eq = MathTex(r"\theta = 0^\circ, \quad \phi = 0^\circ").scale(1.2)

        # Add to scene
        self.play(Write(header))
        self.play(Write(eq))
        self.wait(0.5)

        # Animate discrete values
        for phi in phi_vals:
            for theta in theta_vals:
                new_eq = MathTex(
                    rf"\theta = {theta}^\circ, \quad \phi = {phi}^\circ"
                ).scale(1.2)
                self.play(Transform(eq, new_eq), run_time=0.5)
                self.wait(0.2)

        self.wait(1)

class Sum(Scene):
    def construct(self):
        sum_eq = MathTex(
            r"\sum_{p=0}^{m}\;\sum_{k=0}^{n-1}\Big(",
            r"\sin\!\frac{\pi p}{m}",   # <- isolate sin φ for x
            r"\cos\!\frac{2\pi k}{n},\;",
            r"\sin\!\frac{\pi p}{m}",   # <- isolate sin φ for y
            r"\sin\!\frac{2\pi k}{n},\;",
            r"\cos\!\frac{\pi p}{m}",
            r"\Big)",
        ).to_edge(UP)

        sum_eq1 = MathTex(
            r"\sum_{p=0}^{m}\;\sum_{k=0}^{n-1}\Big(",
            r"\sin\!\frac{\pi p}{m}",   # <- isolate sin φ for x
            r"\cos\!\frac{2\pi k}{n},\;",
            r"\sin\!\frac{\pi p}{m}",   # <- isolate sin φ for y
            r"\sin\!\frac{2\pi k}{n},\;",
            r"\cos\!\frac{\pi p}{m}",
            r"\Big)",
            r" = (0, 0, ?)"
        ).to_edge(UP)
        
        sum_eq2 = MathTex(
            r"\sum_{p=0}^{m}\;\sum_{k=0}^{n-1}\Big(",
            r"\sin\!\frac{\pi p}{m}",   # <- isolate sin φ for x
            r"\cos\!\frac{2\pi k}{n},\;",
            r"\sin\!\frac{\pi p}{m}",   # <- isolate sin φ for y
            r"\sin\!\frac{2\pi k}{n},\;",
            r"\cos\!\frac{\pi p}{m}",
            r"\Big)",
            r" = (0, 0, 0)"
        ).to_edge(UP)

        self.play(Write(sum_eq))
        self.wait(1)
        self.play(sum_eq.animate.set_color_by_tex(r"\sin\!\frac{\pi p}{m}", YELLOW))

        # # Add a brace + label to explicitly indicate factorization idea
        brace = Brace(sum_eq[1:5], DOWN, color=YELLOW)
        brace1 = Brace(sum_eq1[5], DOWN, color =  YELLOW)
        self.play(Create(brace))
        self.wait()

        xy_factor = MathTex(
            r"\text{For constant } \sin\phi:\quad",
            r"\sin\!\left(\tfrac{\pi p}{m}\right)",
            r"\left(",
            r"\sum_{k=0}^{n-1}\cos\!\left(\tfrac{2\pi k}{n}\right),",
            r"\ \sum_{k=0}^{n-1}\sin\!\left(\tfrac{2\pi k}{n}\right)",
            r"\right)",
            substrings_to_isolate=[r"\sin\!\left(\tfrac{\pi p}{m}\right)"],
        ).scale(0.9)
        xy_factor.next_to(sum_eq, DOWN, buff=0.6).set_color_by_tex(r"\sin\!\left(\tfrac{\pi p}{m}\right)", YELLOW)

        # 2D identity equals (0,0)
        xy_zero = MathTex(
            r"\text{We already know}:\quad",
            r"\sum_{k=0}^{n-1}\big(",
            r"\cos\!\left(\tfrac{2\pi k}{n}\right),",
            r"\sin\!\left(\tfrac{2\pi k}{n}\right)",
            r"\big)\;=\;(0,0)"
        ).scale(0.95)
        xy_zero.next_to(xy_factor, DOWN, buff=0.6)

        # Implication that whole xy-part dies
        xy_vanish = MathTex(
            r"\sin\!\left(\tfrac{\pi p}{m}\right)",
            r"\left(",
            r"\sum_{k=0}^{n-1}\cos\!\left(\tfrac{2\pi k}{n}\right),",
            r"\ \sum_{k=0}^{n-1}\sin\!\left(\tfrac{2\pi k}{n}\right)",
            r"\right)",
            r"=\,(0,0)"
        ).scale(0.95)
        xy_vanish.next_to(xy_zero, DOWN, buff=0.6)

        self.play(ReplacementTransform(sum_eq.copy(), xy_factor))
        self.wait()
        self.play(Write(xy_zero))
        self.wait()
        self.play(ReplacementTransform(xy_factor[1:].copy(), xy_vanish))
        self.wait(2)
        self.play(FadeOut(VGroup(xy_factor, xy_zero, xy_vanish)))
        self.play(ReplacementTransform(sum_eq, sum_eq1), ReplacementTransform(brace, brace1))
        self.wait(2)

        z_sum = MathTex(
            r"\text{For the } z\text{-component:}\quad",
            r"\sum_{p=0}^{m}\cos\!\left(\tfrac{\pi p}{m}\right)",
            r"=\,0" 
        ).scale(0.95)
        z_sum.next_to(sum_eq, DOWN, buff=0.9)

        z_expl = Tex(
            r"This is a symmetric sum over $\cos(\phi)$, which cancels when sampled evenly on $[0,\pi]$. "
            r"Each term above the equator cancels with its mirror below, plus the poles. "
            r"One can also apply Euler's formula for a more elegant proof.",
            font_size = 30,
            tex_environment="flushleft"   # keeps nice multiline alignment
        ).next_to(z_sum, DOWN, buff=0.5)

        self.play(Write(z_sum[0:2]))
        self.wait(0.5)
        self.play(FadeIn(z_expl, shift=DOWN))
        self.wait()
        self.play(Write(z_sum[2]), ReplacementTransform(sum_eq1[7], sum_eq2[7]))
        self.wait()
        self.play(FadeOut(VGroup(brace1, sum_eq2[7], z_sum, z_expl)))
        self.play(VGroup(sum_eq1[0:7], sum_eq2[7]).animate.shift(2*DOWN))
        self.wait()

class Loading2(Scene):
    def construct(self):
        # Parameters
        n, m = 3, 2
        delta_theta, delta_phi = 120, 90
        theta_vals = [i * delta_theta for i in range(n+1)]  # 0 → 360
        phi_vals = [i * delta_phi for i in range(m+1)]      # 0 → 180

        # Header (static info)
        header = MathTex(
            rf"n = {n},\; m = {m},\; \Delta\theta = {delta_theta}^\circ,\; \Delta\phi = {delta_phi}^\circ"
        ).scale(0.9).to_edge(UP)

        # Initial display for theta and phi
        eq = MathTex(r"\theta = 0^\circ, \quad \phi = 0^\circ").scale(1.2)

        # Add to scene
        self.play(Write(header))
        self.play(Write(eq))
        self.wait(0.5)

        # Animate discrete values
        for phi in phi_vals:
            for theta in theta_vals:
                new_eq = MathTex(
                    rf"\theta = {theta}^\circ, \quad \phi = {phi}^\circ"
                ).scale(1.2)
                self.play(Transform(eq, new_eq), run_time=0.5)
                self.wait(0.2)

        self.wait(1)

class Loading3(Scene):
    def construct(self):
        # Parameters
        n, m = 4, 2
        delta_theta, delta_phi = 90, 90
        theta_vals = [i * delta_theta for i in range(n+1)]  # 0 → 360
        phi_vals = [i * delta_phi for i in range(m+1)]      # 0 → 180

        # Header (static info)
        header = MathTex(
            rf"n = {n},\; m = {m},\; \Delta\theta = {delta_theta}^\circ,\; \Delta\phi = {delta_phi}^\circ"
        ).scale(0.9).to_edge(UP)

        # Initial display for theta and phi
        eq = MathTex(r"\theta = 0^\circ, \quad \phi = 0^\circ").scale(1.2)

        # Add to scene
        self.play(Write(header))
        self.play(Write(eq))
        self.wait(0.5)

        # Animate discrete values
        for phi in phi_vals:
            for theta in theta_vals:
                new_eq = MathTex(
                    rf"\theta = {theta}^\circ, \quad \phi = {phi}^\circ"
                ).scale(1.2)
                self.play(Transform(eq, new_eq), run_time=0.5)
                self.wait(0.2)

        self.wait(1)