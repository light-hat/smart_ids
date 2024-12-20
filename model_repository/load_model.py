"""
Скрипт для скачивания ML-модели с HuggingFace
и сохранения в ONNX-формат.
"""

import torch
import os
import shutil
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = "rdpahalavan/bert-network-packet-flow-header-payload"
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Задаем путь к папке для сохранения модели
MODEL_DIR= "bert_network_packet"
version_dir = os.path.join(MODEL_DIR, "1")

# Проверяем, существует ли папка, если да — удаляем её содержимое
if os.path.exists(version_dir):
    shutil.rmtree(version_dir)

# Создаем новую папку для модели
os.makedirs(version_dir, exist_ok=True)

# Пример текста и подготовка данных
TEXT = "Sample packet text"
inputs = tokenizer(TEXT, return_tensors="pt")

# Сохраняем модель в ONNX формате в папку `1`
onnx_model_path = os.path.join(version_dir, "model.onnx")
torch.onnx.export(
    model,
    (inputs['input_ids'], inputs['attention_mask']),
    onnx_model_path,
    input_names=["input_ids", "attention_mask"],
    output_names=["output"],
    dynamic_axes={"input_ids": {0: "batch_size"}, "attention_mask": {0: "batch_size"}},
    opset_version=14,
)

print(f"Model saved at {onnx_model_path}")
