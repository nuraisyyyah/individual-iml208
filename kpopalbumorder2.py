import tkinter as tk
from tkinter import messagebox

def add_to_cart():
    try:
        selected_index = album_listbox.curselection()[0]
        album = albums[selected_index]
        quantity = int(quantity_entry.get())

        if quantity <= 0:
            messagebox.showerror("Invalid Quantity", "Please enter a valid quantity greater than 0.")
            return

        cart.append((album, quantity))
        cart_listbox.insert(tk.END, f"{album} x{quantity}")
        quantity_entry.delete(0, tk.END)
    except IndexError:
        messagebox.showerror("No Album Selected", "Please select an album to add to the cart.")
    except ValueError:
        messagebox.showerror("Invalid Quantity", "Please enter a valid number for quantity.")

def get_total():
    return sum(album[2] * quantity for album, quantity in cart)

def checkout():
    if not cart:
        messagebox.showerror("Cart Empty", "Your cart is empty. Add items before checking out.")
        return

    name = name_entry.get().strip()
    contact = contact_entry.get().strip()
    address = address_entry.get().strip()
    payment_method = payment_var.get()

    if not name or not contact or not address:
        messagebox.showerror("Missing Information", "Please provide your name, contact number, and address.")
        return

    if payment_method == "None":
        messagebox.showerror("Payment Method Missing", "Please select a payment method before proceeding.")
        return

    total = get_total()
    discount_code = discount_entry.get().strip().upper()

    if discount_code == "SARANGHAE":
        discount = total * 0.10
        total -= discount
        messagebox.showinfo("Discount Applied", f"Discount of RM{discount:.2f} applied!")
    elif discount_code:
        messagebox.showerror("Invalid Code", "The discount code entered is invalid. No discount applied.")

    messagebox.showinfo(
        "Checkout",
        f"Customer Name: {name}\nContact: {contact}\nAddress: {address}\n"
        f"Payment Method: {payment_method}\nTotal: RM{total:.2f}\nThank you for your purchase!"
    )

    clear_cart()
    name_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    discount_entry.delete(0, tk.END)
    payment_var.set("None")

def clear_cart():
    cart.clear()
    cart_listbox.delete(0, tk.END)

# Initialize the application
root = tk.Tk()
root.title("K-pop Album Store By Nuraisyah")
root.geometry("1600x1000")

albums = [
    ("BOYNEXTDOOR - HOW?", "Sticker Version", 45.60),
    ("BOYNEXTDOOR - 19.99", "Clink Version", 47.50),
    ("THE BOYZ - Thrill-ing", "Splash Version", 55.90),
    ("THE BOYZ - Reveal", "Wolf Version", 50.90),
    ("EXO - Don't Mess Up My Tempo", "Andante Version", 63.25),
    ("EXO - The War", "Regular A Version", 75.00),
    ("D.O - SYMPATHY", "Digipack Version", 34.90),
    ("KAI - Rover", "Sleeve Version", 44.90),
    ("Queen of Tears", "Korean Drama Sound Track", 80.50),
    ("Lovely Runner", "Korean Drama Sound Track", 78.00),
]

cart = []

album_listbox = tk.Listbox(root, height=20, width=60, font=("arial", 10), bg="lightpink", fg="grey")
album_listbox.grid(row=0, column=0, rowspan=6)

for album in albums:
    album_listbox.insert(tk.END, f"{album[0]} ({album[1]}) - RM{album[2]:.2f}")

quantity_label = tk.Label(root, text="Quantity:", font=("arial", 15))
quantity_label.grid(row=2, column=1)
quantity_entry = tk.Entry(root, font=("arial", 15))
quantity_entry.grid(row=2, column=2)

add_to_cart_button = tk.Button(root, text="Add to Cart", command=add_to_cart, font=("arial", 15), bg="purple", fg="white")
add_to_cart_button.grid(row=3, column=1)

checkout_button = tk.Button(root, text="Checkout", command=checkout, font=("arial", 15), bg="lightgreen", fg="white")
checkout_button.grid(row=10, column=1)

clear_cart_button = tk.Button(root, text="Clear Cart", command=clear_cart, font=("arial", 15), bg="red", fg="white")
clear_cart_button.grid(row=3, column=2)

customer_info_label = tk.Label(root, text="Customer Information:", font=("arial", 17, "bold"))
customer_info_label.grid(row=4, column=1)

name_label = tk.Label(root, text="Name:", font=("arial", 13))
name_label.grid(row=5, column=1)
name_entry = tk.Entry(root, font=("arial", 13), width=35)
name_entry.grid(row=5, column=2)

contact_label = tk.Label(root, text="Contact Number:", font=("arial", 13))
contact_label.grid(row=5, column=3)
contact_entry = tk.Entry(root, font=("arial", 13))
contact_entry.grid(row=5, column=4)

address_label = tk.Label(root, text="Address:", font=("arial", 13))
address_label.grid(row=6, column=1)
address_entry = tk.Entry(root, font=("arial", 13), width=35)
address_entry.grid(row=6, column=2)

payment_label = tk.Label(root, text="Payment Method:", font=("arial", 13))
payment_label.grid(row=7, column=1)

payment_var = tk.StringVar(value="None")
payment_var.set("None")
payment_card = tk.Radiobutton(root, text="Credit/Debit Card", font=("arial", 13))
payment_card.grid(row=7, column=2)
payment_online = tk.Radiobutton(root, text="Online Banking", font=("arial", 13))
payment_online.grid(row=8, column=2)
payment_ewallet = tk.Radiobutton(root, text="E-Wallet", font=("arial", 13))
payment_ewallet.grid(row=9, column=2)
payment_cod = tk.Radiobutton(root, text="Cash on Delivery", font=("arial", 13))
payment_cod.grid(row=10, column=2)

# Discount Code
discount_label = tk.Label(root, text="Discount Code:", font=("arial", 13))
discount_label.grid(row=7, column=3)
discount_entry = tk.Entry(root, font=("arial", 13))
discount_entry.grid(row=7, column=4)


cart_label = tk.Label(root, text="Your Cart:", font=("arial", 17, "bold"))
cart_label.grid(row=5, column=0)
cart_listbox = tk.Listbox(root, height=20, width=60, font=("arial", 10), bg="lightblue", fg="grey")
cart_listbox.grid(row=6, column=0, rowspan=6)

messagebox.showinfo("Greeting", "Annyeonghaseyo, Welcome to StoreNextDoor!")
root.mainloop()
