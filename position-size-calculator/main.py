import tkinter as tk
import tkinter.font as tfont


root = tk.Tk()

left_align = 120
right_align = 370

canvas1 = tk.Canvas(root, width=550, height=600)
canvas1.pack()

heading_font = tfont.Font(size=28)
heading = tk.Label(canvas1, text="Position Size Calculator", font=heading_font)
canvas1.create_window(275, 25, window=heading)

vl = tk.Label(canvas1, text="Account value")
rl = tk.Label(canvas1, text="Risk as percent of account")
sl = tk.Label(canvas1, text="Stop price")
bl = tk.Label(canvas1, text="Entry price")

canvas1.create_window(left_align, 100, window=vl)
canvas1.create_window(right_align, 100, window=rl)
canvas1.create_window(left_align, 160, window=bl)
canvas1.create_window(right_align, 160, window=sl)

ve = tk.Entry(root)
re = tk.Entry(root)
be = tk.Entry(root)
se = tk.Entry(root)

canvas1.create_window(left_align, 127, window=ve)
canvas1.create_window(right_align, 127, window=re)
canvas1.create_window(left_align, 187, window=be)
canvas1.create_window(right_align, 187, window=se)

num_shares_d = tk.Label(canvas1, text="Number of shares to buy")
canvas1.create_window(left_align, 300, window=num_shares_d)

pos_size_d = tk.Label(canvas1, text="Position size")
canvas1.create_window(right_align, 300, window=pos_size_d)

rps_d = tk.Label(canvas1, text="Risked per share")
canvas1.create_window(left_align, 400, window=rps_d)

rpos_d = tk.Label(canvas1, text="Risked position")
canvas1.create_window(right_align, 400, window=rpos_d)


def positionSize():
    value = ve.get()
    risk = re.get()
    buy = be.get()
    stop = se.get()

    dollarrisk = (float(value) / 100) * float(risk)
    difference = float(buy) - float(stop)

    num_shares = dollarrisk / difference
    pos_size = num_shares * float(buy)

    num_shares_a = tk.Label(canvas1, text=num_shares)
    canvas1.create_window(left_align, 330, window=num_shares_a)

    pos_size_a = tk.Label(canvas1, text=f"${pos_size}")
    canvas1.create_window(right_align, 330, window=pos_size_a)

    rps_a = tk.Label(canvas1, text=f"${difference}")
    canvas1.create_window(left_align, 430, window=rps_a)

    rpos_a = tk.Label(canvas1, text=f"${dollarrisk}")
    canvas1.create_window(right_align, 430, window=rpos_a)


c = tk.Button(text="Calculate", command=positionSize)
canvas1.create_window(left_align, 240, window=c)

root.mainloop()
