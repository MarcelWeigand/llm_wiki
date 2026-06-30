# Computer Vision

**Summary**: Structured overview of computer vision sub-tasks from an AI Solution Architect perspective, with capability, learning paradigm, and model architecture mapped to the [[1 - Overview]] dimensions for each.

**Last updated**: 2026-06-23

---

## Dimensions Overview

**Application domain**: Computer vision (given — all tasks in this file operate on images, video, or 2D/3D scans)

The other 3 dimensions vary by sub-task but follow clear patterns across the field:

**Capability**: Dominated by **Predictive AI**, split between classification (what is it?) and regression (where is it? how many? how far?). Image generation is the one exception — that is Generative AI. Decision making AI appears only when CV is the perception input to a robotics or control system.

**Learning paradigm**: **Supervised** is the default for almost all CV tasks — labeled images, bounding boxes, or pixel masks are required. Two exceptions:
- **Unsupervised** for visual anomaly detection — trained on normal images only, no defect labels needed
- **Self-supervised** for image generation (diffusion models, GANs) and increasingly for pre-training large vision models (MAE, DINO, CLIP) before fine-tuning on small labeled datasets

**Model architecture**: **CNN** is the foundation of nearly every CV architecture. The field is progressively moving toward **Transformers** (Vision Transformer — ViT) for tasks where global context matters, and **CNN + Transformer hybrids** for tasks that need both local feature extraction and long-range attention. Pure CNNs still dominate on edge devices where compute is constrained.

| Dimension | Dominant value | Exception |
|---|---|---|
| Capability | Predictive AI — classification + regression | Image generation → Generative AI |
| Learning paradigm | Supervised | Anomaly detection → Unsupervised; Generation & pre-training → Self-supervised |
| Model architecture | CNN | High-accuracy tasks → Transformer (ViT); Complex tasks → CNN + Transformer hybrid |

---

## Quick Reference

| Sub-task | Output | Capability | Learning paradigm | Architecture |
|---|---|---|---|---|
| Image classification | Class label per image | Predictive — classification | Supervised / Self-supervised | CNN, ViT |
| Object detection | Bounding boxes + class labels | Predictive — classification + regression | Supervised | CNN (YOLO, Faster R-CNN) |
| Object counting | Integer count per class | Predictive — regression | Supervised / Unsupervised | CNN (detection-based or density map) |
| Semantic segmentation | Class label per pixel | Predictive — classification | Supervised | CNN (UNet, DeepLab) |
| Instance segmentation | Per-object pixel mask | Predictive — classification + regression | Supervised | CNN (Mask R-CNN) |
| Pose estimation | Keypoint coordinates per joint | Predictive — regression | Supervised | CNN (HRNet, OpenPose) |
| OCR | Text extracted from image | Predictive — classification (sequence) | Supervised / Self-supervised | CNN + Transformer (TrOCR) |
| Visual anomaly detection | Anomaly / normal flag | Predictive — binary classification | Unsupervised | CNN Autoencoder, PatchCore |
| Action recognition | Activity label from video | Predictive — classification | Supervised | 3D CNN, Video Transformer |
| Image generation | New synthetic images | Generative AI | Self-supervised | Diffusion model, GAN |
| Depth estimation | Per-pixel distance from camera | Predictive — regression | Supervised / Self-supervised | CNN + Transformer (MiDaS) |
| Change detection | Changed / unchanged per region | Predictive — binary classification | Supervised / Unsupervised | Siamese CNN |

---

## 1. Image Classification

**What it does**: Assigns a single label to an entire image. The simplest CV task.

**Output**: One class label per image (binary: defect / ok; multi-class: cat / dog / bird)

**Typical use cases**: Product quality pass/fail, document type classification, medical image triage

| Dimension | Value |
|---|---|
| Capability | Predictive AI — binary or multi-class classification |
| Learning paradigm | Supervised (labeled images) — or Self-supervised when fine-tuning a pre-trained model (ImageNet-pretrained CNN / ViT) on a small labeled dataset |
| Model architecture | Neural networks — CNN (ResNet, EfficientNet for edge deployment) or Vision Transformer (ViT for large datasets with high accuracy requirements) |

**Primary metric**: Accuracy (balanced) / F1 macro (imbalanced classes) / ROC-AUC (binary)

---

## 2. Object Detection

**What it does**: Locates and classifies multiple objects within a single image. Output is a set of bounding boxes, each with a class label and confidence score.

**Output**: List of (class, confidence, x, y, width, height) per detected object

**Typical use cases**: Defect localization on production lines, person detection in safety zones, vehicle counting in logistics

| Dimension | Value |
|---|---|
| Capability | Predictive AI — multi-class classification (what is it?) + regression (where is it? — bounding box coordinates) |
| Learning paradigm | Supervised — requires images labeled with bounding boxes per object (expensive to annotate) |
| Model architecture | Neural networks — CNN: **YOLO** (v8/v11, real-time, edge-friendly), **Faster R-CNN** (more accurate, slower), **SSD** (balanced) |

**Primary metric**: **mAP** (mean Average Precision) at IoU threshold — mAP@0.5 is standard; mAP@0.5:0.95 is stricter

**SA note**: YOLO is the default choice for manufacturing edge deployments (<10ms latency). Faster R-CNN when accuracy matters more than speed.

---

## 3. Object Counting

**What it does**: Counts the number of instances of a class in an image, even when objects are densely packed and individual detection fails.

**Output**: Integer count per class

**Typical use cases**: Counting cells under a microscope, people in a crowd, parts on a conveyor belt, trees in satellite imagery

| Dimension | Value |
|---|---|
| Capability | Predictive AI — regression (count as a continuous/integer value, single output per class) |
| Learning paradigm | Supervised (labeled counts or point annotations) for density map approach; detection-based counting reuses object detection labels |
| Model architecture | Neural networks — detection-based (YOLO, count bounding boxes) for sparse scenes; **density map CNN** (CSRNet) for dense, overlapping objects where individual boxes fail |

**Primary metric**: MAE and RMSE on count predictions

**SA note**: Use detection-based counting when objects are well-separated. Switch to density maps when objects overlap heavily (crowd scenes, cell counting).

---

## 4. Semantic Segmentation

**What it does**: Classifies every pixel in the image into a category. Unlike detection, there are no bounding boxes — the output is a full pixel-level mask.

**Output**: A label map the same size as the input image (each pixel = one class)

**Typical use cases**: Road/lane detection in autonomous vehicles, land use classification from satellite imagery, separating foreground material from background in industrial inspection

| Dimension | Value |
|---|---|
| Capability | Predictive AI — multi-class classification (one label per pixel) |
| Learning paradigm | Supervised — requires pixel-level annotated masks (very expensive to label; tools like Labelme or Scale AI help) |
| Model architecture | Neural networks — CNN: **UNet** (encoder-decoder, standard for medical/industrial imaging), **DeepLab v3+** (dilated convolutions for fine boundaries), **SegFormer** (Transformer-based, state of the art) |

**Primary metric**: **mIoU** (mean Intersection over Union per class)

---

## 5. Instance Segmentation

**What it does**: Like semantic segmentation, but distinguishes individual object instances — each car, each person, each defect gets its own separate mask.

**Output**: Per-object pixel mask + class label (car1 mask, car2 mask — not just "car pixels")

**Typical use cases**: Counting and measuring individual parts on a production line, surgical instrument tracking, cell biology

| Dimension | Value |
|---|---|
| Capability | Predictive AI — multi-class classification (what is it?) + regression (pixel mask per instance) |
| Learning paradigm | Supervised — requires instance-level mask annotations (more expensive than bounding boxes) |
| Model architecture | Neural networks — CNN: **Mask R-CNN** (standard), **YOLO with segmentation head** (faster), **SAM** (Segment Anything Model — can be prompted with a point or box, reducing annotation need) |

**Primary metric**: mAP computed with mask IoU instead of bounding box IoU

**SA note**: SAM (Meta) is a game-changer for annotation cost — it can generate masks from a single point click, drastically reducing labeling effort.

---

## 6. Pose Estimation

**What it does**: Detects the positions of anatomical keypoints (joints, landmarks) on a person or object, producing a skeleton or structural representation.

**Output**: (x, y) coordinates per keypoint — e.g., 17 joints for a human body

**Typical use cases**: Worker ergonomics / safety monitoring on factory floors, gesture recognition, sports performance analysis, robot arm joint tracking

| Dimension | Value |
|---|---|
| Capability | Predictive AI — regression (multiple output: x/y coordinates per keypoint) |
| Learning paradigm | Supervised — requires images labeled with keypoint coordinates |
| Model architecture | Neural networks — CNN: **HRNet** (high-resolution representation, most accurate), **OpenPose** (multi-person, real-time), **MediaPipe** (lightweight, runs on mobile/edge) |

**Primary metric**: **PCK** (Percentage of Correct Keypoints) at a distance threshold; **OKS** (Object Keypoint Similarity) for COCO benchmark

---

## 7. OCR (Optical Character Recognition)

**What it does**: Extracts text content from images — scanned documents, photos of signs, printed labels, handwritten forms.

**Output**: Extracted text string (and optionally bounding boxes per word/character)

**Typical use cases**: Digitizing paper documents, reading part numbers from photos, invoice processing, reading labels on packaging

| Dimension | Value |
|---|---|
| Capability | Predictive AI — classification (character-level or sequence-to-sequence: map image regions to text tokens) |
| Learning paradigm | Supervised (labeled image-text pairs) — modern models also use Self-supervised pre-training on large document corpora |
| Model architecture | Neural networks — CNN + Transformer: **TrOCR** (Microsoft, transformer encoder-decoder), **PaddleOCR** (practical, multilingual), **Tesseract** (traditional, rule-based — use only as a baseline) |

**Primary metric**: **CER** (Character Error Rate) and **WER** (Word Error Rate)

**SA note**: For structured document extraction (invoices, forms) combine OCR with a layout-aware model (LayoutLM, Donut) to also capture the spatial structure.

---

## 8. Visual Anomaly Detection

**What it does**: Flags images or regions that deviate from a learned "normal" appearance — without needing labeled examples of defects.

**Output**: Anomaly score per image or anomaly heatmap per pixel

**Typical use cases**: Surface defect detection on production lines, PCB inspection, pharmaceutical tablet inspection — wherever defects are rare and hard to label

| Dimension | Value |
|---|---|
| Capability | Predictive AI — binary classification (anomaly / normal) |
| Learning paradigm | Unsupervised — trained only on images of good/normal parts; no defect labels required. Anomalies are detected as deviations from the learned normal distribution. |
| Model architecture | Neural networks — CNN: **Autoencoder** (reconstructs normal images; high reconstruction error = anomaly), **PatchCore** (stores patch embeddings of normal images, flags patches far from the normal distribution — state of the art on MVTec benchmark) |

**Primary metric**: **AUROC** per image; **PRO** (Per-Region Overlap) for pixel-level anomaly maps

**SA note**: This is the most common starting point for visual quality inspection when defect images are not available. See also the note in [[1 - Overview]] on how anomaly detection maps to the 4 dimensions.

---

## 9. Action Recognition (Video)

**What it does**: Classifies the activity or action occurring in a video clip — operates on sequences of frames, not single images.

**Output**: Activity class label per video clip (walking, picking, falling, welding)

**Typical use cases**: Worker safety monitoring (detecting falls, unsafe behavior), gesture-based control, surveillance, sports analytics

| Dimension | Value |
|---|---|
| Capability | Predictive AI — multi-class classification |
| Learning paradigm | Supervised — requires labeled video clips (expensive; each clip needs a start/end timestamp and activity label) |
| Model architecture | Neural networks — **3D CNN** (SlowFast — processes spatial and temporal features simultaneously), **Video Transformer** (TimeSformer, VideoMAE — higher accuracy, more compute) |

**Primary metric**: Top-1 / Top-5 accuracy on clip-level classification

**SA note**: Collecting and labeling video data is significantly more expensive than images. Consider whether pose estimation (tracking worker skeleton over time) can replace full video classification at lower annotation cost.

---

## 10. Image Generation

**What it does**: Creates new synthetic images from a text prompt, a reference image, or random noise. Not a predictive task — the output is novel content.

**Output**: New image(s)

**Typical use cases**: Generating synthetic training data to augment scarce defect datasets, product visualization from text descriptions, creating variation for data augmentation

| Dimension | Value |
|---|---|
| Capability | Generative AI |
| Learning paradigm | Self-supervised — models are trained on massive unlabeled image datasets by learning to denoise (diffusion) or to fool a discriminator (GANs). No per-image labels needed. |
| Model architecture | Neural networks — **Diffusion models** (Stable Diffusion, DALL-E 3 — current state of the art, high quality), **GANs** (faster inference, less stable training — still used for domain-specific generation) |

**Primary metric**: **FID** (Fréchet Inception Distance) — measures similarity between generated and real image distributions; lower is better. Human eval for specific use cases.

**SA note**: In manufacturing, the most practical use of image generation is **synthetic defect augmentation** — generate realistic defect images to overcome dataset imbalance for the defect detection model.

---

## 11. Depth Estimation

**What it does**: Predicts the distance from the camera to each pixel in a single 2D image (monocular depth estimation) — reconstructing 3D structure from a flat image.

**Output**: Per-pixel depth map (same resolution as input)

**Typical use cases**: Robot navigation and pick-and-place, autonomous vehicles, 3D scene reconstruction, AR overlays in industrial maintenance

| Dimension | Value |
|---|---|
| Capability | Predictive AI — regression (multiple output: one depth value per pixel) |
| Learning paradigm | Supervised (depth sensor ground truth from LiDAR or structured light) or Self-supervised (stereo image pairs or monocular video consistency as the supervision signal — no depth sensor needed) |
| Model architecture | Neural networks — CNN + Transformer: **MiDaS** (robust zero-shot depth, runs on a single image), **DPT** (dense prediction transformer, higher accuracy) |

**Primary metric**: **AbsRel** (absolute relative error), **RMSE** on depth values, **δ < 1.25** (fraction of predictions within 25% of ground truth)

---

## 12. Change Detection

**What it does**: Compares two images of the same scene taken at different times and identifies regions that have changed.

**Output**: Binary change mask (changed / unchanged per pixel or region)

**Typical use cases**: Monitoring construction sites or factory floor layouts from satellite/drone imagery, detecting tampering in security footage, tracking product changes on a shelf

| Dimension | Value |
|---|---|
| Capability | Predictive AI — binary classification (changed / unchanged per region or pixel) |
| Learning paradigm | Supervised (pairs of images with labeled change masks) or Unsupervised (compare feature embeddings of two images without labels) |
| Model architecture | Neural networks — **Siamese CNN** (two identical networks process each image; the difference in their embeddings flags change), **ChangeFormer** (Transformer-based, higher accuracy on complex scenes) |

**Primary metric**: F1 score on the change mask (precision/recall on changed pixels)

---

## Technical

The representations aren't alternatives you choose randomly — they're tools for different jobs. Let me make it concrete.

Take **two pixels** of the same orange color, one bright and one dim:

| Bright orange | Dim orange (same color, less light) |                   |
| ------------- | ----------------------------------- | ----------------- |
| **RGB**       | `[255, 140, 0]`                     | `[128, 70, 0]`    |
| **Grayscale** | `[136]`                             | `[68]`            |
| **HSV**       | `[33°, 1.0, 1.0]`                   | `[33°, 1.0, 0.5]` |
Notice: In HSV the **Hue stays 33° in both cases** — because it's the same orange. RGB changes completely. This is why the choice of color space matters for your task.

**When to use which:**

**RGB** — the default. Every image from a camera is RGB. Use it when:

- Feeding images into a CNN (most deep learning models expect RGB)
- You need all color information

**Grayscale** — drop color, keep brightness. Use it when:

- Color doesn't help your task (e.g. reading text, detecting shapes, X-rays)
- You want to reduce memory and computation (3× fewer values)
- Edge detection (edges are brightness changes, color is irrelevant)

**HSV** — separate "what color" from "how bright". Use it when:

- You want to **detect a specific color** reliably (e.g. "find all red objects")
- Lighting varies — in RGB a red apple in shadow looks totally different than in sunlight, but its Hue stays roughly the same
- Example: traffic light detection — filter `Hue ≈ 0°` (red), ignore Value (brightness)


---

## Related pages

- [[1 - Overview]]
- [[Use cases manufacturing]]
- [[1.1 - Metrics]]
