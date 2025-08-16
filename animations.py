from manim import *
import numpy as np

class ElectronsOnString(Scene):
    def construct(self):
        # math mode + safe \mathbb usage
        title = MathTex(
            r"\mathbb{I}\!\text{ magine tying electrons to the end of strings !}",
            font_size=42
        ).to_edge(UP)
        title.set_color_by_gradient(BLUE, TEAL_E)  # apply gradient safely

        self.play(FadeIn(title, shift=0.3*UP))
        self.wait()
                # Static text part
        label = Tex("Number of electrons =", font_size=32)
        label.next_to(title, DOWN, buff=0.5)

        # Number part
        number = Tex("2", font_size=32)
        number.next_to(label, RIGHT)

        self.play(FadeIn(label), Write(number))
        self.wait(1)

        # Transform numbers only
        for n in ["3", "4"]:
            new_number = Tex(n, font_size=32)
            new_number.move_to(number)  # keep position
            self.play(Transform(number, new_number))
            self.wait(1)
        # center = ORIGIN
        # R = 2.6  # string length
        # center_dot = Dot(center, radius=0.05, color=GRAY_B)

        # # Start angle: electrons both below x-axis
        # sep = ValueTracker(60 * DEGREES)  # small separation
        # base_angle = -90 * DEGREES  # pointing downward

        # def pos1():
        #     a = base_angle + sep.get_value() / 2
        #     return center + R * np.array([np.cos(a), np.sin(a), 0])

        # def pos2():
        #     a = base_angle - sep.get_value() / 2
        #     return center + R * np.array([np.cos(a), np.sin(a), 0])

        # # Strings from center to electrons
        # string1 = always_redraw(lambda: Line(center, pos1(), color=GRAY_A, stroke_width=2.5))
        # string2 = always_redraw(lambda: Line(center, pos2(), color=GRAY_A, stroke_width=2.5))

        # # Electrons
        # e1 = always_redraw(lambda: Dot(pos1(), color=BLUE_E, radius=0.3))
        # e2 = always_redraw(lambda: Dot(pos2(), color=BLUE_E, radius=0.3))
        # minus1 = always_redraw(lambda: MathTex(r"e", color=WHITE).scale(1.1).move_to(pos1()))
        # minus2 = always_redraw(lambda: MathTex(r"e", color=WHITE).scale(1.1).move_to(pos2()))



        # # Build scene
        # self.play(FadeIn(center_dot))
        # self.play(FadeIn(string1, string2, e1, e2, minus1, minus2), run_time=0.6)

        # # Let go: swing up to horizontal (theta = 180°)
        # self.play(sep.animate.set_value(180 * DEGREES), run_time=2.0, rate_func=smooth)

        #         # Angle arc + label
        # theta_arc = always_redraw(
        #     lambda: Angle(string1, string2, radius=0.5, color=YELLOW, other_angle=False)
        # )
        # theta_label = always_redraw(
        #     lambda: MathTex(r"\theta = 180^\circ", color=YELLOW).scale(0.8).next_to(theta_arc, UP, buff=0.15)
        # )

        # self.play(FadeIn(theta_arc, theta_label), run_time=0.8)
        # self.wait(1.2)

        # self.play(*map(FadeOut, [string1, string2, e1, e2, minus1, minus2, theta_label, theta_arc]))
        # self.wait(0.6)

        # #3 electrons scene
        # start_offsets = np.array([-15, 0, 15]) * DEGREES
        # final_offsets = np.array([-120, 0, 120]) * DEGREES
        # spread = ValueTracker(0.0)  # 0 = start, 1 = final

        # def angles():
        #     t = spread.get_value()
        #     offs = start_offsets * (1 - t) + final_offsets * t
        #     return base_angle + offs

        # def pos(k):
        #     a = angles()[k]
        #     return center + R * np.array([np.cos(a), np.sin(a), 0])

        # # Strings & electrons
        # strings = [
        #     always_redraw(lambda k=k: Line(center, pos(k), color=GRAY_A, stroke_width=2.5))
        #     for k in range(3)
        # ]
        # electrons = [
        #     always_redraw(lambda k=k: Dot(pos(k), color=BLUE_E, radius=0.3))
        #     for k in range(3)
        # ]
        # labels = [
        #     always_redraw(lambda k=k: MathTex(r"e", color=WHITE).scale(1.1).move_to(pos(k)))
        #     for k in range(3)
        # ]

        # self.play(*[FadeIn(s) for s in strings],
        #           *[FadeIn(e) for e in electrons],
        #           *[FadeIn(l) for l in labels],
        #           run_time=0.6)

        # # Let go: spread into equilateral triangle (120° apart)
        # self.play(spread.animate.set_value(1.0), run_time=2.0, rate_func=smooth)

        # # Show angle between two adjacent strings
        # theta_arc = always_redraw(
        #     lambda: Angle(strings[0], strings[1], radius=0.5, color=YELLOW, other_angle=False)
        # )
        # theta_label = always_redraw(
        #     lambda: MathTex(r"\theta = 120^\circ", color=YELLOW).scale(0.8).next_to(theta_arc, UP, buff=0.15)
        # )

        # self.play(FadeIn(theta_arc, theta_label), run_time=0.8)
        # self.wait(1.2)

        # self.play(*map(FadeOut, [*strings, *electrons, *labels, theta_label, theta_arc]))
        # self.wait(0.6)

        # #Four Electrons
        # start_offsets = np.array([-15, -5, 5, 15]) * DEGREES
        # final_offsets = np.array([-135, -45, 45, 135]) * DEGREES  # 90° apart
        # spread = ValueTracker(0.0)

        # def angles():
        #     t = spread.get_value()
        #     offs = start_offsets * (1 - t) + final_offsets * t
        #     return base_angle + offs

        # def pos(k):
        #     a = angles()[k]
        #     return center + R * np.array([np.cos(a), np.sin(a), 0])

        # strings = [
        #     always_redraw(lambda k=k: Line(center, pos(k), color=GRAY_A, stroke_width=2.5))
        #     for k in range(4)
        # ]
        # electrons = [
        #     always_redraw(lambda k=k: Dot(pos(k), color=BLUE_E, radius=0.3))
        #     for k in range(4)
        # ]
        # labels = [
        #     always_redraw(lambda k=k: MathTex(r"e", color=WHITE).scale(1.1).move_to(pos(k)))
        #     for k in range(4)
        # ]

        # self.play(*[FadeIn(s) for s in strings],
        #           *[FadeIn(e) for e in electrons],
        #           *[FadeIn(l) for l in labels],
        #           run_time=0.6)

        # self.play(spread.animate.set_value(1.0), run_time=2.0, rate_func=smooth)

        # theta_arc = always_redraw(
        #     lambda: Angle(strings[0], strings[1], radius=0.5, color=YELLOW, other_angle=False)
        # )
        # theta_label = always_redraw(
        #     lambda: MathTex(r"\theta = 90^\circ", color=YELLOW).scale(0.8).next_to(theta_arc, UP, buff=0.15)
        # )

        # self.play(FadeIn(theta_arc, theta_label), run_time=0.8)
        # self.wait(1.2)

        # self.play(*map(FadeOut, [*strings, *electrons, *labels, theta_label, theta_arc]))
        # self.wait(0.6)

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


class GalileoQuote1(Scene):
    def construct(self):
        # --- main quote with per-line colors ---
        quote = VGroup(
            Tex(
                r"\textit{``Philosophy is written in this grand book---I mean the universe---which stands continually open to our gaze.}",
                tex_environment="flushleft",
                font_size=36,
            ),
            Tex(
                r"\textit{But it cannot be understood unless one first learns to comprehend the language and interpret the characters in which it is written.}",
                tex_environment="flushleft",
                font_size=36,
                color=BLUE,
            ),
            Tex(
                r"\textit{It is written in the language of mathematics, and its characters are triangles, circles, and other geometrical figures,}",
                tex_environment="flushleft",
                font_size=36,
            ), 
            Tex(
                r"\textit{without which it is humanly impossible to understand a single word of it.''}",
                tex_environment="flushleft",
                font_size=36,
                color=WHITE,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(LEFT).shift(UP*0.5)

        # --- emphasize key words inside the colored lines ---
        quote[2].set_color_by_tex("mathematics", YELLOW)
        quote[2].set_color_by_tex("triangles", TEAL)
        quote[2].set_color_by_tex("circles", BLUE)
        quote[2].set_color_by_tex("geometrical figures", GREEN)

        # --- author attribution ---
        author = Tex(
            r"\textbf{ - Galileo Galilei}, \textit{Il Saggiatore} (The Assayer), 1623",
            font_size=30,
            color=WHITE,
        )
        author.next_to(quote, DOWN, buff=0.5)
        author.align_to(quote, RIGHT)

        # --- decorative geometry ---
        circle = Circle(radius=1.2, color=BLUE_E).set_stroke(width=3, opacity=0.15)
        tri = RegularPolygon(3, radius=1.1).set_stroke(color=TEAL_E, width=3, opacity=0.15)
        geo = VGroup(circle, tri).arrange(RIGHT, buff=0.5)
        geo.move_to(quote.get_center() + 3.0*RIGHT + 0.3*UP)
        geo.set_z_index(-1)

        # --- animation ---
        for line in quote:
            self.play(FadeIn(line), run_time=1.2)
        self.play(FadeIn(geo, shift=UP*0.2), run_time=0.8)
        self.play(Write(author), run_time=0.8)
        self.wait(2)

class SymmetryTemplate(Scene):
    def construct(self):
        # Titles
        title = MathTex(
            r'\text{``Symmetry is everywhere in nature``}',
            font_size=48
        ).set_color_by_gradient(BLUE, GREEN)

        title2 = MathTex(
            r'\text{``And inspired by nature, we humans design:``}',
            font_size=48
        ).set_color_by_gradient(BLUE, GREEN)

        # First title
        self.play(FadeIn(title))
        self.play(title.animate.to_edge(UP))
        self.wait(0.5)

        # First set of captions
        captions = [
            (
                MathTex(r"\mathrm{BF_3\ (Trigonal\ Planar)}", font_size=28),
                MathTex(r"\mathrm{CH_4\ (Tetrahedral)}", font_size=28)
            ),
            (
                MathTex(r"\mathrm{Charged\ Ring\ (2D)}", font_size=28),
                MathTex(r"\mathrm{Charged\ Sphere\ (3D)}", font_size=28)
            ),
            (
                MathTex(r"\mathrm{Water\ Droplets, Ripples}", font_size=28),
                MathTex(r"\mathrm{Snowflakes(Hexagonal)}", font_size=28)
            )
        ]

        captions2 = [
            (
                MathTex(r"\mathrm{Fan\ Blades}", font_size=28),
                MathTex(r"\mathrm{Turbines}", font_size=28)
            ),
            (
                MathTex(r"\mathrm{Speaker\ Cones}", font_size=28),
                MathTex(r"\mathrm{Satellite\ Dishes}", font_size=28)
            ),
            (
                MathTex(r"\mathrm{Domes}", font_size=28),
                MathTex(r"\mathrm{Arches}", font_size=28)
            )
        ]

        # Initialize empty captions for first set
        bottom_left = MathTex("", font_size=28).to_corner(DL).shift(2*RIGHT)
        bottom_right = MathTex("", font_size=28).to_corner(DR).shift(2*LEFT)
        self.add(bottom_left, bottom_right)

        # Play first captions
        for left_caption, right_caption in captions:
            left_caption.to_corner(DL).shift(1.5*RIGHT + UP)
            right_caption.to_corner(DR).shift(1.5*LEFT + UP)
            self.play(
                Transform(bottom_left, left_caption),
                Transform(bottom_right, right_caption)
            )
            self.wait(2)

        # Fade out everything from first part
        self.play(FadeOut(title), FadeOut(bottom_left), FadeOut(bottom_right))
        self.wait(0.5)

        # Second title
        self.play(FadeIn(title2))
        self.play(title2.animate.to_edge(UP))
        self.wait(0.5)

        # Reset captions for second set
        bottom_left2 = MathTex("", font_size=28).to_corner(DL).shift(2*RIGHT)
        bottom_right2 = MathTex("", font_size=28).to_corner(DR).shift(2*LEFT)
        self.add(bottom_left2, bottom_right2)

        # Play second captions
        for left_caption, right_caption in captions2:
            left_caption.to_corner(DL).shift(1.5*RIGHT + UP)
            right_caption.to_corner(DR).shift(1.5*LEFT + UP)
            self.play(
                Transform(bottom_left2, left_caption),
                Transform(bottom_right2, right_caption)
            )
            self.wait(2)

        self.wait(1)

class ThomsonSlide(Scene):
    def construct(self):
        # Title + question (start centered)
        title = MathTex(
            r'\text{\textbf{Thomson problem}}',
            font_size=52
        )
        subtitle = MathTex(
            r'\text{How do multiple electrons arrange themselves on the surface of a sphere?}',
            font_size=36
        )
        header = VGroup(title, subtitle).arrange(DOWN, buff=0.35)

        # Optional: color flair
        title.set_color_by_gradient(BLUE, TEAL)
        subtitle.set_color(GRAY_A)

        self.play(FadeIn(header, shift=0.3*UP), run_time=1.0)
        self.wait(0.5)

        # Move header to the top
        self.play(header.animate.to_edge(UP), run_time=0.9)
        self.wait(0.2)

        # Captions: appear at the same time (DL, bottom-center, DR)
        cap_left  = MathTex(r"\mathrm{n=4}", font_size=30).to_corner(DL).shift(RIGHT*1.2 + UP*0.6)
        cap_mid   = MathTex(r"\mathrm{n=5}", font_size=30).to_edge(DOWN).shift(UP*0.6)
        cap_right = MathTex(r"\mathrm{n=6}", font_size=30).to_corner(DR).shift(LEFT*1.2 + UP*0.6)

        self.play(
            Write(cap_left),
            Write(cap_mid),
            Write(cap_right),
            run_time=0.8
        )
        self.wait(2)

        # (Optional) If you want to fade out at the end:
        self.play(FadeOut(header), FadeOut(cap_left), FadeOut(cap_mid), FadeOut(cap_right))
        self.wait(0.3)

class Image(Scene):
    def construct(self):
        # Load an image from file
        img = ImageMobject("snowflake.jpg")  # replace with your file path
        img.scale(2)  # optional scaling
        self.add(img)

        # Rotate slowly over 10 seconds
        self.play(Rotate(img, angle=TAU, run_time=10, rate_func=linear))
        self.wait()

class Fan(Scene):
    def construct(self):
        # Load an image from file
        img = ImageMobject("fan.png")  # replace with your file path
        img.scale(2)  # optional scaling
        self.add(img)

        # Rotate slowly over 10 seconds
        self.play(Rotate(img, angle=TAU, run_time=10, rate_func=linear))
        self.wait()

class ThinkingMuBot(Scene):
    def construct(self):
        title = MathTex(
            r'\text{``Symmetry brings balance in nature``}',
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

        tex1 = Tex("Impossible to prove in a", "purely philosophical sense !").scale(0.8).arrange(DOWN).move_to(thinking_cloud.get_center())
        tex2 = Tex("\"balance\" = equilibrium")
        tex2.arrange(DOWN)

        tex2.scale(0.8).move_to(thinking_cloud.get_center())
        self.play(FadeIn(VGroup(dot1, dot2, dot3, thinking_cloud)))
        self.play(Write(tex1))
        self.play(Transform(tex1, tex2))
        self.wait(2)
        # self.add(title, dot1, dot2, dot3, thinking_cloud)

class MuBot(Scene):
    def construct(self):
        # Mu symbol as the body of the bot
        mu = MathTex(r"\mu").scale(5).set_color(BLUE).shift(LEFT + DOWN)
        
        # Eyes: Create two small white circles with black pupils
                # Eyes: Create two white ovals for the eyes
        left_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 1.25 + DOWN)
        right_eye_white = Ellipse(width=0.3, height=0.4, color=WHITE, fill_opacity=1).shift(UP * 0.6 + LEFT * 0.65 + DOWN)
        left_eye_pupil = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.1, color=BLACK)
        right_eye_pupil = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.1, color=BLACK)
        
        # Add small circle in the middle of each pupil
        left_eye_glint = Dot(point=UP * 0.6 + LEFT * 1.25 + DOWN, radius=0.03, color=WHITE, fill_opacity=0.8)
        right_eye_glint = Dot(point=UP * 0.6 + LEFT * 0.65 + DOWN, radius=0.03, color=WHITE,fill_opacity=0.8)
        
        # Group the eyes for easy animation
        eyes = VGroup(left_eye_white, right_eye_white, 
                      left_eye_pupil, right_eye_pupil,
                      left_eye_glint,right_eye_glint)

        # Assemble the bot
        mu_bot = VGroup(mu, eyes)


        # Mouth (arc for different moods)
        happy_mouth = Arc(radius=0.2, 
                          start_angle= - 3* PI/4,
                          angle= 2 * PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT)
        sad_mouth = Arc(radius=0.2, start_angle= PI/4,
                        angle= 2 *PI/4).set_color(WHITE).move_to(DOWN * 0.9 + LEFT)
        thinking_mouth = Line(start=LEFT * 0.15 + DOWN * 0.9 + LEFT, 
                              end=RIGHT * 0.15 + DOWN * 0.9 + LEFT).set_color(WHITE)
        mu_bot_happy = VGroup(mu_bot,happy_mouth)
        mu_bot_sad = VGroup(mu_bot,sad_mouth)
        mu_bot_thinking = VGroup(mu_bot,thinking_mouth)

        # Blinking effect using fade-in and fade-out
        def blink():
            return AnimationGroup(
                FadeOut(left_eye_pupil,right_eye_pupil,
                        left_eye_glint,right_eye_glint),
                FadeIn(left_eye_pupil,right_eye_pupil,
                       left_eye_glint,right_eye_glint),
                lag_ratio=0.2,
            )

        
        # Intro Animation
        self.play(FadeIn(mu_bot_thinking), run_time=1.5)
        # Blinking Animation
        self.play(blink(), run_time=0.5)
        self.wait(0.5)
        self.play(blink(), run_time=0.5)
        self.wait(1)
    
        # Blinking Animation
        self.play(blink(), run_time=0.5)
        self.wait(0.5)
        self.play(blink(), run_time=0.5)
        self.wait(1)
                
        self.play(ReplacementTransform(mu_bot_thinking, mu_bot_happy), run_time=1)
        # Blinking Animation
        self.play(blink(), run_time=0.5)
        self.wait(0.5)
        self.play(blink(), run_time=0.5)
        self.wait(2)

        self.play(ReplacementTransform(mu_bot_happy, mu_bot_sad), run_time=1)
        # Blinking Animation
        self.play(blink(), run_time=0.5)
        self.wait(0.5)
        self.play(blink(), run_time=0.5)
        self.wait(2)

        self.play(ReplacementTransform(mu_bot_sad, mu_bot_thinking), run_time=1)
        # Blinking Animation
        self.play(blink(), run_time=0.5)
        self.wait(0.5)
        self.play(blink(), run_time=0.5)
        self.wait(2)

       