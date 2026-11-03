import os
import cv2
import numpy as np

os.environ['MPLCONFIGDIR'] = r'C:\Users\LENOVO\.gemini\antigravity\brain\b768dafa-3595-483f-97f3-a6502a8b1ef6\scratch'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

repo_dir = r'C:\Users\LENOVO\.gemini\antigravity\scratch\Image-Handling-and-Pixel-Transformations-Using-OpenCV'
assets_dir = os.path.join(repo_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)

# 1. Read image as color, convert BGR to RGB
img_bgr = cv2.imread(os.path.join(repo_dir, 'sunflower.jpg'), cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
h, w, c = img_rgb.shape

# 1 & 3: Grayscale image
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
fig, ax = plt.subplots(figsize=(4, 6))
ax.imshow(img_gray, cmap='gray')
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_1_gray.png'), bbox_inches='tight', dpi=150)
plt.close()

# 4: Save image as PNG
cv2.imwrite(os.path.join(assets_dir, 'sunflower_saved.png'), img_bgr)

# 6: Display color image
fig, ax = plt.subplots(figsize=(4, 6))
ax.imshow(img_rgb)
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_2_color.png'), bbox_inches='tight', dpi=150)
plt.close()

# 7: Crop the sunflower head
crop = img_rgb[280:620, 130:460]
fig, ax = plt.subplots(figsize=(4.5, 5))
ax.imshow(crop)
ax.set_title("Cropped Region")
ax.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_3_crop.png'), bbox_inches='tight', dpi=150)
plt.close()

# 8 & 9: Resize and Flip
res = cv2.resize(crop, (crop.shape[1] * 2, crop.shape[0] * 2))
flip = cv2.flip(res, 1)
fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(flip)
ax.set_title("Flipped Horizontally")
ax.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_4_flip.png'), bbox_inches='tight', dpi=150)
plt.close()

# 10 & 11: Text added to image
img_text = img_rgb.copy()
cv2.putText(img_text, "Sunflower, Nature Photography on Summer Morning", (20, 980),
            cv2.FONT_HERSHEY_SIMPLEX, 0.62, (255, 255, 255), 2)
fig, ax = plt.subplots(figsize=(4, 6))
ax.imshow(img_text)
ax.set_title("New image")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_5_text.png'), bbox_inches='tight', dpi=150)
plt.close()

# 12 & 13: Magenta rectangle encompassing the sunflower
img_rect = img_text.copy()
rcol = (255, 0, 255)
cv2.rectangle(img_rect, (130, 280), (460, 620), rcol, 3)
fig, ax = plt.subplots(figsize=(4, 6))
ax.imshow(img_rect)
ax.set_title("Annotated image")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_6_annotated.png'), bbox_inches='tight', dpi=150)
plt.close()

# 15, 16, 17: Adjust brightness
m = np.ones(img_rgb.shape, dtype="uint8") * 50
img_brighter = cv2.add(img_rgb, m)
img_darker = cv2.subtract(img_rgb, m)

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1), plt.imshow(img_rgb), plt.title("Original Image"), plt.axis("off")
plt.subplot(1, 3, 2), plt.imshow(img_brighter), plt.title("Brighter Image"), plt.axis("off")
plt.subplot(1, 3, 3), plt.imshow(img_darker), plt.title("Darker Image"), plt.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_7_brightness.png'), bbox_inches='tight', dpi=150)
plt.close()

# 18, 19: Modify image contrast
matrix1 = np.ones(img_rgb.shape, dtype="float32") * 1.1
matrix2 = np.ones(img_rgb.shape, dtype="float32") * 1.2
img_higher1 = cv2.multiply(img_rgb.astype("float32"), matrix1).clip(0, 255).astype("uint8")
img_higher2 = cv2.multiply(img_rgb.astype("float32"), matrix2).clip(0, 255).astype("uint8")

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1), plt.imshow(img_rgb), plt.title("Original Image"), plt.axis("off")
plt.subplot(1, 3, 2), plt.imshow(img_higher1), plt.title("Higher Contrast (1.1x)"), plt.axis("off")
plt.subplot(1, 3, 3), plt.imshow(img_higher2), plt.title("Higher Contrast (1.2x)"), plt.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_8_contrast.png'), bbox_inches='tight', dpi=150)
plt.close()

# 20: Split B, G, R channels
b, g, r = cv2.split(img_bgr)
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1), plt.imshow(b, cmap='gray'), plt.title("Blue Channel"), plt.axis("off")
plt.subplot(1, 3, 2), plt.imshow(g, cmap='gray'), plt.title("Green Channel"), plt.axis("off")
plt.subplot(1, 3, 3), plt.imshow(r, cmap='gray'), plt.title("Red Channel"), plt.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_9_bgr_channels.png'), bbox_inches='tight', dpi=150)
plt.close()

# 21: Merged RGB
merged_rgb = cv2.merge([r, g, b])
plt.figure(figsize=(5, 6))
plt.imshow(merged_rgb)
plt.title("Merged RGB Image")
plt.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_10_merged_rgb.png'), bbox_inches='tight', dpi=150)
plt.close()

# 22: Split HSV channels
hsv_img = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
h_ch, s_ch, v_ch = cv2.split(hsv_img)
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1), plt.imshow(h_ch, cmap='gray'), plt.title("Hue Channel"), plt.axis("off")
plt.subplot(1, 3, 2), plt.imshow(s_ch, cmap='gray'), plt.title("Saturation Channel"), plt.axis("off")
plt.subplot(1, 3, 3), plt.imshow(v_ch, cmap='gray'), plt.title("Value Channel"), plt.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_11_hsv_channels.png'), bbox_inches='tight', dpi=150)
plt.close()

# 23: Merged HSV displays along with original image
merged_hsv = cv2.cvtColor(cv2.merge([h_ch, s_ch, v_ch]), cv2.COLOR_HSV2RGB)
combined = np.concatenate((img_rgb, merged_hsv), axis=1)
plt.figure(figsize=(8, 6))
plt.imshow(combined)
plt.title("Original Image  &  Merged HSV Image")
plt.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_12_merged_hsv.png'), bbox_inches='tight', dpi=150)
plt.close()

# 24: Bitwise Operations (AIM Requirement 4: Generate a third image using bitwise operations)
# Create a circular mask centered on the sunflower head
mask = np.zeros(img_rgb.shape[:2], dtype="uint8")
cv2.circle(mask, (295, 450), 170, 255, -1)
bitwise_and_img = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1), plt.imshow(img_rgb), plt.title("Original Image"), plt.axis("off")
plt.subplot(1, 3, 2), plt.imshow(mask, cmap='gray'), plt.title("Circular Mask"), plt.axis("off")
plt.subplot(1, 3, 3), plt.imshow(bitwise_and_img), plt.title("Bitwise AND (Generated Third Image)"), plt.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'output_13_bitwise_operations.png'), bbox_inches='tight', dpi=150)
plt.close()

print('All output images generated successfully!')
