# import cv2
# import os
# import numpy as np
# from tensorflow.keras.models import load_model

# def capture_palm_print_frames(output_folder='captured_frames', x1=200, y1=150, x2=400, y2=350):
#     os.makedirs(output_folder, exist_ok=True)

#     # Define a video capture object
#     vid = cv2.VideoCapture(0)

#     frame_count = 0

    #while True:
        # Capture the video frame
        #ret, frame = vid.read()

        # Draw the border rectangle for palm print area on the frame
        # frame_with_border = frame.copy()
        # cv2.rectangle(frame_with_border, (x1, y1), (x2, y2), (0, 300, 0), 2)

        # Display the frame with the border
        # cv2.imshow('frame', frame_with_border)

        # Check if the 'c' key is pressed to capture and save the frame within the palm print area
        # key = cv2.waitKey(1) & 0xFF
        # if key == ord('c'):
        #     palm_print = frame[y1:y2, x1:x2]  # Extract the palm print area
        #     frame_count += 1
        #     output_file = os.path.join(output_folder, f"palm_{frame_count:04d}.jpg")
        #     cv2.imwrite(output_file, palm_print)
        #     print(f"Palm print {frame_count} captured and saved.")

        # The 'q' button is set as the quitting button.
        # You may use any desired button of your choice.
        # elif key == ord('q'):
        #     break

    # After the loop release the cap object
    # vid.release()

    # Destroy all the windows
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     capture_palm_print_frames()
import cv2
import os
import numpy as np
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model("palm_print_model.h5")
current_directory = os.path.dirname(os.path.abspath(__file__))

def capture_palm_print_frames(output_folder='captured_frames', x1=200, y1=150, x2=400, y2=350):
    os.makedirs(output_folder, exist_ok=True)

    # Define a video capture object
    vid = cv2.VideoCapture(0)

    frame_count = 0

    while True:
        # Capture the video frame
        ret, frame = vid.read()

        # Draw the border rectangle for palm print area on the frame
        frame_with_border = frame.copy()
        cv2.rectangle(frame_with_border, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Display the frame with the border
        cv2.imshow('frame', frame_with_border)

        # Check if the 'c' key is pressed to capture and save the frame within the palm print area
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            palm_print = frame[y1:y2, x1:x2]  # Extract the palm print area
            frame_count += 1
            output_file = os.path.join(output_folder, f"palm_{frame_count:04d}.jpg")
            cv2.imwrite(output_file, palm_print)
            print(f"Palm print {frame_count} captured and saved.")

            # Perform testing on the captured palm print
            image_width = 1000
            image_height = 750

            resized_image = cv2.resize(palm_print, (image_width, image_height))
            normalized_image = resized_image / 255.0
            input_image = np.expand_dims(normalized_image, axis=0)
            prediction = model.predict(input_image)
            predicted_class = np.argmax(prediction, axis=-1)[0]
            class_names = ["niv", "tp"]
            class_name = class_names[predicted_class]
            print(f"Prediction for palm {frame_count}: {class_name}")

            # Display prediction result in a pop-up screen
            result_frame = frame.copy()
            cv2.putText(result_frame, f"Prediction: {class_name}", (x1, y2 + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.imshow('Result', result_frame)
            cv2.waitKey(3000)  # Display the result for 3 seconds

            # Close the pop-up screen
            cv2.destroyWindow('Result')

        # The 'q' button is set as the quitting button.
        # You may use any desired button of your choice.
        elif key == ord('q'):
            break

    # After the loop release the cap object
    vid.release()

    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_palm_print_frames()
    