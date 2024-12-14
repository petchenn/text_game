from TextAdventure import tk
from TextAdventure import TextAdventureGame

def this_operation(a):
    cur = 1
    res = 1
    if a <= 1000 and a >0 :
        while cur <= a:
            res *= cur
            cur +=2
    return res

if __name__ == "__main__":
    print(this_operation(6))
    root = tk.Tk()
    game = TextAdventureGame(root)
    root.geometry("960x720")
    root.mainloop()

