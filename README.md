# GIF to Video Converter

一个将多个GIF图片合成为视频并添加背景音乐的Python脚本。

## ✨ 功能特点

- 将多个GIF文件按序合成为1080p (1920x1080) 视频
- 自动调整GIF尺寸，保持原始比例
- 上下留出10%边距，自动居中显示
- 支持GIF透明背景
- 每个GIF循环播放5秒
- 可添加背景音乐
- 带进度显示功能

## 🔧 依赖要求

- Python 3.6+
- moviepy
- tqdm

## 📦 安装

1. 克隆仓库：
```bash
git clone https://github.com/SomiaWhiteRing/gif-to-video-converter.git
cd gif-to-video-converter
```

2. 安装依赖：
```bash
pip install moviepy tqdm
```

## 📝 使用方法

1. 创建所需的文件结构：

```
项目目录/
├── makeMovie.py
├── music.mp3 # 背景音乐文件
└── gif/ # GIF文件夹
├── 1.gif
├── 2.gif
├── 3.gif
└── ...
```

2. 将需要处理的GIF文件放入`gif`文件夹，并按照`1.gif`、`2.gif`等格式命名
3. 将背景音乐文件命名为`music.mp3`并放在项目根目录
4. 运行脚本：
```bash
python makeMovie.py
```

## 🎥 输出

- 输出文件：`output.mp4`
- 分辨率：1920x1080 (16:9)
- 帧率：24fps
- 编码：H.264
- 音频编码：AAC

## ⚠️ 注意事项

- GIF文件需要按数字顺序命名（1.gif, 2.gif, ...）
- 建议使用带透明背景的GIF以获得最佳效果
- 确保有足够的磁盘空间存储输出视频
- 处理大量或高分辨率GIF文件可能需要较长时间

## 📄 许可证

[MIT License](LICENSE)

## 🤝 贡献

欢迎提交问题和改进建议！

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📧 联系方式

项目作者：[苍旻白轮]
- GitHub: [@SomiaWhiteRing](https://github.com/SomiaWhiteRing)
- Email: anonsoyo@soyorin.love
```
