import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import *
clr.AddReference('System.Drawing')
from System.Drawing import Size
import math

name = 'sqRoot'

def sqRootFunction(sender, e):
    frm = sender.Tag
    frm.textBox3.Text = str(math.sqrt(float(frm.textBox1.Text)))

def AddFunction(frm):
    operation = ToolStripMenuItem(Text='SqRoot', Name='runSqRoot', Size=Size(130, 25))
    operation.Tag = frm
    operation.Click += sqRootFunction
    frm.addedOperationsToolStripMenuItem.DropDownItems.Add(operation)
