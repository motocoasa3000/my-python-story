import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_piano(num_octaves=2):
    fig, ax = plt.subplots(figsize=(num_octaves * 2, 3))

    # White and black key dimensions
    white_key_width = 1
    white_key_height = 2
    black_key_width = 0.6
    black_key_height = 1.4

    # Set limits and remove axis
    ax.set_xlim(0, num_octaves * 7)
    ax.set_ylim(0, white_key_height)
    ax.axis('off')

    # Draw white keys
    for i in range(num_octaves * 7):
        rect = patches.Rectangle(
            (i * white_key_width, 0),
            white_key_width, white_key_height,
            edgecolor='black', facecolor='white',
            lw=1, zorder=0
        )
        ax.add_patch(rect)

    # Black key positions in an octave: 1(C#), 2(D#), 4(F#), 5(G#), 6(A#)
    black_key_positions = [1, 2, 4, 5, 6]

    # Draw black keys
    for octave in range(num_octaves):
        for pos in black_key_positions:
            x = (octave * 7 + pos) * white_key_width - black_key_width / 2
            rect = patches.Rectangle(
                (x, white_key_height - black_key_height),
                black_key_width,
                black_key_height,
                edgecolor='black',
                facecolor='black',
                lw=1,
                zorder=1  # Black keys are drawn above white keys
            )
            ax.add_patch(rect)

    # Optional: Add shading or effects to make it more realistic (e.g., a gradient on white keys)
    for i in range(num_octaves * 7):
        # Subtle gradient effect for white keys (light gray to white)
        rect = patches.Rectangle(
            (i * white_key_width, 0),
            white_key_width, white_key_height,
            edgecolor='black', facecolor=(1, 1, 1, 0.9),  # Slight opacity for depth effect
            lw=1, zorder=0
        )
        ax.add_patch(rect)

    # Optional: Highlight middle C (C4) (if desired, based on number of octaves)
    if num_octaves >= 2:
        middle_c_pos = 4  # Middle C is the 4th key in a standard octave
        rect = patches.Rectangle(
            (middle_c_pos * white_key_width, 0),
            white_key_width, white_key_height,
            edgecolor='red', facecolor='yellow', lw=2, zorder=2
        )
        ax.add_patch(rect)

    plt.show()

draw_piano(3)  # Draw a 3-octave keyboard