'''
#just for dehazing
import cv2
import image_dehazer

if __name__ == "__main__":

    HazeImg = cv2.imread('Images/foggy_oaks.jpg')						# read input image -- (**must be a color image**)
    HazeCorrectedImg, haze_map = image_dehazer.remove_haze(HazeImg, showHazeTransmissionMap=False)		# Remove Haze

    cv2.imshow('haze_map', haze_map);						# display the original hazy image
    cv2.imshow('enhanced_image', HazeCorrectedImg);			# display the result
    cv2.waitKey(0)
    cv2.imwrite("outputImages/result.png", HazeCorrectedImg)'''






'''import cv2 #dehazing and cam
import image_dehazer

if __name__ == "__main__":
    folder_path = 'Images/'  # Specify the folder path where your image is located
    image_filename = 'foggy_bench.jpg'  # Specify the image file name

    HazeImg = cv2.imread(folder_path + image_filename)  # Read the image from the specified folder
    HazeCorrectedImg, haze_map = image_dehazer.remove_haze(HazeImg, showHazeTransmissionMap=False)

    cv2.imshow('haze_map', haze_map)
    cv2.imshow('enhanced_image', HazeCorrectedImg)
    cv2.waitKey(0)

    output_folder = 'outputImages/'  # Specify the folder where you want to save the result
    output_path = output_folder + 'result.png'
    cv2.imwrite(output_path, HazeCorrectedImg)'''







'''import cv2
import image_dehazer
webCam = cv2.VideoCapture(0)
currentframe = 0

while (True):
    
    success, frame = webCam.read()
    
    cv2.imshow("output", frame)
    
    cv2.imwrite('img_captured' + str(currentframe)+ '.jpg', frame)
    currentframe +=10000
    
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

if __name__ == "__main__":
    folder_path = 'Images/'  # Specify the folder path where your image is located
    image_filename = 'foggy_bench.jpg'  # Specify the image file name

    HazeImg = cv2.imread(folder_path + image_filename)  # Read the image from the specified folder
    HazeCorrectedImg, haze_map = image_dehazer.remove_haze(HazeImg, showHazeTransmissionMap=False)

    cv2.imshow('haze_map', haze_map)
    cv2.imshow('enhanced_image', HazeCorrectedImg)
    cv2.waitKey(0)

    output_folder = 'outputImages/'  # Specify the folder where you want to save the result
    output_path = output_folder + 'result.png'
    cv2.imwrite(output_path, HazeCorrectedImg)'''



'''
#time can be managed for each frames 
import cv2
import os
import image_dehazer

# Create a folder to store captured frames
frame_folder = 'captured_frames/'
os.makedirs(frame_folder, exist_ok=True)

# Create a folder to store dehazed images
output_folder = 'dehazed_images/'
os.makedirs(output_folder, exist_ok=True)

webCam = cv2.VideoCapture(0)
frame_rate = 30  # Frames per second
duration = 60  # Duration in seconds (1 minute)

# Calculate the total number of frames to capture
total_frames = frame_rate * duration

current_frame = 0

while current_frame < total_frames:
    success, frame = webCam.read()
    
    if not success:
        break

    # Save every 5 frames
    if current_frame % 5 == 0:
        frame_filename = os.path.join(frame_folder, f'frame_{current_frame}.jpg')
        cv2.imwrite(frame_filename, frame)

    cv2.imshow("Capturing Frames", frame)

    # Break the loop after capturing the required number of frames
    if current_frame >= total_frames:
        break

    current_frame += 1
    
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

webCam.release()
cv2.destroyAllWindows()

# Dehazing the captured frames
frame_files = os.listdir(frame_folder)

for frame_file in frame_files:
    frame_path = os.path.join(frame_folder, frame_file)
    frame = cv2.imread(frame_path)
    
    HazeCorrectedImg, haze_map = image_dehazer.remove_haze(frame, showHazeTransmissionMap=False)
    
    output_path = os.path.join(output_folder, f'dehazed_{frame_file}')
    cv2.imwrite(output_path, HazeCorrectedImg)

print(f'Dehazing completed. {len(frame_files)} frames dehazed.')'''



'''#overall code upto saving as frames
import cv2
import os
import image_dehazer

# Create a folder to store captured frames
frame_folder = 'captured_frames/'
os.makedirs(frame_folder, exist_ok=True)

# Create a folder to store dehazed images
output_folder = 'dehazed_images/'
os.makedirs(output_folder, exist_ok=True)

webCam = cv2.VideoCapture(0)
frame_rate = 30  # Frames per second

# Capture 5 frames
for current_frame in range(5):
    success, frame = webCam.read()
    
    if not success:
        break

    frame_filename = os.path.join(frame_folder, f'frame_{current_frame}.jpg')
    cv2.imwrite(frame_filename, frame)
    
    cv2.imshow("Capturing Frames", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

webCam.release()
cv2.destroyAllWindows()

# Dehazing the captured frames
frame_files = os.listdir(frame_folder)

for frame_file in frame_files:
    frame_path = os.path.join(frame_folder, frame_file)
    frame = cv2.imread(frame_path)
    
    HazeCorrectedImg, haze_map = image_dehazer.remove_haze(frame, showHazeTransmissionMap=False)
    
    output_path = os.path.join(output_folder, f'dehazed_{frame_file}')
    cv2.imwrite(output_path, HazeCorrectedImg)

print(f'Dehazing completed for {len(frame_files)} frames.')'''



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

# Capture frames for a specific duration (e.g., 10 seconds)
duration_seconds = 100
total_frames = frame_rate * duration_seconds

for current_frame in range(total_frames):
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



