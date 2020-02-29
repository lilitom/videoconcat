from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips


def video_loop(path, time_list):
    """
    对指定的地方进行循环
    :param path: 路径
    :param time_list: 时间列表
    :return: 修改后的视频
    """
    inital_clip = VideoFileClip(path)
    time_list_part = time_list
    for i in time_list:
        time_list_part.append(i+1)
    time_list_part.insert(0, 0)
    time_list_part.append(inital_clip.duration)
    clip_list_part =[]
    for i in range(0,len(time_list_part)-2):
        clip_list_part.append(inital_clip.subclip(time_list[i], time_list[i+1]))



    




if __name__ == '__main__':
    video_loop(path="D:\\Bilibilup\\youtube\\s2_051.mp4", time_list=[10, 20])
