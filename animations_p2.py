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