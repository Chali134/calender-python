from tkinter import *
import calendar

# Create main window with new styling
win = Tk()
win.title("Futuristic Calendar Viewer")
win.geometry('450x500')
win.config(bg='#121212')

# Function to display the calendar
def display_calendar():
    year_str = year.get()
    month_str = month.get()
    year_int = int(year_str)
    month_int = int(month_str)
    
    # Get the calendar text and format it
    cal = calendar.month(year_int, month_int)
    
    # Adjust formatting to make the calendar more centered and visually aligned
    formatted_cal = ''
    for line in cal.split('\n'):
        formatted_cal += line.center(20) + '\n'  # Center-align each line of the calendar
    
    # Clear existing text and insert the new formatted calendar
    textfield.delete(0.0, END)
    textfield.insert(INSERT, formatted_cal)

# Function to clear the text field
def clear_calendar():
    textfield.delete(0.0, END)

# Style variables
LABEL_FONT = ('Century Gothic', 14, 'bold')
ENTRY_FONT = ('Century Gothic', 12)
BTN_FONT = ('Century Gothic', 12, 'bold')
TEXT_BG = '#1f1f1f'
TEXT_FG = '#f8f8f8'
BTN_BG = '#ff6b6b'
BTN_FG = 'white'

# Create a frame for layout to center elements
frame = Frame(win, bg='#121212')
frame.pack(expand=True)

# Header text
header = Label(frame, text='Calendar', font=('Century Gothic', 18, 'bold'), bg='#121212', fg='#ffffff')
header.grid(row=0, columnspan=3, pady=(10, 20))

# Create labels for year and month
label1 = Label(frame, text='Year:', font=LABEL_FONT, bg='#121212', fg='#f8f8f8')
label1.grid(row=1, column=0, padx=10, pady=10, sticky=E)

label2 = Label(frame, text='Month:', font=LABEL_FONT, bg='#121212', fg='#f8f8f8')
label2.grid(row=1, column=1, padx=10, pady=10, sticky=E)

# Create Spinboxes for year and month selection
year = Spinbox(frame, from_=1947, to=2150, width=10, font=ENTRY_FONT, bg='#2a2a2a', fg='white', justify=CENTER, bd=0, relief=FLAT)
year.grid(row=2, column=0, padx=10, pady=10)

month = Spinbox(frame, from_=1, to=12, width=5, font=ENTRY_FONT, bg='#2a2a2a', fg='white', justify=CENTER, bd=0, relief=FLAT)
month.grid(row=2, column=1, padx=10, pady=10)

# Create a stylish button to display calendar
button = Button(frame, text="Generate", command=display_calendar, font=BTN_FONT, bg=BTN_BG, fg=BTN_FG, activebackground='#ff8787', activeforeground='white', bd=0, padx=20, pady=10, relief=FLAT, highlightthickness=0)
button.grid(row=2, column=2, padx=10, pady=10)

# Create a stylish button to clear the calendar
clear_button = Button(frame, text="Clear", command=clear_calendar, font=BTN_FONT, bg=BTN_BG, fg=BTN_FG, activebackground='#ff8787', activeforeground='white', bd=0, padx=20, pady=10, relief=FLAT, highlightthickness=0)
clear_button.grid(row=3, columnspan=3, padx=10, pady=(10, 20))

# Create a styled text field to display the calendar
textfield = Text(frame, height=10, width=30, font=('Courier', 12), bg=TEXT_BG, fg=TEXT_FG, bd=0, padx=15, pady=15, relief=FLAT, highlightthickness=0)
textfield.grid(row=4, columnspan=3, padx=20, pady=(20, 10))

# Add a shadow effect around the frame
frame_shadow = Label(win, bg='#1f1f1f', width=50, height=2)
frame_shadow.pack(fill=X, padx=10)

win.mainloop()
