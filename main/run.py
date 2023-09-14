
import cv2
import os
import image_dehazer

# Create a folder to store captured frames
frame_folder = 'captured_frames/'
os.makedirs(frame_folder, exist_ok=True)

# Create a folder to store dehazed images
output_folder = 'dehazed_images/'
os.makedirs(output_folder, exist_ok=True)

# Output video file name
output_video_file = 'dehazed_video.mp4'

webCam = cv2.VideoCapture(0)
frame_rate = 30  # Frames per second

# Capture 5 frames and dehaze them
for current_frame in range(10):
    success, frame = webCam.read()
    
    if not success:
        break

    frame_filename = os.path.join(frame_folder, f'frame_{current_frame}.jpg')
    cv2.imwrite(frame_filename, frame)
    
    cv2.imshow("Capturing Frames", frame)

    # Dehaze the captured frame
    HazeCorrectedImg, haze_map = image_dehazer.remove_haze(frame, showHazeTransmissionMap=False)
    
    output_path = os.path.join(output_folder, f'dehazed_{current_frame}.jpg')
    cv2.imwrite(output_path, HazeCorrectedImg)
    
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

webCam.release()
cv2.destroyAllWindows()

# Convert dehazed images to a video
dehazed_image_files = sorted([os.path.join(output_folder, img) for img in os.listdir(output_folder)])

# Load the first image to get dimensions
sample_image = cv2.imread(dehazed_image_files[0])
height, width, layers = sample_image.shape

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change the codec as needed
out = cv2.VideoWriter(output_video_file, fourcc, 30.0, (width, height))

# Loop through dehazed images and add them to the video
for image_file in dehazed_image_files:
    frame = cv2.imread(image_file)
    out.write(frame)

# Release the VideoWriter and close all OpenCV windows
out.release()
cv2.destroyAllWindows()

print(f'Dehazed video saved as {output_video_file}')
