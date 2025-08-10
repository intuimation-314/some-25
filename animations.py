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

class NEqualVectors(Scene):
    def construct(self):
        
        # Set the number of vectors
        n = 9  # Change this value to the desired number of vectors

        tex_lines = [
            "If n equal vectors are lined up",
            "making an angle of $\\frac{2\pi}{n}$ to each",
            "other, then the resultant is 0.",
        ]
        
        # Create text objects
        text_group = VGroup(*[Tex(line) for line in tex_lines if line])
        text_group.arrange(DOWN, aligned_edge=LEFT)
        text_group.move_to(3*RIGHT + UP)  # Move text group to desired position

        formula = MathTex(r"\sum_{n=0}^{k-1}\vec{v}_k = 0").next_to(text_group, DOWN, buff=0.8)
        
        # Create the central object
        obj = Dot(ORIGIN, color=WHITE)
        
        # Angle between the vectors
        angle = 2 * PI / n
        
        # Create and display the vectors
        vectors = [
            Arrow(
                start=obj.get_center(), 
                end=obj.get_center() + np.array([np.cos(k * angle), np.sin(k * angle), 0]) * 2.5, 
                buff=0, 
                color=BLUE,
                stroke_width=2
            ) for k in range(n)
        ]
        forces = VGroup(*vectors)

        # Create arcs and angle labels between vectors, but only show one at a time
        arc = Arc(
            radius=1, 
            start_angle=0, 
            angle=angle, 
            color=YELLOW,
            stroke_width=2
        ).move_arc_center_to(obj.get_center())
        angle_label = MathTex(r"\frac{2\pi}{n}").scale(0.6)
        angle_label.move_to(arc.point_from_proportion(0.5) + 0.5 * UP)

        # Group for initial arc and label
        arc_angle_group = VGroup(arc, angle_label)

        self.play(Create(obj))
        self.play(Create(forces))
        self.wait(1)

        # Animate each arc and label one by one
        for k in range(n):
            new_arc = Arc(
                radius=1,
                start_angle=k * angle,
                angle=angle,
                color=YELLOW,
                stroke_width=2
            ).move_arc_center_to(obj.get_center())

            new_angle_label = MathTex(r"\frac{2\pi}{n}").scale(0.6)
            new_angle_label.move_to(new_arc.point_from_proportion(0.5) + 0.5 * UP)

            new_arc_angle_group = VGroup(new_arc, new_angle_label)
        
            self.play(Transform(arc_angle_group, new_arc_angle_group))
        
        self.wait(1)
        self.play(FadeOut(arc_angle_group))
        self.play(VGroup(obj,forces).animate.shift(LEFT*3.5))
        self.wait(1)
        self.play(Write(text_group))
        self.wait(1)
        self.play(Write(formula))
        self.wait(1)
        self.play(FadeOut(VGroup(text_group, formula)))

        obj1 = Dot().move_to(RIGHT*3)
        # Shift the vectors to form a closed polygon
        closed_polygon_vectors = VGroup()
        for i in range(n):
            if i == 0:
                start = obj1.get_center() + np.array([np.cos(i * angle), np.sin(i * angle), 0]) * 2.5
            else:
                start = end
            end = obj1.get_center() + np.array([np.cos((i + 1) * angle), np.sin((i + 1) * angle), 0]) * 2.5
            closed_polygon_vectors.add(Arrow(start=start, end=end, buff=0, color=BLUE, stroke_width=2))

        for i in range(n):
         self.play(Transform(forces[i].copy(), closed_polygon_vectors[i]))

        # Fade out text and elements
        self.wait(1)
        self.play(FadeOut(forces), FadeOut(obj))
        self.wait(1)

