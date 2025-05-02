import os
from PIL import Image

def compressor(path_to_file: str, quality: int = 30):
    try:
        # Validate file extension
        if not path_to_file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            print("❌ Unsupported file type.")
            return

        # Get original file size
        original_size = os.path.getsize(path_to_file)

        # Open and compress image
        img = Image.open(path_to_file)
        img.save(path_to_file, optimize=True, quality=quality)

        # Get new file size
        compressed_size = os.path.getsize(path_to_file)

        print(f"✅ Successfully compressed: {os.path.basename(path_to_file)}")
        print(f"🔹 Original size: {original_size // 1024} KB")
        print(f"🔻 Compressed size: {compressed_size // 1024} KB")
        print(f"📉 Reduction: {100 - (compressed_size / original_size) * 100:.1f}%")

    except Exception as e:
        print(f"⚠️ Error compressing {path_to_file}: {e}")

if __name__ == "__main__":
    # Example usage
    path = input("Enter path to image file: ")
    compressor(path)
