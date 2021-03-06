# Lab 16
# 70pt -  Add in movement buttons for up, down, left and right using WASD
# 80pt -  Make sure the player can't go out of bounds to the left, right or down.
# 90pt -  When you hit space, fire a missile straight up! 
#         Subtract from how many missiles you have left
# 100pt - Destroy the target if a missile hits it! 
# Hints: use drawpad.delete(enemy) in the collision detect function, which you can trigger
# from the key press event... maybe a loop to keep checking until the rocket goes out of bounds?
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
rocket1 = drawpad.create_rectangle(400,585,405,590)
player = drawpad.create_oval(390,580,410,600, fill="blue")
enemy = drawpad.create_rectangle(50,50,100,60, fill="red")
rocket1Fired = False

direction = 5


class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        self.button1 = Button(self.myContainer1)
	self.button1.configure(text="Up", background= "green")
	self.button1.grid(row=0,column=0)

	self.button2 = Button(self.myContainer1)
	self.button2.configure(text="down", background= "green")
	self.button2.grid(row=1,column=0)
		
	self.button3 = Button(self.myContainer1)
	self.button3.configure(text="right", background= "green")
	self.button3.grid(row=0,column=1)
		
	self.button4 = Button(self.myContainer1)
	self.button4.configure(text="left", background= "green")
	self.button4.grid(row=1,column=1)
		
		# "Bind" an action to the first button												
	self.button1.bind("<Button-1>", self.button1Click)
	self.button2.bind("<Button-1>", self.button2Click)
	self.button3.bind("<Button-1>", self.button3Click)
	self.button4.bind("<Button-1>", self.button4Click)

        
        # Enter my text
        self.prompt = "Rockets left :"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()

        self.rockets = 3
        
        self.rocketsTxt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='green')
        self.rocketsTxt.pack()
        
        self.rocketFired = False
        # Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    def animate(self):
        global drawpad
        global enemy
        global direction
        global rocket
        global rocket1Fired
        x1,y1,x2,y2 = drawpad.coords(enemy)
        px1,py1,px2,py2 = drawpad.coords(player)

        if x2 > 800:
            direction = - 5
        elif x1 < 0:
            direction = 5
        drawpad.move(enemy, direction, 0)
        drawpad.after(5,self.animate)

    def key(self,event):
        global player
        global rocket1Fired
        if event.char == "w":
            drawpad.move(player,0,-4)
            drawpad.move(rocket1,0,-4)
            
    
    def collisionDetect(self, rocket):
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket)
app = myApp(root)
root.mainloop()