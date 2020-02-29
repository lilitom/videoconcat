from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips, ImageSequenceClip
import cv2
import os
from PIL import Image, ImageDraw, ImageFont

chinfont1 = ImageFont.truetype("ShangShouRunHeiTi-2.ttf", size=50)
chinfont2 = ImageFont.truetype("ShangShouRunHeiTi-2.ttf", size=45)


def save_img(videopath="E:\\Alex\\xincangku\\video1\\video"):
    video_path = videopath
    videos = os.listdir(video_path)
    a = 0
    all_path = []
    pic_path = os.path.join("E:\\Alex\\xincangku\\video1", "pic" + str(a))
    all_path.append(pic_path)
    if not os.path.exists(pic_path):
        os.mkdir(pic_path)
    for video_name in videos:
        file_name = os.path.join(video_path, video_name)
        vc = cv2.VideoCapture(file_name)  # 读入视频文件
        c = 0
        rval = vc.isOpened()
        while rval:  # 循环读取视频帧
            c = c + 1
            rval, frame = vc.read()
            if rval:
                cv2.imwrite(os.path.join(pic_path, "{}.jpg".format(c)), frame)  # 存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
                cv2.waitKey(1)
            else:
                break
        vc.release()
        print('save_success')
    return all_path


def pic_cut(pic_path):
    pic_all_path = os.listdir(pic_path)
    for i in pic_all_path:
        img = Image.open(os.path.join(pic_path, i))
        drawObject = ImageDraw.Draw(img)
        drawObject.rectangle((0, 0, 574, 86), fill="white")
        drawObject.rectangle((0, 938, 574, 1024), fill="white")
        drawObject.text((197, 28), fill="red", text="面面", font=chinfont1, align="center")
        drawObject.text((287, 29), fill="green", text="相觑", font=chinfont2, align="center")
        drawObject.text((100, 956), fill="blue", text="关注我", font=chinfont1, align="center")
        drawObject.text((250, 956), fill="green", text="学做面食吧", font=chinfont2, align="center")
        # drawObject.ellipse((50, 50, 80, 80), fill="red")  # 在image上画一个红色的圆
        # img2 = img.crop((0, 86, 574, 853))
        img.save(os.path.join(pic_path, i))
    return [os.path.join(pic_path, str(i) + ".jpg") for i in range(1, len(pic_all_path) + 1)]


if __name__ == '__main__':
    all_path = save_img()
    j = 0
    for i in all_path:
        images_list = pic_cut(i)
        clip = ImageSequenceClip(images_list, fps=25)
        clip.write_videofile("E:\\Alex\\xincangku\\video1\\after\\pic{}.mp4".format(j))
        j = j + 1


    # target = Image.new('RGB', (574, 1024))
    # image_draw = ImageDraw.Draw(target)
    # image_draw.text((267, 28), fill="red", text="加油", font=chinfont, align="center")
    # target.save("hao.jpg")