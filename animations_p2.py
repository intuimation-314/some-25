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
        self.wait(2)
        self.play(Indicate(unit_vec[0]))
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

class SumToIntegral(Scene):
    def construct(self):
        title = Tex(
            "As n, m tends to infity the double sum can be translated into double integral using Riemann Sums",
            color = BLUE
        ).to_edge(UP).scale(0.8)

        # 1) Double sum (center)
        sum_vec = MathTex(
            r"\sum_{p=0}^{m} \sum_{k=0}^{n-1} "
            r"\begin{pmatrix}"
            r"\sin\left(\frac{\pi p}{m}\right)\cos\left(\frac{2\pi k}{n}\right) \\"
            r"\sin\left(\frac{\pi p}{m}\right)\sin\left(\frac{2\pi k}{n}\right) \\"
            r"\cos\left(\frac{\pi p}{m}\right)"
            r"\end{pmatrix}",
            font_size=40
        ).scale(0.9)

        # 2) Limit label (to the left of sum)
        lim_label = MathTex(
            r"\lim_{n,m\to\infty}",
            font_size=40
        ).scale(0.9)

        # 3) Arrow + integral (to the right of sum)
        arrow_integral = MathTex(
            r"\;\to\;"
            r"\frac{nm}{2\pi^2}\int_{0}^{\pi}\int_{0}^{2\pi}"
            r"\begin{pmatrix}"
            r"\sin\phi\cos\theta \\"
            r"\sin\phi\sin\theta \\"
            r"\cos\phi"
            r"\end{pmatrix}"
            r"\, d\theta \, d\phi",
            font_size=40
        ).scale(0.9)

        subtitle = Tex(
            "Evaluating the double integral gives 0, again in the continuous limit: ",
            color = BLUE
        ).scale(0.8)

        # 4) Evaluation (below the integral)
        evaluation = MathTex(
            r"\frac{nm}{2\pi^2}\int_{0}^{\pi}\int_{0}^{2\pi}"
            r"\begin{pmatrix}"
            r"\sin\phi\cos\theta \\"
            r"\sin\phi\sin\theta \\"
            r"\cos\phi"
            r"\end{pmatrix}"
            r"\, d\theta \, d\phi"
            r" \;=\; "
            r"\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}",
            font_size=40
        ).scale(0.9)

        # Layout
        sum_vec.move_to(ORIGIN + 2.5*LEFT)
        lim_label.next_to(sum_vec, LEFT, buff=0.6)
        arrow_integral.next_to(sum_vec, RIGHT, buff=0.6)
        subtitle.next_to(VGroup(sum_vec, arrow_integral), DOWN, buff=0.8)
        evaluation.next_to(subtitle, DOWN, buff=0.8)

        # Animations
        self.play(Write(sum_vec))
        self.wait(0.7)
        self.play(Write(title), Write(lim_label))
        self.wait(0.5)
        self.play(FadeIn(arrow_integral, shift=RIGHT))
        self.wait(0.5)
        self.play(FadeIn(subtitle))
        self.play(Write(evaluation))
        self.wait(2)

class MatrixExplanation3D(Scene):
    def construct(self):
        # --- Explanatory block: 3D rotations (SO(3)) ---
        explanation = VGroup(
            Tex(
                "But what happens when we step into ",
                r"\textbf{3D}",
                "?",
                font_size=26
            ),
            Tex(
                "Here, rotations are $3\\times 3$ matrices—elements of the group $SO(3)$.",
                font_size=26
            ),
            Tex(
                "For instance, a rotation around the $z$-axis looks like this:",
                font_size=26
            ),
            MathTex(
                r"R_z(\theta) = "
                r"\begin{bmatrix}"
                r"\cos\theta & -\sin\theta & 0 \\"
                r"\sin\theta & \cos\theta  & 0 \\"
                r"0          & 0           & 1"
                r"\end{bmatrix}.",
                font_size=28
            ),
            Tex(
                "There are similar ones for rotations about the $x$- and $y$-axes, "
                "and by combining them you can get \\emph{any} rotation in 3D.",
                font_size=26
            ),
            # NOTE: add a space or {} after \qquad to avoid \qquadR_y
            MathTex(
                r"R_x(\phi) = "
                r"\begin{bmatrix}"
                r"1 & 0         & 0        \\"
                r"0 & \cos\phi  & -\sin\phi\\"
                r"0 & \sin\phi  & \cos\phi "
                r"\end{bmatrix},\qquad {}"
                r"R_y(\psi) = "
                r"\begin{bmatrix}"
                r"\cos\psi & 0 & \sin\psi \\"
                r"0        & 1 & 0        \\"
                r"-\sin\psi& 0 & \cos\psi "
                r"\end{bmatrix}.",
                font_size=28
            ),
        ).arrange(DOWN, buff=0.4).scale(1.2)

        # Staged reveals
        self.play(FadeIn(explanation[0]))
        self.wait(3)
        self.play(FadeIn(explanation[1]))
        self.wait()
        self.play(FadeIn(explanation[2]))
        self.play(FadeIn(explanation[3]))
        self.wait()
        self.play(FadeIn(explanation[4:]))
        self.wait()