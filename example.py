root = Tk()

i=0

def choice1():
    list1[a1].implement()
    list1.remove(list1[a1])

def choice2():
    list2[a2].implement()
    list2.remove(list2[a2])

while i==0:

 # put here, what this extra loop will do.#

button1 = tk.Button(root, text=list1.headline, command=choice1)
button2 = tk.Button(root, text=list2.headline, command =choice2)
root.mainloop()