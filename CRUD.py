import sqlite3

# Membuat dan menghubungkan ke database SQLite
conn = sqlite3.connect('club_members.db')
cursor = conn.cursor()

# Membuat tabel anggota klub jika belum ada
cursor.execute('''
CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    position TEXT,
    team TEXT
)
''')
conn.commit()

# Fungsi untuk menambahkan anggota baru
def add_member(name, age, position, team):
    cursor.execute('''
        INSERT INTO members (name, age, position, team) 
        VALUES (?, ?, ?, ?)''', (name, age, position, team))
    conn.commit()
    print(f"Anggota {name} berhasil ditambahkan!")

# Fungsi untuk menampilkan semua anggota
def show_members():
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()
    if members:
        for member in members:
            print(f"ID: {member[0]}, Nama: {member[1]}, Umur: {member[2]}, Posisi: {member[3]}, Tim: {member[4]}")
    else:
        print("Belum ada anggota yang terdaftar.")

# Fungsi untuk memperbarui anggota
def update_member(member_id, name=None, age=None, position=None, team=None):
    cursor.execute("SELECT * FROM members WHERE id=?", (member_id,))
    member = cursor.fetchone()
    if member:
        new_name = name if name else member[1]
        new_age = age if age else member[2]
        new_position = position if position else member[3]
        new_team = team if team else member[4]
        cursor.execute('''
            UPDATE members 
            SET name=?, age=?, position=?, team=? 
            WHERE id=?''', (new_name, new_age, new_position, new_team, member_id))
        conn.commit()
        print(f"Data anggota ID {member_id} berhasil diperbarui!")
    else:
        print(f"Anggota dengan ID {member_id} tidak ditemukan.")

# Fungsi untuk menghapus anggota
def delete_member(member_id):
    cursor.execute("SELECT * FROM members WHERE id=?", (member_id,))
    member = cursor.fetchone()
    if member:
        cursor.execute("DELETE FROM members WHERE id=?", (member_id,))
        conn.commit()
        print(f"Anggota ID {member_id} berhasil dihapus!")
    else:
        print(f"Anggota dengan ID {member_id} tidak ditemukan.")

# Main program (contoh penggunaan)
if __name__ == "__main__":
    while True:
        print("\n=== Sistem CRUD Anggota Klub Bola ===")
        print("1. Tambah Anggota")
        print("2. Lihat Semua Anggota")
        print("3. Perbarui Anggota")
        print("4. Hapus Anggota")
        print("5. Keluar")
        choice = input("Pilih opsi (1-5): ")

        if choice == '1':
            name = input("Nama: ")
            age = int(input("Umur: "))
            position = input("Posisi: ")
            team = input("Tim: ")
            add_member(name, age, position, team)

        elif choice == '2':
            show_members()

        elif choice == '3':
            member_id = int(input("ID Anggota yang ingin diperbarui: "))
            print("Tekan enter jika tidak ingin mengubah field.")
            name = input("Nama baru (kosongkan jika tidak ada perubahan): ")
            age = input("Umur baru (kosongkan jika tidak ada perubahan): ")
            age = int(age) if age else None
            position = input("Posisi baru (kosongkan jika tidak ada perubahan): ")
            team = input("Tim baru (kosongkan jika tidak ada perubahan): ")
            update_member(member_id, name, age, position, team)

        elif choice == '4':
            member_id = int(input("ID Anggota yang ingin dihapus: "))
            delete_member(member_id)

        elif choice == '5':
            print("Keluar dari program...")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")
