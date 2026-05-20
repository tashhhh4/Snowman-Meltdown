# Snowman ASCII Art frames

# Stage 0: Full snowman
FRAME_0 = """
           ___
          /___\\
          (o o)
          ( : )
          ( : )
          """

FRAME_00 = """
           ___
          /___\\
          (o o)
          ( : )
         _( : )_
          """

# Stage 1: Bottom part starts melting
FRAME_1 = """
           ___
          /___\\
          (o o)
        __( : )__
          """

FRAME_10 = """
            ___
           /___\\
           ( o o)
       ___( . \\__
          """

# Stage 2: Only the head remains
FRAME_2 = """
            ___
           /___\\
      _____( o -)___
          """

FRAME_20 = """
            ___
           /___\\
     ______( - _\\____
          """

# Stage 3: Snowman completely melted
FRAME_3 = """
            ___
    _______/___\\______
          """


# List of frames => game stages
STAGES_EASY = [FRAME_0, FRAME_00, FRAME_1, FRAME_10, FRAME_2, FRAME_20, FRAME_3]
STAGES_MEDIUM = [FRAME_0, FRAME_1, FRAME_10, FRAME_2, FRAME_3]
STAGES_HARD = [FRAME_0, FRAME_1, FRAME_2, FRAME_3]
