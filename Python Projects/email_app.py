import os
import smtplib
import tkinter as tk
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from tkinter import filedialog, messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email():
    sender_email: str = sender_entry.get()
    password:  str =pass_entry.get()
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END).strip()

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    image_path = image_entry.get()
    pdf_path = pdf_entry.get()

    # Attaching Image
    if image_path and os.path.getsize(image_path) <= 3 * 1024 * 1024:
        with open(image_path, 'rb') as f:
            img_data = f.read()
        image = MIMEImage(img_data, name=f.name)
        msg.attach(image)
    elif image_path:
        messagebox.showerror("Image size exceeds the limit of 2 MB.")
        return

    # Attaching PDF
    if pdf_path and os.path.getsize(pdf_path) <= 10 * 1024 * 1024:
        with open(pdf_path, 'rb') as file:
            pdf_data = file.read()
        pdf = MIMEApplication(pdf_data, name=file.name)
        msg.attach(pdf)
    elif pdf_path:
        messagebox.showerror("PDF size exceeds the limit of 10 MB.")
        return

    # Sending email
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        messagebox.showinfo("Email Sent", "Email sent successfully!")
    except smtplib.SMTPException as e:
        messagebox.showerror("Error", f"Error sending email: {str(e)}")

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    image_entry.delete(0, tk.END)
    image_entry.insert(0, file_path)
def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_entry.delete(0, tk.END)
    pdf_entry.insert(0, file_path)

def clear_fields():
    # Clear all entry fields
    sender_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)
    receiver_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    message_text.delete("1.0", tk.END)
    image_entry.delete(0, tk.END)
    pdf_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Email Sender")
root.geometry('560x480')
root.resizable(False,False)

# Sender
sender_label = tk.Label(root, text="Sender's Email",font=('Helvetica',14))
sender_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
sender_entry = tk.Entry(root, bd=2, highlightthickness=1, highlightbackground='gray',width=32)
sender_entry.grid(row=0, column=1, padx=5, pady=5)

#Password
pass_label = tk.Label(root, text="Password",font=('Helvetica',14))
pass_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
pass_entry = tk.Entry(root, bd=2, highlightthickness=1, highlightbackground='gray',width=32,show='*')
pass_entry.grid(row=1, column=1, padx=5, pady=5)

# Receiver
receiver_label = tk.Label(root, text="Receiver's Email", font=('Helvetica',14))
receiver_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
receiver_entry = tk.Entry(root, bd=2, highlightthickness=1, highlightbackground='gray', width=32)
receiver_entry.grid(row=2, column=1, padx=5, pady=5)

# Subject
subject_label = tk.Label(root, text="Subject", font=('Helvetica',14))
subject_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
subject_entry = tk.Entry(root, bd=2, highlightthickness=1, highlightbackground='gray', width=32)
subject_entry.grid(row=3, column=1, padx=5, pady=5)

# Message
message_label = tk.Label(root, text="Message", font=('Helvetica',14))
message_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
message_text = tk.Text(root, height=10, width=32, bd=2, highlightthickness=1, highlightbackground='gray')
message_text.grid(row=4, column=1, padx=5, pady=5)

# Image Attachment
image_label = tk.Label(root, text="Image Attachment", font=('Helvetica',14))
image_label.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
image_entry = tk.Entry(root, bd=2, highlightthickness=1, highlightbackground='gray', width=32)
image_entry.grid(row=5, column=1, padx=5, pady=5)
image_button = tk.Button(root, text="Browse", font=('Bold',8), command=browse_image,  padx=6,pady=3)
image_button.grid(row=5, column=2, padx=5, pady=5)

# PDF Attachment
pdf_label = tk.Label(root, text="PDF Attachment", font=('Helvetica',14))
pdf_label.grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)
pdf_entry = tk.Entry(root, bd=2, highlightthickness=1, highlightbackground='gray', width=32)
pdf_entry.grid(row=6, column=1, padx=5, pady=5)
pdf_button = tk.Button(root, text="Browse", font=('Bold',8), command=browse_pdf, padx=6,pady=3)
pdf_button.grid(row=6, column=2, padx=5, pady=5)

# Email Button
send_button = tk.Button(root, text="Send Email", font=('Bold',10), command=send_email, padx=5,pady=4)
send_button.grid(row=7, column=1, padx=5, pady=5)

# Clear Button
clear_button = tk.Button(root, text="Clear", command=clear_fields, padx=5, pady=5)
clear_button.grid(row=7, column=2, padx=5,pady=5)

root.mainloop()
