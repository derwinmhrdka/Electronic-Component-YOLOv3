Terkait gagal training bisa disebabkan oleh belum terbentuknya file train.txt atau file train yang masih kosong. Problemnya adalah terdapat error saat melakukan execute pada file process.py/generate_train.py. Silahkan dicek terlebih dahulu apakah file train.txt sudah terbentuk dan isinya apakah sudah ada?
Pastikan running process.py/generate_train.py dan pastikan file train ada seperti gambar di bawah.

Alternatif: Silahkan buat file train.txt (masih kosong), lalu run baris
```python
import glob
images_list = glob.glob("data/obj/*.jpg")
with open("data/train.txt", "w") as f:
    f.write("\n".join(images_list))
```
Lalu copy file tersebut ke direkori darknet
Atau jika anda punya cara lain untuk menggabungkan nama file foto menjadi baris pada file train.txt juga bisa digunakan.
Format baris pada file train.txt : path/nama_foto.jpg 
Contoh : data/obj/diode (75).jpg

![Train](https://user-images.githubusercontent.com/65268884/170170925-c5e2a408-41c1-49a6-95dc-b4a26716fae9.PNG)
