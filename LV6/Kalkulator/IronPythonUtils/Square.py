import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import *
clr.AddReference('System.Drawing')
from System.Drawing import Size
import math

name = 'square'

def squareFunction(sender, e):
    frm = sender.Tag
    frm.textBox3.Text = str((float(frm.textBox1.Text)) * (float(frm.textBox1.Text)))

def AddFunction(frm):
    operation = ToolStripMenuItem(Text='Square', Name='runSquare', Size=Size(130, 25))
    operation.Tag = frm
    operation.Click += squareFunction
    frm.addedOperationsToolStripMenuItem.DropDownItems.Add(operation)
