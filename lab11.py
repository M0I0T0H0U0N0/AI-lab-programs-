import cv2
def process_image(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    cv2.imshow("grayscale image",gray)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

def process_video(video_path):
    cap=cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret , frame=cap.read()
        if not ret :
            break
        cv2.imshow("video",frame)
        
        if cv2.waitKey(25) & 0xFF==ord('q') :
            break
    cap.release()
    cv2.destroyAllWindows()

choice=input("enter 'i' for image or 'V' for video:")
if choice.lower()=='i':

    image = cv2.imread(r'C:\Users\Student\Desktop\basketball.jfif')

    process_image(image)
elif choice.lower()=='v':
    video_path=r"C:\Users\Student\Videos\Captures\basketball - Bing images and 5 more pages - [InPrivate] - Microsoft​ Edge 2023-10-31 04-26-34.mp4"
    process_video(video_path)
else:
    print("invalid choice please enter 'i' or 'v' ")