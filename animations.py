from manim import *
import numpy as np

class ElectronsOnString(Scene):
    def construct(self):
        # Black background + title
        self.camera.background_color = BLACK
        title = Text(
            "Imagine tying electrons to the end of strings !",
            gradient=(BLUE, TEAL),
            font_size=36
        ).to_edge(UP)   

        self.play(FadeIn(title, shift=0.3*UP))

        center = ORIGIN
        R = 2.6  # string length
        center_dot = Dot(center, radius=0.05, color=GRAY_B)

        # Start angle: electrons both below x-axis
        sep = ValueTracker(60 * DEGREES)  # small separation
        base_angle = -90 * DEGREES  # pointing downward

        def pos1():
            a = base_angle + sep.get_value() / 2
            return center + R * np.array([np.cos(a), np.sin(a), 0])

        def pos2():
            a = base_angle - sep.get_value() / 2
            return center + R * np.array([np.cos(a), np.sin(a), 0])

        # Strings from center to electrons
        string1 = always_redraw(lambda: Line(center, pos1(), color=GRAY_A, stroke_width=2.5))
        string2 = always_redraw(lambda: Line(center, pos2(), color=GRAY_A, stroke_width=2.5))

        # Electrons
        e1 = always_redraw(lambda: Dot(pos1(), color=BLUE_E, radius=0.3))
        e2 = always_redraw(lambda: Dot(pos2(), color=BLUE_E, radius=0.3))
        minus1 = always_redraw(lambda: MathTex(r"e", color=WHITE).scale(1.1).move_to(pos1()))
        minus2 = always_redraw(lambda: MathTex(r"e", color=WHITE).scale(1.1).move_to(pos2()))



        # Build scene
        self.play(FadeIn(center_dot))
        self.play(FadeIn(string1, string2, e1, e2, minus1, minus2), run_time=0.6)

        # Let go: swing up to horizontal (theta = 180°)
        self.play(sep.animate.set_value(180 * DEGREES), run_time=2.0, rate_func=smooth)

                # Angle arc + label
        theta_arc = always_redraw(
            lambda: Angle(string1, string2, radius=0.5, color=YELLOW, other_angle=False)
        )
        theta_label = always_redraw(
            lambda: MathTex(r"\theta = 180^\circ", color=YELLOW).scale(0.8).next_to(theta_arc, UP, buff=0.15)
        )

        self.play(FadeIn(theta_arc, theta_label), run_time=0.8)
        self.wait(1.2)

        self.play(*map(FadeOut, [string1, string2, e1, e2, minus1, minus2, theta_label, theta_arc]))
        self.wait(0.6)

        #3 electrons scene
        start_offsets = np.array([-15, 0, 15]) * DEGREES
        final_offsets = np.array([-120, 0, 120]) * DEGREES
        spread = ValueTracker(0.0)  # 0 = start, 1 = final

        def angles():
            t = spread.get_value()
            offs = start_offsets * (1 - t) + final_offsets * t
            return base_angle + offs

        def pos(k):
            a = angles()[k]
            return center + R * np.array([np.cos(a), np.sin(a), 0])

        # Strings & electrons
        strings = [
            always_redraw(lambda k=k: Line(center, pos(k), color=GRAY_A, stroke_width=2.5))
            for k in range(3)
        ]
        electrons = [
            always_redraw(lambda k=k: Dot(pos(k), color=BLUE_E, radius=0.3))
            for k in range(3)
        ]
        labels = [
            always_redraw(lambda k=k: MathTex(r"e", color=WHITE).scale(1.1).move_to(pos(k)))
            for k in range(3)
        ]

        self.play(*[FadeIn(s) for s in strings],
                  *[FadeIn(e) for e in electrons],
                  *[FadeIn(l) for l in labels],
                  run_time=0.6)

        # Let go: spread into equilateral triangle (120° apart)
        self.play(spread.animate.set_value(1.0), run_time=2.0, rate_func=smooth)

        # Show angle between two adjacent strings
        theta_arc = always_redraw(
            lambda: Angle(strings[0], strings[1], radius=0.5, color=YELLOW, other_angle=False)
        )
        theta_label = always_redraw(
            lambda: MathTex(r"\theta = 120^\circ", color=YELLOW).scale(0.8).next_to(theta_arc, UP, buff=0.15)
        )

        self.play(FadeIn(theta_arc, theta_label), run_time=0.8)
        self.wait(1.2)

        self.play(*map(FadeOut, [*strings, *electrons, *labels, theta_label, theta_arc]))
        self.wait(0.6)

        #Four Electrons
        start_offsets = np.array([-15, -5, 5, 15]) * DEGREES
        final_offsets = np.array([-135, -45, 45, 135]) * DEGREES  # 90° apart
        spread = ValueTracker(0.0)

        def angles():
            t = spread.get_value()
            offs = start_offsets * (1 - t) + final_offsets * t
            return base_angle + offs

        def pos(k):
            a = angles()[k]
            return center + R * np.array([np.cos(a), np.sin(a), 0])

        strings = [
            always_redraw(lambda k=k: Line(center, pos(k), color=GRAY_A, stroke_width=2.5))
            for k in range(4)
        ]
        electrons = [
            always_redraw(lambda k=k: Dot(pos(k), color=BLUE_E, radius=0.3))
            for k in range(4)
        ]
        labels = [
            always_redraw(lambda k=k: MathTex(r"e", color=WHITE).scale(1.1).move_to(pos(k)))
            for k in range(4)
        ]

        self.play(FadeIn(center_dot))
        self.play(*[FadeIn(s) for s in strings],
                  *[FadeIn(e) for e in electrons],
                  *[FadeIn(l) for l in labels],
                  run_time=0.6)

        self.play(spread.animate.set_value(1.0), run_time=2.0, rate_func=smooth)

        theta_arc = always_redraw(
            lambda: Angle(strings[0], strings[1], radius=0.5, color=YELLOW, other_angle=False)
        )
        theta_label = always_redraw(
            lambda: MathTex(r"\theta = 90^\circ", color=YELLOW).scale(0.8).next_to(theta_arc, UP, buff=0.15)
        )

        self.play(FadeIn(theta_arc, theta_label), run_time=0.8)
        self.wait(1.2)

        self.play(*map(FadeOut, [*strings, *electrons, *labels, theta_label, theta_arc]))
        self.wait(0.6)

class FourElectronsTetrahedron3D(ThreeDScene):
    def construct(self):
        # Black background + gradient title
        self.camera.background_color = BLACK
        title = Text(
            "Imagine tying electrons to the end of strings !",
            gradient=(BLUE, TEAL),
            font_size=36
        ).to_edge(UP)
        self.play(FadeIn(title, shift=0.3*UP))

        center = ORIGIN
        R = 2.6
        center_dot = Dot(center, radius=0.05, color=GRAY_B)

        # Final tetrahedral directions: pairwise dot = -1/3 => angle ≈ 109.47°
        final_dirs = np.array([
            [ 1,  1,  1],
            [ 1, -1, -1],
            [-1,  1, -1],
            [-1, -1,  1],
        ], dtype=float)
        final_dirs = final_dirs / np.linalg.norm(final_dirs, axis=1)[:, None]

        # Start directions: bias them downward so they "rise" into tetrahedron
        start_dirs = final_dirs + np.array([0, 0, -3.0])
        start_dirs = start_dirs / np.linalg.norm(start_dirs, axis=1)[:, None]

        t = ValueTracker(0.0)  # 0 -> start, 1 -> tetrahedron

        def dir_k(k):
            d = (1 - t.get_value()) * start_dirs[k] + t.get_value() * final_dirs[k]
            return d / np.linalg.norm(d)

        def pos_k(k):
            return center + R * dir_k(k)

        # Strings and electrons
        strings = [
            always_redraw(lambda k=k: Line3D(center, pos_k(k), color=GRAY_A, stroke_width=2.5))
            for k in range(4)
        ]
        electrons = [
            always_redraw(lambda k=k: Dot3D(pos_k(k), color=BLUE_E, radius=0.08))
            for k in range(4)
        ]
        labels = [
            always_redraw(lambda k=k: MathTex(r"e", color=WHITE).scale(0.9).move_to(pos_k(k)))
            for k in range(4)
        ]

        # Optional edges to reveal the tetrahedron (6 edges)
        def edge(i, j):
            return always_redraw(lambda i=i, j=j: Line3D(pos_k(i), pos_k(j), color=YELLOW, stroke_width=2))

        edges = [edge(0,1), edge(0,2), edge(0,3), edge(1,2), edge(1,3), edge(2,3)]

        self.play(FadeIn(center_dot))
        self.play(*[FadeIn(s) for s in strings],
                  *[FadeIn(e) for e in electrons],
                  *[FadeIn(l) for l in labels],
                  run_time=0.6)

        # Camera setup + start slow rotation
        self.set_camera_orientation(phi=70*DEGREES, theta=-45*DEGREES, zoom=1.0)
        self.begin_ambient_camera_rotation(rate=0.15)

        # Animate into tetrahedral arrangement
        self.play(t.animate.set_value(1.0), run_time=2.0, rate_func=smooth)

        # Show angle label (tetrahedral angle)
        theta_label = MathTex(r"\theta \approx 109.5^\circ", color=YELLOW).scale(0.8).next_to(title, DOWN)
        self.play(FadeIn(theta_label), run_time=0.6)

        # Draw edges to make the tetrahedron clear
        self.play(*[Create(ed) for ed in edges], run_time=0.8)
        self.wait(1.4)

        # Clean up
        self.stop_ambient_camera_rotation()
        self.play(*map(FadeOut, [theta_label, *edges, *strings, *electrons, *labels]))
        self.wait(0.4)

