import cv2


def main():

    print("Press 1 for pre-recorded videos, 2 for live stream: ")
    option = int(input())

    if option == 1:
        # Record video
        windowName = "Sample Feed from Camera 1"
        cv2.namedWindow(windowName)

        windowName2 = "Sample Feed from Camera 2"
        cv2.namedWindow(windowName2)

        windowName3 = "Sample Feed from Camera 3"
        cv2.namedWindow(windowName3)

        capture1 = cv2.VideoCapture("http://10.130.149.38:4747/video")  # laptop's camera
        capture2 = cv2.VideoCapture("http://10.130.138.187:4747/video")   # sample code for mobile camera video capture using IP camera
        capture3 = cv2.VideoCapture("http://10.130.15.141:4747/video")


        # define size for recorded video frames:
        width1 = int(capture1.get(3))
        height1 = int(capture1.get(4))
        size1 = (width1, height1)

        width2 = int(capture2.get(3))
        height2 = int(capture2.get(4))
        size2 = (width2, height2)

        width3 = int(capture3.get(3))
        height3 = int(capture3.get(4))
        size3 = (width3, height3)

        # frame of size is being created and stored in .avi file
        outputFile1 = cv2.VideoWriter(
            'Stream1Recording.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 10, size1)

        outputFile2 = cv2.VideoWriter(
            'Stream2Recording.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 10, size2)

        outputFile3 = cv2.VideoWriter(
            'Stream3Recording.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 10, size3)

        # check if feed exists or not for camera 1
        #if capture1.isOpened():
        #    ret1, frame1 = capture1.read()
        #else:
        #   ret1 = False

        while True:
            #ret1, frame1 = capture1.read()
            # sample feed display from camera 1
            #cv2.imshow(windowName, frame1)

            # saves the frame from camera 1
            #optputFile1.write(frame1)
            ret1, frame1 = capture1.read()
            ret2, frame2 = capture2.read()
            ret3, frame3 = capture3.read()

            cv2.imshow(windowName, frame1)
            cv2.imshow(windowName2, frame2)
            cv2.imshow(windowName3, frame3)

            outputFile1.write(frame1)
            outputFile2.write(frame2)
            outputFile3.write(frame3)


            # escape key (27) to exit
            if cv2.waitKey(1) == 27:
                break

        capture1.release()
        outputFile1.release()

        capture2.release()
        outputFile2.release()

        capture3.release()
        outputFile3.release()
        cv2.destroyAllWindows()

    elif option == 2:
        # live stream
        windowName1 = "Live Stream Camera 1"
        cv2.namedWindow(windowName1)

        windowName2 = "Live Stream Camera 2"
        cv2.namedWindow(windowName2)

        windowName3 = "Live Stream Camera 3"
        cv2.namedWindow(windowName3)

        capture1 = cv2.VideoCapture("http://10.130.145.102:4747/video")  # laptop's camera
        capture2 = cv2.VideoCapture("http://10.130.15.141:4747/video")
        capture3 = cv2.VideoCapture("http://10.130.138.187:4747/video")

        #if capture1.isOpened():  # check if feed exists or not for camera 1
        #    ret1, frame1 = capture1.read()
        #else:
        #    ret1 = False

        while True:
            ret1, frame1 = capture1.read()
            cv2.imshow(windowName1, frame1)

            ret2, frame2 = capture2.read()
            cv2.imshow(windowName2, frame2)

            ret3, frame3 = capture3.read()
            cv2.imshow(windowName3, frame3)

            if cv2.waitKey(1) == 27:
                break

        capture1.release()
        capture2.release()
        capture3.release()
        cv2.destroyAllWindows()

    else:
        print("Invalid option entered. Exiting...")


main()
