import cv2

def draw_info_button(frame, language):
    button_size = 50
    button_margin = 10
    button_color = (100, 100, 100, 128)  # Semi-transparent grey color (BGRA format)
    button_font_scale = 0.6
    button_font_color = (255, 255, 255)

    # Draw circular button at the top-right corner
    cv2.rectangle(frame, (button_margin, button_margin), (button_margin + button_size, button_margin + button_size),
                  button_color, -1, cv2.LINE_AA)

    cv2.putText(frame, 'i', (button_margin + 15, button_margin + 35), cv2.FONT_HERSHEY_SIMPLEX,
                button_font_scale, button_font_color, 1, cv2.LINE_AA)

    # Draw rectangular button at the top-left corner
    cv2.rectangle(frame, (button_margin, button_margin), (button_margin + button_size * 2, button_margin + button_size),
                  button_color, -1, cv2.LINE_AA)

    if language == True:
        lang = 'DE'
    else:
        lang = 'ENG'
    cv2.putText(frame, lang, (button_margin + 5, button_margin + 35), cv2.FONT_HERSHEY_SIMPLEX,
                button_font_scale, button_font_color, 1, cv2.LINE_AA)
    # Create a button layer with a semi-transparent grey background
    button_layer = frame.copy()
    button_radius = 30
    button_center = (frame.shape[1] - button_radius - 10, button_radius + 10)
    button_color = (150, 150, 150)  # Semi-transparent grey color (BGR format)
    cv2.circle(button_layer, button_center, button_radius, button_color, -1)

    # Draw a black drop-shadow behind the button
    shadow_offset = 3
    shadow_color = (0, 0, 0)  # Black color (BGR format)
    cv2.circle(button_layer, (button_center[0] + shadow_offset, button_center[1] + shadow_offset),
               button_radius, shadow_color, -1)

    # Combine the button layer with the original frame
    alpha = 0.8  # Adjust the transparency as needed
    cv2.addWeighted(button_layer, alpha, frame, 1 - alpha, 0, frame)

    # Draw the 'i' symbol at the center of the circle
    i_text = "i"
    i_font_scale = 1.2
    i_font_color = (255, 255, 255)
    i_text_size = cv2.getTextSize(i_text, cv2.FONT_HERSHEY_SIMPLEX, i_font_scale, 1)[0]
    i_text_x = button_center[0] - i_text_size[0] // 2
    i_text_y = button_center[1] + i_text_size[1] // 2
    cv2.putText(frame, i_text, (i_text_x, i_text_y), cv2.FONT_HERSHEY_SIMPLEX,
                i_font_scale, i_font_color, 2, cv2.LINE_AA)

def draw_info_overlay(frame, language):
    overlay = frame.copy()

    # Draw a semi-transparent grey rectangle overlay
    rectangle_color = (100, 100, 100, 128)  # Semi-transparent grey color (BGRA format)
    cv2.rectangle(overlay, (100, 100), (frame.shape[1] - 100, frame.shape[0] - 100), rectangle_color, -1)

    # Text to be displayed with wrapping
    if language == True:
        text = "AllerSee is a lake whose biodiversity is in peril due to the unreliable exchange of fresh water. The most critical element for life, oxygen, is provided solely by rainfall. Take the cup you see on your right and MAKE IT RAIN! Save the fish! Save the lake!"
    else:
        text = "Der AllerSee ist ein See, dessen Artenvielfalt durch den unzuverlässigen Austausch von Süßwasser gefährdet ist. Das wichtigste Element für das Leben, der Sauerstoff, wird ausschließlich durch Regenfälle bereitgestellt. Nimm die Tasse, die du rechts siehst, und bringe sie zum Regnen! Retten Sie die Fische! Rette den See!"

    # Calculate text size and position for wrapping
    text_font_scale = 2.2
    text_font_color = (255, 255, 255)
    max_text_width = frame.shape[1] - 200  # Maximum width for wrapping
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, text_font_scale, 1)[0]
    text_lines = []
    words = text.split()
    line = words[0]
    for word in words[1:]:
        test_line = f"{line} {word}"
        width, _ = cv2.getTextSize(test_line, cv2.FONT_HERSHEY_SIMPLEX, text_font_scale, 1)[0]
        if width <= max_text_width:
            line = test_line
        else:
            text_lines.append(line)
            line = word
    text_lines.append(line)

    # Draw each line of text
    text_y = 200
    for line in text_lines:
        cv2.putText(overlay, line, (150, text_y), cv2.FONT_HERSHEY_SIMPLEX,
                    text_font_scale, text_font_color, 1, cv2.LINE_AA | cv2.WARP_FILL_OUTLIERS)
        text_y += int(text_size[1] * 1.5)  # Increase the Y coordinate for the next line

    alpha = 0.5  # Adjust the transparency as needed
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)