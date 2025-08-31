from manim import *

class ThinkingMuBot(Scene):
    def construct(self):
        title = MathTex(
            r'\text{``Climbing into Higher Dimensions``}',
            font_size=48
        ).set_color_by_gradient(BLUE, GREEN).to_edge(UP)
        self.play(FadeIn(title))

        # Thought bubbles (dots leading to cloud)
        dot1 = Dot(radius=0.08, color=WHITE).move_to(2*DL).shift(1.5*LEFT + 0.5*UP)
        dot2 = Dot(radius=0.12, color=WHITE).next_to(dot1, UR, buff=0.2)
        dot3 = Dot(radius=0.16, color=WHITE).next_to(dot2, UR, buff=0.2)

        # Thinking cloud (Rounded Rectangle)
        thinking_cloud = RoundedRectangle(width=7, height=2.5, corner_radius=0.3, color=WHITE, fill_opacity=0.2)
        thinking_cloud.next_to(dot3, UR)

        tex1 = Tex("What about 4D ?", "Or even 5D?").scale(0.8).arrange(DOWN).move_to(thinking_cloud.get_center())
        tex2 = Tex("Yes, the same principle still holds!").scale(0.8).move_to(thinking_cloud.get_center())
        tex3 = Tex("Hyperspheres, multiple angles", "and some pure Math generalizations").scale(0.7).arrange(DOWN).move_to(thinking_cloud.get_center())
        tex4 = Tex("Too much Math!!").scale(0.8).move_to(thinking_cloud.get_center())

        self.play(FadeIn(VGroup(dot1, dot2, dot3, thinking_cloud)))
        self.play(Write(tex1))
        self.play(Transform(tex1, tex2))
        self.wait()
        self.play(Transform(tex1, tex3))
        self.wait()
        self.play(Transform(tex1, tex4))
        self.wait(2)
        # self.add(title, dot1, dot2, dot3, thinking_cloud)

class HigherDim(Scene):
        def construct(self):
            title = MathTex(
                r'\text{``In every dimension, symmetry enforces balance``}',
                font_size=48
            ).set_color_by_gradient(BLUE, GREEN)
            self.play(Create(title))
            self.wait(2)

class SumToInt2D(Scene):
    def construct(self):
        # --- Corner labels ---
        label_2d = Text("2D", font_size=36).to_edge(UP)

        # --- 2D: sum -> integral (upper-left) ---
        # Keep each LaTeX environment in a SINGLE string to avoid align* breakage.
        sum_2d = MathTex(
            r"\sum_{k=0}^{n-1}"
            r"\begin{pmatrix}"
            r"\cos\!\left(\frac{2\pi k}{n}\right)\\"
            r"\sin\!\left(\frac{2\pi k}{n}\right)"
            r"\end{pmatrix}"
            r"\;\;\longrightarrow\;\;"
            r"\frac{n}{2\pi}\int_{0}^{2\pi}"
            r"\begin{pmatrix}"
            r"\cos\theta\\"
            r"\sin\theta"
            r"\end{pmatrix}"
            r"\,d\theta",
            font_size=48,
            color = BLUE
        ).to_edge(DOWN)

  
        # --- Appear animations ---
        self.play(FadeIn(label_2d, shift=DOWN))
        self.play(Write(sum_2d))
        self.wait(0.4)

class SumToInt3D(Scene):
    def construct(self):

        label_3d = Text("3D", font_size=36).to_edge(UP)

        # --- 3D: double sum -> double integral (upper-right) ---
        sum_3d = MathTex(
            r"\sum_{p=0}^{m}\sum_{k=0}^{n-1}"
            r"\begin{pmatrix}"
            r"\sin\!\left(\frac{\pi p}{m}\right)\cos\!\left(\frac{2\pi k}{n}\right)\\"
            r"\sin\!\left(\frac{\pi p}{m}\right)\sin\!\left(\frac{2\pi k}{n}\right)\\"
            r"\cos\!\left(\frac{\pi p}{m}\right)"
            r"\end{pmatrix}"
            r"\;\;\longrightarrow\;\;"
            r"\frac{nm}{2\pi^2}\int_{0}^{\pi}\int_{0}^{2\pi}"
            r"\begin{pmatrix}"
            r"\sin\phi\cos\theta\\"
            r"\sin\phi\sin\theta\\"
            r"\cos\phi"
            r"\end{pmatrix}"
            r"\,d\theta\,d\phi",
            font_size=40,
            color = BLUE
        ).to_edge(DOWN)
        # --- Appear animations ---
        self.play(FadeIn(label_3d, shift=DOWN))
        self.play(Write(sum_3d))
        self.wait(0.4)

class GTProof(Scene):
    def construct(self):
        # 1) Start with the compact exponential sum
        eq1 = MathTex(
            r"S = \sum_{k=0}^{n-1} e^{2\pi i k / n}", font_size=46
        ).to_edge(UP)
        self.play(Write(eq1))
        self.wait(0.6)

        # 2) Expanded form
        eq2 = MathTex(
            r"S =",
            "1",
            r"+ e^{2\pi i / n}",
            r"+ e^{4\pi i / n}",
            r"+ \cdots + e^{2\pi i (n-2)/n}",
            r"+ e^{2\pi i (n-1)/n}",
            font_size=44
        ).next_to(eq1, DOWN, buff=0.7)
        self.play(Write(eq2))
        self.wait(0.6)

        # 3) Multiply both sides by e^{2π i / n}
        #    (Keep each piece as a separate arg; include all needed '+' signs)
        eq3 = MathTex(
            r"e^{2\pi i / n}\, S =",
            r"e^{2\pi i / n}",
            r"+ e^{4\pi i / n}",
            r"+ e^{6\pi i / n}",
            r"+ \cdots + e^{2\pi i (n-1)/n}",
            r"+ e^{2\pi i}",
            font_size=44
        ).next_to(eq2, DOWN, buff=0.7)

        eq4 = MathTex(
            r"e^{2\pi i / n}\, S =",
            r"e^{2\pi i / n}",
            r"+ e^{4\pi i / n}",
            r"+ e^{6\pi i / n}",
            r"+ \cdots + e^{2\pi i (n-1)/n}",
            r"+ 1",
            font_size=44
        ).next_to(eq2, DOWN, buff=0.7)
        eq5 = MathTex(
            r"e^{2\pi i / n}\, S = S"
        ).next_to(eq2, DOWN, buff=0.7)

        # Write the full eq3 so its parts exist for transforms
        self.play(Write(eq3[0]))
        self.wait(0.6)

        # Pairs of mappings (top eq2 → bottom eq3)
        # eq2 parts: [0:"S =", 1:"1", 2:"+ e^{2πi/n}", 3:"+ e^{4πi/n}", 4:"+ ⋯ + e^{... (n-2)/n}", 5:"+ e^{... (n-1)/n}"]
        # eq3 parts: [0:"e^{...} S =", 1:"e^{2πi/n}", 2:"+ e^{4πi/n}", 3:"+ e^{6πi/n}", 4:"+ ⋯ + e^{... (n-1)/n}", 5:"+ e^{2πi}"]
        mappings = [
            (1, 1),   # 1 -> e^{2π i / n}
            (2, 2),
            (3, 3),   # e^{2π i / n} -> e^{4π i / n}
            (4, 4),   # "… + e^{(n-2)/n}"  -> "… + e^{(n-1)/n}"
            (5, 5),   # e^{(n-1)/n} -> e^{2π i}
        ]

        for t_idx, b_idx in mappings:
            self.play(eq2[t_idx].animate.set_color(YELLOW))
            self.play(TransformFromCopy(eq2[t_idx], eq3[b_idx]))
            self.wait(0.4)
            self.play(eq2[t_idx].animate.set_color(WHITE))

        # 3a) Call out that e^{2π i} = 1
        note_e2pi = MathTex(r"e^{2\pi i} = 1", font_size=36).next_to(eq3, DOWN, buff=0.5)
        self.play(
            Indicate(eq3.get_part_by_tex(r"e^{2\pi i}")),
            FadeIn(note_e2pi)
        )
        self.wait(0.6)

        # Turn e^{2π i} into 1
        self.play(Transform(eq3, eq4))
        self.wait(0.6)

        # Boxes around the sums excluding the labels (index 0)
        box_top = SurroundingRectangle(VGroup(*eq2[1:]), color=BLUE, buff=0.2)
        box_bottom = SurroundingRectangle(VGroup(*eq3[1:]), color=GREEN, buff=0.2)
        self.play(Create(box_top))
        self.wait(0.3)
        self.play(ReplacementTransform(box_top, box_bottom))
        self.wait(0.6)

                # Fade out the boxes and the note
        self.play(FadeOut(box_top), FadeOut(box_bottom), FadeOut(note_e2pi))
        self.wait(0.2)

        # Transform eq2[1:] (expanded S) into a single "S" placed next to eq3[0]
        rhs_S = MathTex("S", font_size=44).next_to(eq3[0], RIGHT, buff=0.3)
        # Optionally fade out eq3's current RHS to make space
        self.play(ReplacementTransform(VGroup(*eq3[1:]), rhs_S))
        self.wait(0.3) 
        self.play(Transform(VGroup(eq3[0], rhs_S), eq5))
        self.wait()

        # Caption ABOVE the first subtraction line
        caption = MathTex(r"\text{Subtracting } S \text{ on both sides}", font_size=32).next_to(eq5, DOWN, buff=0.3)
        # First subtraction line just below eq3
        line1 = MathTex(
            r"e^{2\pi i / n} S \;-\; S \;=\; 0", font_size=44
        ).next_to(caption, DOWN, buff=0.7)
        # Second line (factored form)
        line2 = MathTex(
            r"\big(e^{2\pi i / n} - 1\big)\, S \;=\; 0", font_size=44
        ).next_to(line1, DOWN, buff=0.4)

        self.play(Write(caption))
        self.play(Write(line1))
        self.wait(0.2)
        self.play(Write(line2))
        self.wait(0.4)

        # Conclusion BELOW line2
        conclusion = MathTex(
            r"e^{2\pi i / n} \neq 1 \text{ for } n>1 \;\Rightarrow\; S = 0",
            font_size=44
        ).next_to(line2, DOWN, buff=0.5)
        self.play(Write(conclusion))
        self.wait(0.8)

class ComplexRotation(Scene):
    def construct(self):
        n = 9
        radius = 2  # Radius of the circle
        center = 3 * LEFT  # Center of the circle
        
        # Create axes with grids
        axes = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        ).scale(0.6).shift(center)  # Shift axes to match the new center

        # Add labels for the axes
        x_label0 = MathTex("Re").next_to(axes.x_axis, RIGHT)
        y_label0 = MathTex("Im").next_to(axes.y_axis, UP)


        # Euler's formula text
        euler_formula = MathTex(
            r"e^{i\theta} = \cos(\theta) + i\sin(\theta)"
        ).move_to(3* RIGHT + UP)
      
        # Add elements to the scene
        self.play(Create(VGroup(axes,x_label0,y_label0)))
        self.play(Write(euler_formula))
        self.wait(2)
        self.play(euler_formula.animate.scale(0.6).shift(2*UP + LEFT))
        rec = SurroundingRectangle(euler_formula)
        self.play(Create(rec))
        self.wait() 


        # Create vectors and display them
        vectors = VGroup()
        vector_labels = VGroup()
        for i in range(n):
            angle = TAU * i / n  # Angle in radians
            end_point = center + radius * np.array([np.cos(angle), np.sin(angle), 0])
            vector = Arrow(
                start=center,
                end=end_point,
                buff=0,
                color=BLUE,
                stroke_width=2,  # Thin arrows
            )
            # Add labels based on conditions
            if i == 4:
                label = MathTex(r"k").move_to(1.15 * (end_point - center) + center).scale(0.6)
            elif i == n - 2:
                label = MathTex(r"n-2").move_to(1.15 * (end_point - center) + center).scale(0.6)
            elif i == n - 1:
                label = MathTex(r"n-1").move_to(1.15 * (end_point - center) + center).scale(0.6)
            elif 4 < i < n - 2:  # Dots for mid-section
                label = MathTex(r"\cdots").move_to(1.15 * (end_point - center) + center).scale(0.6)
            else:
                label = MathTex(f"{i}").move_to(1.15 * (end_point - center) + center).scale(0.6)

            vectors.add(vector)
            vector_labels.add(label)

        # Animate vectors and labels
        self.play(Create(vectors))
        self.play(Create(vector_labels))
        self.wait(2)

        group = VGroup(vectors, vector_labels)
        self.play(Create(vectors))
        self.play(Create(vector_labels))
        self.wait(1)

        # Angle display (top-right area)
        def angle_tex(k):
            if k == "2pi":
                return r"R_{\theta} = 2\pi"
            else:
                return rf"R_{{\theta}} = \tfrac{{{k}\cdot 2\pi}}{{n}}"

        angle_disp = MathTex(angle_tex(1)).to_corner(UR).shift(0.5*LEFT + 0.2*DOWN)
        self.play(Write(angle_disp))
        self.wait(0.4)

        # --- Rotations: +2π/n, then to 4π/n, then to 6π/n, then to 2π ---
        # Use incremental rotations so it feels like a continuous group rotation.
        step = TAU / n

        # 2π/n
        self.play(group.animate.rotate(step, about_point=center), run_time=1.0)
        self.wait(0.5)

        # update label to 4π/n and rotate another +2π/n
        self.play(Transform(angle_disp, MathTex(angle_tex(2)).move_to(angle_disp)))
        self.play(group.animate.rotate(step, about_point=center), run_time=1.0)
        self.wait(0.5)

        # update label to 6π/n and rotate another +2π/n
        self.play(Transform(angle_disp, MathTex(angle_tex(3)).move_to(angle_disp)))
        self.play(group.animate.rotate(step, about_point=center), run_time=1.0)
        self.wait(0.5)

        # update label to 2π and rotate the remaining angle to complete full turn
        self.play(Transform(angle_disp, MathTex(angle_tex("2pi")).move_to(angle_disp)))
        remaining = TAU - 3 * step
        self.play(group.animate.rotate(remaining, about_point=center), run_time=1.2)
        self.wait(0.8)

        self.wait(2)

class Explanation(Scene):
    def construct(self):
        # --- Explanatory block ---
        explanation = VGroup(
            Tex(
                "And not just that one! We could rotate by "
                r"$\tfrac{4\pi}{n}$, $\tfrac{6\pi}{n}$, all the way to $2\pi$."
                "\nEach of these rotations is part of a group.",
                font_size=26),
            MathTex(
                r"R_k \;=\; e^{i \tfrac{2\pi k}{n}}, \quad k = 0,1,\dots,n-1.",
                font_size=36
            ),
            Tex("then applying any group element $R_j$ gives", font_size=26),
            MathTex(r"R_j S = S \quad \text{for all } j.", font_size=36),
            Tex("Therefore,", font_size=26),
            MathTex(r"S = 0.", font_size=44).set_color(YELLOW)
        ).arrange(DOWN, buff=0.4).scale(1.5)

        # Show the block
        self.play(FadeIn(explanation[0]))
        self.wait(3)
        self.play(FadeIn(explanation[1]))
        self.wait()
        self.play(FadeIn(explanation[2:]))
        self.wait()

class MatrixExplanation(Scene):
    def construct(self):
        # --- Explanatory block: matrix version ---
        explanation = VGroup(
            Tex(
                "We can do the exact same thing with ",
                r"\textbf{matrix transformations}.",
                font_size=26
            ),
            Tex(
                "To rotate a vector by an angle $\\theta$, we use the rotation matrix:",
                font_size=26
            ),
            MathTex(
                r"R(\theta) = "
                r"\begin{bmatrix}"
                r"\cos\theta & -\sin\theta \\"
                r"\sin\theta & \cos\theta"
                r"\end{bmatrix}",
                font_size=36
            ),
            Tex("And just like before, we can build a whole collection of these rotations.", font_size=26),
            MathTex(
                r"R_k \;=\; R\!\left(\tfrac{2k\pi}{n}\right), \quad k = 0,1,\dots,n-1.",
                font_size=36
            ),
            Tex(
                "This collection forms a ",
                r"\textbf{group}",
                " --- which mathematicians call $SO(2)$.",
                font_size=26
            ),
        ).arrange(DOWN, buff=0.4).scale(1.5)

        # Show in the same staged style as your Explanation scene
        self.play(FadeIn(explanation[0]))
        self.wait(3)
        self.play(FadeIn(explanation[1:3]))
        self.wait()
        self.play(FadeIn(explanation[3:]))
        self.wait()

import numpy as np

# --- Helpers ---
def rot_z(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0],
                     [s,  c, 0],
                     [0,  0, 1]], dtype=float)

def rot_cycle_xyz():  # 120° about axis (1,1,1) via coordinate cycle (x,y,z)->(y,z,x)
    return np.array([[0,1,0],
                     [0,0,1],
                     [1,0,0]], dtype=float)

def rodriques(u, theta):
    # u must be unit 3-vector; returns 3x3 rotation matrix about u by theta
    ux, uy, uz = u
    K = np.array([[0,   -uz,  uy],
                  [uz,   0,  -ux],
                  [-uy, ux,   0]], dtype=float)
    I = np.eye(3)
    return I + np.sin(theta)*K + (1-np.cos(theta))*(K @ K)

class TetrahedronVectors(ThreeDScene):
    def construct(self):
        # Regular tetrahedron vertices
        verts = [
            np.array([1,  1,  1]),
            np.array([-1, -1,  1]),
            np.array([-1,  1, -1]),
            np.array([1, -1, -1]),
        ]

        # Axes
        axes = ThreeDAxes(x_range=[-1.5, 1.5],
                          y_range=[-1.5, 1.5],
                          z_range=[-1.5, 1.5])
        self.add(axes)

        # Lines/vectors
        arrows = VGroup(*[
            Arrow3D(ORIGIN, v, color=BLUE)
            for v in verts
        ])
        dots = VGroup(*[Dot3D(point=v, radius=0.06, color=YELLOW) for v in verts])
        labels = VGroup(*[
            MathTex(f"v_{i+1}", font_size=36).move_to(1.15*verts[i])
            for i in range(4)
        ])

        tetra = VGroup(arrows, dots, labels)
        self.add(tetra)

        # Set camera so all 4 vertices are visible
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES, distance=6)

        # --- Rotation 1: 120° about axis through v1 (cycles v2,v3,v4) ---
        self.play(Rotate(tetra, angle=120*DEGREES, axis=verts[0], about_point=ORIGIN), run_time=4)
        self.wait(1)

        # --- Rotation 2: 180° about axis through midpoints of edges (swaps pairs) ---
        swap_axis = verts[0] + verts[1]  # axis parallel to edge midpoint line
        self.play(Rotate(tetra, angle=180*DEGREES, axis=swap_axis, about_point=ORIGIN), run_time=4)
        self.wait(1)
        self.add(arrows)
        self.wait(1)

class PlatonicSolidLabels(Scene):
    def construct(self):
        SHOW_GUIDES = False

        # List of solids with both n and name
        solids = [
            ("n = 4", "Tetrahedron"),
            ("n = 5", "Triangular Bipyramid"),
            ("n = 6", "Octahedron"),
            ("n = 12", "Dodecahedron"),
            ("n = 20", "Icosahedron"),
        ]

        box_w, box_h = 3.2, 3.2
        cells = []

        for n_label, name in solids:
            box = Rectangle(
                width=box_w,
                height=box_h,
                stroke_opacity=0.15 if SHOW_GUIDES else 0.0,
                fill_opacity=0.0,
            )

            n_text = Tex(n_label, font_size=34)
            name_text = Tex(name, font_size=34)
            labels = VGroup(n_text, name_text).arrange(DOWN, buff=0.15).scale(0.8)
            labels.next_to(box, DOWN, buff=0.3)

            cells.append(VGroup(box, labels))

        # Arrange: top row 3 solids, bottom row 2 solids
        top_row = VGroup(*cells[:3]).arrange(RIGHT, buff=1.0)
        bottom_row = VGroup(*cells[3:]).arrange(RIGHT, buff=1.0)

        layout = VGroup(top_row, bottom_row).arrange(DOWN, buff=1.0)

        # Scale and center so everything is visible
        layout.scale_to_fit_height(config.frame_height - 1.0)
        layout.move_to(ORIGIN)

        self.play(FadeIn(layout, shift=0.2*UP), run_time=0.6)
        self.wait()

class GroupTheorySlide(Scene):
    def construct(self):
        # Title + definition (start centered)
        title = MathTex(
            r'\text{\textbf{Group Theory}}',
            font_size=52
        )
        subtitle = MathTex(
            r'\text{The branch of mathematics that studies symmetry.}',
            font_size=36
        )
        header = VGroup(title, subtitle).arrange(DOWN, buff=0.35)

        # Optional: color flair
        title.set_color_by_gradient(PURPLE, BLUE)
        subtitle.set_color(GRAY_A)

        # Show the slide
        self.play(FadeIn(header, shift=0.3*UP), run_time=1)
        self.wait(3)        
        header.generate_target()
        header.target.to_edge(UP, buff=0.5)  # move whole group to top
        self.play(MoveToTarget(header), run_time=1)
        self.wait(2)

class PermutationScene(Scene):
    def construct(self):
        # --- Header: R in SO(3)
        header = MathTex(r"R \in \mathrm{SO}(3)").to_edge(UP, buff=0.8)
        self.play(FadeIn(header, shift=0.2*UP), run_time=0.6)

        # --- Define S
        S_def = MathTex("S", "=", "v_1", "+", "v_2", "+", "v_3", "+", "v_4")
        S_def.next_to(header, DOWN, buff=0.8)
        self.play(Write(S_def), run_time=0.9)
        self.wait(0.3)

        # --- First rotation: R1 permutes (2 3 4)
        # R1·S = v1 + v3 + v4 + v2  ->  R1·S = S
        expr1 = MathTex(r"R_1\!\cdot\! S", "=", "v_1", "+", "v_3", "+", "v_4", "+", "v_2")
        expr1.next_to(S_def, DOWN, buff=0.9)

        note1 = Tex(r"(vertices permuted)").scale(0.6).next_to(expr1, RIGHT, buff=0.4)
        self.play(Write(expr1), FadeIn(note1, shift=0.1*RIGHT), run_time=1.0)

        expr1_toS = MathTex(r"R_1\!\cdot\! S", "=", "S").move_to(expr1.get_center())
        self.play(TransformMatchingTex(expr1, expr1_toS), FadeOut(note1), run_time=0.9)
        self.wait(0.4)

        # --- Second rotation: R2 permutes as a disjoint swap (example: (12)(34))
        # R2·S = v2 + v1 + v4 + v3  ->  R2·S = S
        expr2 = MathTex(r"R_2\!\cdot\! S", "=", "v_2", "+", "v_1", "+", "v_4", "+", "v_3")
        expr2.next_to(expr1_toS, DOWN, buff=0.7)

        note2 = Tex(r"(vertices permuted)").scale(0.6).next_to(expr2, RIGHT, buff=0.4)
        self.play(Write(expr2), FadeIn(note2, shift=0.1*RIGHT), run_time=1.0)

        expr2_toS = MathTex(r"R_2\!\cdot\! S", "=", "S").move_to(expr2.get_center())
        self.play(TransformMatchingTex(expr2, expr2_toS), FadeOut(note2), run_time=0.9)
        self.wait(0.6)

        # --- Closing remark (optional)
        concl = Tex(r"Thus, for every $R \in \mathrm{SO}(3) , R S = S$.")
        concl.scale(0.85).next_to(expr2_toS, DOWN, buff=0.8)
        self.play(FadeIn(concl, shift=0.2*UP), run_time=0.7)
        self.wait(0.8)
        concl2 = Tex(r"Since permutations preserve the sum, S = 0.")
        concl2.scale(0.85).next_to(concl, DOWN, buff=0.8)
        self.play(FadeIn(concl2, shift=0.2*UP), run_time=0.7)
        self.wait(0.8)
