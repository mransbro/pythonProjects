import tkinter as tk
import tkinter.font as tfont


def positionSize():
    value = float(acventry.get())
    risk = float(riskentry.get())
    buy = float(buyentry.get())
    stop = float(stopentry.get())

    dollar_risk = (value / 100) * risk
    difference = buy - stop

    num_shares = dollar_risk / difference
    pos_size = num_shares * buy

    num_shares_a = tk.Label(canvas1, text=round(num_shares, 2))
    canvas1.create_window(left_align, 330, window=num_shares_a)

    pos_size_a = tk.Label(canvas1, text=f"${round(pos_size, 2)}")
    canvas1.create_window(right_align, 330, window=pos_size_a)

    rps_a = tk.Label(canvas1, text=f"${round(difference, 2)}")
    canvas1.create_window(left_align, 430, window=rps_a)

    rpos_a = tk.Label(canvas1, text=f"${round(dollar_risk, 2)}")
    canvas1.create_window(right_align, 430, window=rpos_a)


root = tk.Tk()
left_align = 137
right_align = 413
heading_font = tfont.Font(size=36)
general_font = tfont.Font(size=14)
canvas1 = tk.Canvas(root, width=550, height=540)
canvas1.pack()

heading = tk.Label(canvas1, text="Position Size Calculator", font=heading_font)
canvas1.create_window(275, 45, window=heading)

acvlabel = tk.Label(canvas1, text="Account value", font=general_font)
canvas1.create_window(left_align, 100, window=acvlabel)
acventry = tk.Entry(root)
canvas1.create_window(left_align, 127, window=acventry)

risklabel = tk.Label(canvas1, text="Risk as percent of account", font=general_font)
canvas1.create_window(right_align, 100, window=risklabel)
riskentry = tk.Entry(root)
canvas1.create_window(right_align, 127, window=riskentry)

stoplabel = tk.Label(canvas1, text="Stop price", font=general_font)
canvas1.create_window(right_align, 160, window=stoplabel)
stopentry = tk.Entry(root)
canvas1.create_window(right_align, 187, window=stopentry)

buylabel = tk.Label(canvas1, text="Entry price", font=general_font)
canvas1.create_window(left_align, 160, window=buylabel)
buyentry = tk.Entry(root)
canvas1.create_window(left_align, 187, window=buyentry)

c = tk.Button(text="Calculate", width=18, command=positionSize)
canvas1.create_window(left_align, 240, window=c)

num_shares_d = tk.Label(canvas1, text="Number of shares to buy", font=general_font)
canvas1.create_window(left_align, 300, window=num_shares_d)
nsb = tk.Entry(root)
canvas1.create_window(left_align, 327, window=nsb)

pos_size_d = tk.Label(canvas1, text="Position size", font=general_font)
canvas1.create_window(right_align, 300, window=pos_size_d)
pos = tk.Entry(root)
canvas1.create_window(right_align, 327, window=pos)

rps_d = tk.Label(canvas1, text="Risked per share", font=general_font)
canvas1.create_window(left_align, 380, window=rps_d)
rps = tk.Entry(root)
canvas1.create_window(left_align, 407, window=rps)

rpos_d = tk.Label(canvas1, text="Risked position", font=general_font)
canvas1.create_window(right_align, 380, window=rpos_d)
rpos = tk.Entry(root)
canvas1.create_window(right_align, 407, window=rpos)


if __name__ == "__main__":
    root.mainloop()
