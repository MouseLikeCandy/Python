# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：image_detect_objects.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/11/27 9:34 
"""

import cv2
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

# # 加载模型
# model = tf.saved_model.load('ssd_mobilenet_v2_coco/saved_model')

# 加载模型
model_url = "https://tfhub.dev/tensorflow/ssd_mobilenet_v2/coco/2"
model = hub.load(model_url)

# 保存模型
tf.saved_model.save(model, 'ssd_mobilenet_v2_coco_saved_model')


# 加载标签
with open('coco_labels.txt', 'r') as file:
    labels = file.read().splitlines()

# 读取图像
image_path = 'hw_1695799382369.jpg'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 预处理图像
input_tensor = tf.convert_to_tensor(image_rgb)
input_tensor = tf.expand_dims(input_tensor, 0)

# 模型推断
detections = model(input_tensor)

# 处理检测结果
boxes = detections['detection_boxes'][0].numpy()
scores = detections['detection_scores'][0].numpy()
classes = detections['detection_classes'][0].numpy().astype(int)

# 设置置信度阈值
confidence_threshold = 0.5
selected_boxes = boxes[scores > confidence_threshold]
selected_classes = classes[scores > confidence_threshold]

# 显示检测结果
for box, class_id in zip(selected_boxes, selected_classes):
    ymin, xmin, ymax, xmax = box
    xmin, ymin, xmax, ymax = map(int, [xmin * image.shape[1], ymin * image.shape[0], xmax * image.shape[1],
                                       ymax * image.shape[0]])

    class_label = labels[class_id]
    cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
    cv2.putText(image, f'{class_label}', (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# 保存带有检测结果的图像
cv2.imwrite('hw_1.jpg', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
