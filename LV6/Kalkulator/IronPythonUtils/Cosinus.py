import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import *
clr.AddReference('System.Drawing')
from System.Drawing import Size
import math

name = 'cosinus'

def cosFunction(sender, e):
    frm = sender.Tag
    frm.textBox3.Text = str(math.cos(float(frm.textBox1.Text)))

def AddFunction(frm):
    operation = ToolStripMenuItem(Text='Cosinus', Name='runCos', Size=Size(130, 25))
    operation.Tag = frm
    operation.Click += cosFunction
    frm.addedOperationsToolStripMenuItem.DropDownItems.Add(operation)
