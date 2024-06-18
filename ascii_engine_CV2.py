import cv2
import os
import argparse

# Function to convert pixel intensity to ASCII character
def pixel_to_ascii(pixel):
    ascii_chars = '@%#*+=-:. '  # ASCII characters from dark to light
    return ascii_chars[int(pixel / 255 * (len(ascii_chars) - 1))]

# Function to clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to convert image frame to ASCII art
def image_to_ascii(image_path, width=100, height=50):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.resize(gray_image, (width, height))
    
    ascii_art = ''
    for row in gray_image:
        for pixel in row:
            ascii_art += pixel_to_ascii(pixel)
        ascii_art += '\n'
    
    return ascii_art

# Function to convert video frames to ASCII art
def video_to_ascii(video_path, width=100, height=50):
    cap = cv2.VideoCapture(video_path)
    ascii_frames = []
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.resize(gray_frame, (width, height))
        
        ascii_art = ''
        for row in gray_frame:
            for pixel in row:
                ascii_art += pixel_to_ascii(pixel)
            ascii_art += '\n'
        
        ascii_frames.append(ascii_art)
    
    cap.release()
    return ascii_frames

# Main function
def main():
    parser = argparse.ArgumentParser(description='Convert image or video to ASCII art.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Path to input image or video')
    parser.add_argument('-t', '--type', choices=['image', 'video'], required=True, help='Type of input: image or video')
    parser.add_argument('-w', '--width', type=int, default=100, help='Width of ASCII art (default: 100)')
    parser.add_argument('-H', '--height', type=int, default=50, help='Height of ASCII art (default: 50)')
    args = parser.parse_args()

    if args.type == 'image':
        ascii_art = image_to_ascii(args.input, args.width, args.height)
        print(ascii_art)
    elif args.type == 'video':
        ascii_frames = video_to_ascii(args.input, args.width, args.height)
        for frame in ascii_frames:
            clear_screen()  # Clear screen before printing each frame
            print(frame)
            input("Press Enter to continue...")  # Pause between frames (optional)

if __name__ == '__main__':
    main()
