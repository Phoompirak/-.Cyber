from A4_to_1inch import create_pdf_with_images
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
import os

dir_path = os.path.join(os.getcwd(), "img")

def main():
    dir_schools = [os.path.join(dir_path, school) for school in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, school))]
    school = [school for school in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, school))]

    for idx, dir_sch in enumerate(dir_schools):
        print(f"Process school: {school[idx]}")

        # ดึงไฟล์รูปภาพทั้งหมดในโฟลเดอร์
        image_paths = [os.path.join(dir_sch, f) for f in os.listdir(dir_sch) if f.endswith(('jpg', 'png', 'jpeg'))]
        output_dir = os.path.join(os.getcwd(), 'output', school[idx])

        # Create the output folder if it doesn't exist
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)
            print(f"Created directory: {output_dir}")


        group_size = 7
        result = []
        for i in range(0, len(image_paths), group_size):
            group = image_paths[i:i+group_size]  # ดึงข้อมูลตั้งแต่ index i จนถึง i+group_size
            result.append(group)

        for idx, r in enumerate(result):
            print(f"Rounede file pdf: {len(r)}")
            output_pdf = os.path.join(output_dir, f"output_{school[idx]}_{idx + 1}.pdf")
            if len(r) <= 7:
                create_pdf_with_images(output_pdf, r)
        
        print("\n")


if __name__ == '__main__':
    main()
    