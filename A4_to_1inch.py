from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
import os

# สร้างไฟล์ PDF
def create_pdf_with_images(output_filename, image_paths):
    # ขนาดกระดาษ A4
    width, height = A4
    # สร้าง canvas สำหรับไฟล์ PDF
    c = canvas.Canvas(output_filename, pagesize=A4)

    # ขนาดรูปภาพ 2.5 ซม. x 3.25 ซม.
    image_width = 2.5 * cm  # 2.5 cm ในหน่วยของ ReportLab
    image_height = 3.5 * cm  # 3.25 cm ในหน่วยของ ReportLab

    # กำหนดจำนวนรูปภาพต่อแถวและจำนวนแถว
    images_per_row = 6  # 6 รูปต่อแถวแนวนอน
    rows_per_person = 1  # 1 แถวต่อคน
    rows_per_page = 7    # 7 แถวต่อหน้า

    # คำนวณระยะห่างระหว่างรูปภาพ
    horizontal_spacing = (width - images_per_row * image_width) / (images_per_row + 1)
    vertical_spacing = (height - rows_per_page * image_height) / (rows_per_page + 1)

    # วาดรูปภาพเรียงตามแถวและคอลัมน์
    for person_index in range(min(rows_per_page, len(image_paths) // rows_per_person)):
        # สำหรับแต่ละคน วาดรูป 6 รูปในแถว
        for col in range(images_per_row):
            image_index = person_index * rows_per_person  # ใช้ index ของคน
            if image_index < len(image_paths):  # ตรวจสอบว่ามีรูปภาพอยู่
                # คำนวณตำแหน่ง X, Y สำหรับรูปแต่ละรูป
                x_position = horizontal_spacing + col * (image_width + horizontal_spacing)
                y_position = height - (vertical_spacing + (person_index + 1) * image_height + person_index * vertical_spacing)

                # ใส่รูปภาพในตำแหน่งที่คำนวณไว้
                c.drawImage(image_paths[image_index], x_position, y_position, image_width, image_height)

    # บันทึกไฟล์ PDF เมื่อวาดรูปครบ
    c.save()

# ฟังก์ชันตรวจสอบโฟลเดอร์
def checkDirPath(dir_path):
    if os.path.isdir(dir_path):
        print(f"{dir_path} is a valid directory!")
        return True
    else:
        print(f"{dir_path} is not a valid directory!")
        return False

# เรียกใช้ฟังก์ชันเพื่อสร้าง PDF
output_pdf = os.path.join(os.getcwd(), "output", "output_with_images.pdf")
dir_path = os.path.join(os.getcwd(), "img")

if __name__ == "__main__":
    if checkDirPath(dir_path):
        # ดึงไฟล์รูปภาพทั้งหมดในโฟลเดอร์
        image_files = [f for f in os.listdir(dir_path) if f.endswith(('jpg', 'png', 'jpeg'))]

        # จำกัดจำนวนไฟล์ให้ตรงตามที่ต้องการ
        image_files = image_files[:7]  # รับรูปภาพ 7 คน
        image_paths = [os.path.join(dir_path, f) for f in image_files]

        create_pdf_with_images(output_pdf, image_paths)
        print(f"PDF created: {output_pdf}")
