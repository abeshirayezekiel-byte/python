import tkinter as tk
from datetime import datetime

# Function to handle the Check In button click
def check_in():
    # 1. Read the typed name from the Entry widget
    participant_name = name_entry.get().strip()
    
    # Check if the user entered a name
    if not participant_name:
        participant_name = "Participant"
        
    # 2. Get the current or workshop date
    # You can customize the date string here as required
    workshop_date = datetime.now().strftime("%B %d, %Y")
    
    # 3. Create the multi-line welcome message
    welcome_message = (
        f"Welcome, {participant_name}!\n"
        f"Thank you for joining our workshop today.\n"
        f"Date of Workshop: {workshop_date}\n"
        f"We hope you have a great learning experience!"
    )
    
    # 4. Update the Text output area
    # Enable editing temporarily to update the text
    output_text.config(state=tk.NORMAL)
    
    # Clear any previous content in the Text widget
    output_text.delete("1.0", tk.END)
    
    # Insert the new greeting message
    output_text.insert(tk.END, welcome_message)
    
    # Disable editing again to keep it read-only for the user
    output_text.config(state=tk.DISABLED)

# Create the main desktop window
window = tk.Tk()
window.title("Workshop Participant Greeting")
window.geometry("450x400")

# --- Widgets ---

# 1. Label widget for instructions
instructions_label = tk.Label(
    window, 
    text="Please enter your name below to check into the workshop:",
    font=("Arial", 11),
    pady=10
)
instructions_label.pack()

# 2. Entry widget to collect the participant's name
name_entry = tk.Entry(window, font=("Arial", 12), width=30)
name_entry.pack(pady=5)

# 3. Button widget to trigger the check_in function
check_in_button = tk.Button(
    window, 
    text="Check In", 
    command=check_in, 
    font=("Arial", 11, "bold"),
    bg="#4CAF50", 
    fg="white", 
    padx=10, 
    pady=5
)
check_in_button.pack(pady=15)

# 4. Text widget to display the multi-line welcome message
output_text = tk.Text(
    window, 
    height=8, 
    width=45, 
    font=("Arial", 11), 
    bg="#f0f0f0", 
    state=tk.DISABLED # Starts as read-only until button is clicked
)
output_text.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
