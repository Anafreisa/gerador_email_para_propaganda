import csv
import smtplib

my_email = EMAIL
password = EMAIL_PASSWORD

users_data = open('usuarios_data.csv', 'r', encoding='utf-8')
reader = csv.reader(users_data)

user = []
for row in reader:
    user.append(row)

for n in range(len(user)):
    if user[n][3] == "M":
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"{user[n][2]}",
                msg=f"Subject:Estamos com saudade!\n\n{user[n][0]} Ja viu que a Cerveja esta em promocao?!"
                # Caso queira enviar propaganda do último produto comprado:
                # msg=f"Subject:Estamos com saudade!\n\n{user[n][0]} Ja viu que {user[n][8]} esta em promocao?!"
            )
