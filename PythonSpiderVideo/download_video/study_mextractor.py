# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：study_mextractor.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/12/18 15:45 
"""
from mextractor.workflow import extract_and_dump_video

dump_dir = "dump_dir"
path_to_video = "path_o_video/m3u8file.mp4"
# metadata = extract_and_dump_video(dump_dir, path_to_video, include_image, greyscale, lossy_compress_image)
metadata = extract_and_dump_video(dump_dir, path_to_video)


