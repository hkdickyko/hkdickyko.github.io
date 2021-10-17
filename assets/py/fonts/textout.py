import framebuf
import gc
from uctypes import bytearray_at, addressof

class TextOut:
    
  def __init__(self, display, font, lineHeight, fgColor=0xffff, bgColor=0x0000, colormap=framebuf.RGB565):
    self.display = display
    self.font = font
    self.lineHeight = lineHeight
    self.fgColor = fgColor
    self.bgColor = bgColor
    self.colormap = colormap
    self.top = 0
    
  def rgb(self, r, g=0, b=0):
        try:
            r, g, b = r  # see if the first var is a tuple/list
        except TypeError:
            pass
        color = (r & 0xf8) << 8 | (g & 0xfc) << 3 | b >> 3 
        return (color<<8 & 0xFF00) + (color>>8 & 0x00FF)

  def setTop(self, top):
      self.top = top

  def setFont(self, font):
      self.font = font

  def setLineHeight(self, height):
    self.lineHeight = height

  def setFgColor(self, r, g, b):
    self.fgColor = self.rgb(r, g, b)
      
  def setBgColor(self, r, g, b):
    self.bgColor = self.rgb(r, g, b)

  def Text(self, text, w, h, top, color=0xffff):
    fbuf = framebuf.FrameBuffer(bytearray(w * h * 2), w, h, self.colormap)
    fbuf.text(text, 0, 0, color)
    self.display.blit_buffer(fbuf, 0, top, w, h)
    gc.collect()
    gc.mem_free()

  def drawText(self, string):
    lines = string.split('\n', 1)
    n = len(lines)
    for i in range(n):
        x = 0
        for char in lines[i]:    
            x = self._drawChar(char, x, i*self.lineHeight+self.top, self.font, self.fgColor, self.bgColor, self.colormap)    
          
  def _drawChar(self, char, x, y, font, fgColor, bgColor, colormap):
    glyph, char_height, char_width = font.get_ch(char)
    bufc = bytearray_at(addressof(glyph), len(glyph))
    bufx = bytearray(char_height*char_width*2)
    if font.hmap() :
        if font.reverse():
            fbi = framebuf.FrameBuffer(bufc, char_width, char_height, framebuf.MONO_HMSB)
        else:
            fbi = framebuf.FrameBuffer(bufc, char_width, char_height, framebuf.MONO_HLSB)
        fbo = framebuf.FrameBuffer(bufx, char_width, char_height, colormap)
        for i in range(char_width):  
            for j in range(char_height): 
                color = fbi.pixel(i, j)
                if color!=0:
                    fbo.pixel(i, j, fgColor)
                else:
                    fbo.pixel(i, j, bgColor)
    else:
        raise ValueError('Font must be horizontally mapped.')
    self.display.blit_buffer(fbo, x, y, char_width, char_height)
    gc.collect()
    gc.mem_free()
    return x+char_width
