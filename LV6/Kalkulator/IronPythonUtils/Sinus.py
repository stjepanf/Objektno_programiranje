import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import *
clr.AddReference('System.Drawing')
from System.Drawing import Size
import math

name = 'sinus'

def sinFunction(sender, e):
    frm = sender.Tag
    frm.textBox3.Text = str(math.sin(float(frm.textBox1.Text)))

def AddFunction(frm):
    operation = ToolStripMenuItem(Text='Sinus', Name='runSin', Size=Size(130, 25))
    operation.Tag = frm
    operation.Click += sinFunction
    frm.addedOperationsToolStripMenuItem.DropDownItems.Add(operation)
