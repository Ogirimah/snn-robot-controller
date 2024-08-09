import cv2
import numpy as np

def to_event_based(frame1, frame2, threshold):
  """Converts two consecutive frames to event-based data.

  Args:
    frame1: The previous frame.
    frame2: The current frame.
    threshold: The intensity change threshold to consider as an event.

  Returns:
    A list of events, where each event is a tuple (x, y, polarity, timestamp).
  """

  diff = cv2.absdiff(frame1, frame2)
  _, diff_binary = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

  events = []
  for y in range(diff_binary.shape[0]):
    for x in range(diff_binary.shape[1]):
      if diff_binary[y, x] > 0:
        # You can use time.time() or some other timestamping method
        timestamp = cv2.getTickCount()  # Example using cv2.getTickCount()
        events.append((x, y, 1, timestamp))  # Positive event
      elif diff_binary[y, x] < 0:
        timestamp = cv2.getTickCount()
        events.append((x, y, -1, timestamp))  # Negative event

  return events

# -----------------------------------------------------------------------
# Using video

# def process_video(video_path, threshold):
#   """Processes a video stream and generates event-based data.

#   Args:
#     video_path: Path to the video file.
#     threshold: The intensity change threshold for event generation.
#   """

#   cap = cv2.VideoCapture(video_path)

#   prev_frame = None
#   while True:
#     ret, frame = cap.read()
#     if not ret:
#       break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     if prev_frame is not None:
#       events = to_event_based(prev_frame, gray, threshold)
#       # Process events here (e.g., store, visualize, analyze)

#     prev_frame = gray

#   cap.release()

# if __name__ == "__main__":
#   video_path = "your_video_path.mp4"
#   threshold = 30  # Adjust threshold as needed
#   process_video(video_path, threshold)



# ___________________________________________________________

# Using stream of images

import glob


def process_images(image_dir, threshold):
  """Processes a stream of images and generates event-based data.

  Args:
    image_dir: Path to the directory containing images.
    threshold: The intensity change threshold for event generation.
  """

  image_list = glob.glob(image_dir + '/*.jpg')  # Adjust extension as needed
  image_list.sort()  # Ensure images are processed in order

  prev_frame = None
  for image_path in image_list:
    frame = cv2.imread(image_path)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if prev_frame is not None:
      events = to_event_based(prev_frame, gray, threshold)
      # Process events here (e.g., store, visualize, analyze)

    prev_frame = gray

if __name__ == "__main__":
  image_dir = "path/to/your/images"
  threshold = 30  # Adjust threshold as needed
  process_images(image_dir, threshold)
