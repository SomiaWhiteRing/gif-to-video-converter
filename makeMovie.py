from moviepy.editor import *
import glob
from tqdm import tqdm
import os

def resize_clip_with_padding(clip, target_width=1920, target_height=1080, margin_percent=0.1):
    # 计算留白区域的像素值
    margin_pixels = int(target_height * margin_percent)
    available_height = target_height - (2 * margin_pixels)
    
    # 确保GIF循环播放
    clip = clip.loop()
    
    # 处理透明背景
    if clip.mask is None and hasattr(clip, 'mask'):
        clip = clip.set_mask(clip.mask)
    
    # 计算缩放比例，保持原始比例
    w, h = clip.size
    scale = min(target_width/w, available_height/h)
    new_size = (int(w*scale), int(h*scale))
    
    # 缩放视频，保持透明度
    resized_clip = clip.resize(new_size)
    
    # 创建黑色背景
    bg = ColorClip(size=(target_width, target_height), color=(0,0,0))
    
    # 计算居中位置
    x_center = (target_width - new_size[0]) // 2
    y_center = (target_height - new_size[1]) // 2
    
    # 将缩放后的视频放在黑色背景上
    final_clip = CompositeVideoClip([
        bg,
        resized_clip.set_position((x_center, y_center))
    ])
    
    return final_clip

def create_video():
    # 设置GIF文件夹路径
    gif_folder = os.path.join(os.getcwd(), 'gif')
    
    # 检查gif文件夹是否存在
    if not os.path.exists(gif_folder):
        print("错误：找不到gif文件夹！")
        return
    
    # 获取所有GIF文件并按数字顺序排序
    gif_files = sorted(
        glob.glob(os.path.join(gif_folder, '*.gif')), 
        key=lambda x: int(os.path.basename(x).split('.')[0])
    )
    
    if not gif_files:
        print("错误：gif文件夹中没有找到GIF文件！")
        return
        
    print(f"在gif文件夹中找到 {len(gif_files)} 个GIF文件")
    
    # 创建视频片段列表
    clips = []
    for gif_file in tqdm(gif_files, desc="处理GIF文件"):
        try:
            clip = VideoFileClip(gif_file, has_mask=True)
            clip = resize_clip_with_padding(clip)
            clip = clip.set_duration(100/23)
            clips.append(clip)
        except Exception as e:
            print(f"处理 {os.path.basename(gif_file)} 时出错: {str(e)}")
    
    if not clips:
        print("错误：没有成功处理任何GIF文件！")
        return
        
    print("正在合成最终视频...")
    final_clip = concatenate_videoclips(clips)
    
    print("正在添加背景音乐...")
    # 检查音乐文件是否存在
    music_path = 'music.mp3'
    if not os.path.exists(music_path):
        print("错误：找不到music.mp3文件！")
        return
        
    audio = AudioFileClip(music_path)
    audio = audio.set_duration(final_clip.duration)
    final_clip = final_clip.set_audio(audio)
    
    print("正在导出视频...")
    final_clip.write_videofile('output.mp4', 
                             fps=24, 
                             codec='libx264',
                             audio_codec='aac')
    
    print("清理资源...")
    final_clip.close()
    audio.close()
    for clip in clips:
        clip.close()
    
    print("处理完成！")

if __name__ == '__main__':
    create_video()
