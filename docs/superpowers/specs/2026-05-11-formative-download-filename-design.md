# 形考答案文件命名冲突修复设计

## 问题

同一课程内多个形考任务名称相同时，后下载的 PDF 会覆盖前面的。

## 解决方案

使用 exam id 作为文件名的区分后缀。

### 修改内容

**文件**: `src/download_formative/download.py` 第 16 行

**原代码**:
```python
file_path = f"{save_dir}/{exam_info.get('title')}.pdf"
```

**新代码**:
```python
file_path = f"{save_dir}/{exam_info.get('title')}_{exam_info.get('id')}.pdf"
```

### 效果示例

| 原文件名 | 新文件名 |
|---------|---------|
| 形考一.pdf | 形考一_123456.pdf |
| 形考一.pdf | 形考一_789012.pdf |

### 优点

- 完全避免冲突
- 无需额外 API 请求
- 保持可读性

## 改动范围

仅修改 `download.py` 一行代码。