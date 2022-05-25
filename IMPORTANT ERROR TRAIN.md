Terkait gagal trainin bisa disebabkan oleh belum terbentuknya file train.txt atau file train yang masih kosong. Problemnya adalah terdapat error saat melakukan execute pada file process.py/generate_train.py. Silahkan dicek terlebih dahulu apakah file train.txt sudah terbentuk dan isinya apakah sudah ada?
Pastikan running process.py/generate_train.py dan pastikan file train ada seperti gambar di bawah.

Alternatif: Silahkan buat file train.txt (masih kosong), lalu run baris
```python
import glob
images_list = glob.glob("data/obj/*.jpg")
with open("data/train.txt", "w") as f:
    f.write("\n".join(images_list))
```

Atau jika anda punya cara lain untuk menggabungkan nama file foto menjadi baris pada file train.txt juga bisa digunakan.
Format baris pada file train.txt : path/nama_foto.jpg 
Contoh : data/obj/diode (75).jpg

https://mail.google.com/mail/u/0?ui=2&ik=08c8027e95&attid=0.1&permmsgid=msg-a:r5348721128262185816&th=180f91c4974dce16&view=fimg&fur=ip&sz=s0-l75-ft&attbid=ANGjdJ-VQmh-vl888nuGkaZdDf66sDkPekOhL-wvQgpWOHwWV9s7809miXhUiGrLenlZxc3SjjrYI26tGI2L5wYdW7FdEGBWr0bNKruGVD1V477AAiVKVitfUfFKXmE&disp=emb&realattid=ii_l3kzbmz10
