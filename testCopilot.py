#冒泡排序方法
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
#基于冒泡排序的二分查找
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = int(l + (r - l)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1

#快速排序方法
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

#partition方法
def partition(arr, low, high):
    i = ( low-1 )         
    pivot = arr[high]     
    for j in range(low , high):
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )


#基于opencv实现人脸识别方法

def face_recognition():
    #人脸识别
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    #读取图片
    img = cv2.imread('test.jpg')
    #灰度化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #检测人脸
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #在人脸上画矩形框
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        #检测眼睛
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    #显示图片
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#怎么安装opencv
#pip install opencv-python


    
