# Theme: art of conciseness.
# Header comments
# individual features
'''
-I seted the environment, which locate the program on the top left of the computer screen.
-I set the captain.
-Individual incon and cursor.
-Has an intro screen.
-When users use mouse to select tools or press buttons, the tool will be highlighted.
-After users selected my drawing tools(all kinds of pens), the tool selected will move closer to the canvas to show it's being used.
-When users use mouse to select tools or press buttons, the tool will be highlighted.
-I have a size bar, exhibiting the current used size and color.
-To resize the tools, it can be done via rolling the mouse scroll, press left or right button, or just click on the size bar.
-My pencil can also change the size and color and perform as a brush.
-I have a chinese brush, a spray pen, a highlighter, and a mixed color pen.
-I have undo and redo.
-To save more screen surface for canvas, I stored color, stamps,and shapes at one area. User can switch the type of the tools by press the buttons.
-When user is graphing and they moved the mouse out of the canvas, it won't cause any trouble such as changing the color.
-To chose color professionally,I set up color surface.On the surface,a larger color palette is set for convenience. And 3 ramps with rgb color can be used to click to change colors.
    Technically, people can use it to make 255**3 colors. And the current used color is shown through the color bar on the surface.
-Also, there is testing pencil on the color surface.
-User can generate the canvas's color by clicking the canvas button on the color surface.
-I have 10 stamps with the anime themes. Their sizes are alterable.
-I have filled and unfilled polygon tool.
-I have filled and unfilled four-angle stars.
-I have clean canvas method.
-I have change-background method.
-I have a text tool for user to add text to the paint. The size is alterable.
-I have save and load. I use specific methods to ensure the unproper name won't crash the program.
-In setting screen, users can change the theme for black-white to colorful, or vice versa
-The program has 5 musics for user to choose.
-User can change the volume of the music freely via rolling the mouse scroll, press left or right button, or just click on the size bar. Pause/unpause button is provided, too.
-This program has screen timeout, which can remind user to work if the user rest for a period. The feature can be cancle by the button on the settings interface.
-I have live mirror graphing,containing three types of live mirror. Users can switch them by click the live mirror button on the setting interface.
-I have a flood fill tool.
'''
# attation to detail
'''
-when the program is being processed,the window is not just black screen.
-Can't accidently change color.
-My stamps are all from animes and with hight hd.
-My drawing tools(all kinds of pens) are all black colors with the same theme.
-My musics are relate to the theme.
-My bakgrounds are either pure balck and white, or pure color.
-When users use mouse to select tools or press buttons, the tool will be highlighted.
-After increasing the size of my pencil, it doesn't have any gap.
-I has 4 size variables which represent different types of tools' sizes respectively and neatly, poviding better graphing experience.
-When the color change to white, which is also size bar's background color, the background of the size bar will automatically become grey to enable the wite color can be shown.
-After people changed canvas's color, the canvas will automaticallly adapt to it.
-All the pictures of shapes are very concise. Also, the order is always filled shape on the top and unfilled at the bottom.
-Musics are all pure music, which fits the theme conciseness.
-On settings interface, if the object, such like music, theme and so on, is not being used, the picture of it would be dimmed.
-Remind users to add extentions when save or load files.
-If the user type the wrong name for save or load,the program will remind them.
-I fixed the unfilled rectangle's corners
-I fixed the gaps occured on the unfilled oval
'''

# imprort libraries.
from pygame import *
from math import *
from random import *
from glob import *
import os

# Here is to initializing the program set up the screen and frame.
init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = display.set_mode((1200, 800))
display.set_caption('Art of Conciseness')
display.set_icon(transform.scale(image.load("settings/icon.png"), (25, 25)))
screen.fill((224, 224, 224))
screen.blit(transform.scale(image.load("settings/icon.png"), (500, 500)),
            (350, 150))  # show icon while the program is being processed
display.update()

# music.
mixer.music.load("settings/sword.mp3")
mixer.music.play(-1)
volume = 0.9
mixer.music.set_volume(volume)
music = True  # It indicates if the music is playing

# Overall prepare
interface = 1  # interface flag.
out = 0  # a flag for screen timeout.
mouse.set_cursor(*cursors.broken_x)
mouse.set_visible(True)

# Load backgrounds
##Baclk-white backgrounds.
pic_1 = transform.scale(image.load("settings/pic_1.jpg"), (1200, 800))  # load and transform background pictures
pic_2 = transform.scale(image.load("settings/pic_2.jpg"), (1200, 800))
pic_3 = transform.scale(image.load("settings/pic_3.jpg"), (1200, 800))
pic_4 = transform.scale(image.load("settings/pic_4.jpg"), (1200, 800))
pic_5 = transform.scale(image.load("settings/pic_5.jpg"), (1200, 800))
pic_6 = transform.scale(image.load("settings/pic_6.jpg"), (1200, 800))
pic_7 = transform.scale(image.load("settings/pic_7.jpg"), (1200, 800))
pic_8 = transform.scale(image.load("settings/pic_8.jpg"), (1200, 800))
pic_9 = transform.scale(image.load("settings/pic_9.jpg"), (1200, 800))
pic_10 = transform.scale(image.load("settings/pic_10.jpg"), (1200, 800))
pic_lis1 = [pic_1, pic_2, pic_3, pic_4, pic_5, pic_6, pic_7, pic_8, pic_9, pic_10]
##colorful Background
pic_red = transform.scale(image.load("settings/redBack.jpg"),
                          (1200, 800))  # for those background pictures, I load and transform their sizes.
pic_green = transform.scale(image.load("settings/greenBack.jpg"), (1200, 800))
pic_orange = transform.scale(image.load("settings/orangeBack.jpg"), (1200, 800))
pic_pink = transform.scale(image.load("settings/pinkBack.jpg"), (1200, 800))
pic_purple = transform.scale(image.load("settings/purpleBack.jpg"), (1200, 800))
pic_white = transform.scale(image.load("settings/whiteBack.jpg"), (1200, 800))
pic_blue = transform.scale(image.load("settings/blueBack.jpg"), (1200, 800))
pic_yellow = transform.scale(image.load("settings/yellowBack.jpg"), (1200, 800))
pic_cyan = transform.scale(image.load("settings/cyanBack.jpg"), (1200, 800))
pic_flourescent = transform.scale(image.load("settings/flourescentBack.jpg"), (1200, 800))
pic_lis2 = [pic_red, pic_green, pic_orange, pic_pink, pic_purple, pic_white, pic_blue, pic_yellow, pic_cyan,
            pic_flourescent, pic_flourescent]
##use backgrouds
current_pic_lis = pic_lis1  # flag to switch background theme.
pic_numb = randint(0, 9)  # falg to switch background.

# interface0: drawing interface. It is the main interface for graphing.
# canvas,color
canvas = Rect(196, 50, 1000, 500)
canvasSet = 1  # canvas flag used to edit canvas
canvasCol = (255, 255, 255)  # used to change canvas color
frameR = Rect(192, 46, 1008, 508)  # canvas frame
drawCol = (0, 0, 0)
sizeBarR = Rect(132, 54, 16, 514)  # shows size of the presently used tool
# undo & redo
undoR = Rect(10, 50, 50, 50)
pic_undo = transform.scale(image.load("pictures/undo.png"), (47, 47))
can_list = []  # save the copied paintings for undo
redoR = Rect(60, 50, 50, 50)
pic_redo = transform.scale(image.load("pictures/redo.png"), (47, 47))
can_list2 = []  # save the copied paintings before undo, for redo
# tools
tool = False  # flag for indicate present used tool.
sz = 'sz1'  # represents present size.
# drawing tools,which are the pens and eraser.
sz1 = 1  # size for pens and eraser.
pencilR = Rect(0, 104, 100, 70)  # set button rectangles
pic_pencil = transform.scale(image.load("pictures/pencil.png"),
                             (97, 67))  # load and resize the pictures of drawing tools
chineseBrushR = Rect(0, 178, 100, 70)
pic_chineseBrush = transform.scale(image.load("pictures/brush.png"), (97, 67))
sprayR = Rect(0, 252, 100, 70)
pic_spray = transform.scale(image.load("pictures/spray.png"), (97, 67))
highlighterR = Rect(0, 326, 100, 70)
pic_highlighter = transform.scale(image.load("pictures/highlighter.png"), (97, 67))
mixedColpenR = Rect(0, 400, 100, 70)
pic_mixedColpen = transform.scale(image.load("pictures/mixedColpen.png"), (97, 67))
eraserR = Rect(0, 474, 100, 70)
pic_eraser = transform.scale(image.load("pictures/eraser.png"), (97, 67))


def use_pencil(mx, my, omx, omy, sz, col):
    '''this requires start,end positions,and color to draw pencil lines. Because the distance between two positions is a line, so this function draws circles on each point on the
    line to make a line with flexible sizes and colors. It can also be '''

    if mb[0] == 1:  # works when the left mouse button is pressing
        draw.circle(screen, drawCol, (mx, my), sz)  # draw a dot/circle when the mouse got pressed.
        h = hypot((mx - omx), (my - omy))  # the distance between two postions
        if h != 0:
            x = (mx - omx) / h  # find the ratio comparing to the distation
            y = (my - omy) / h
            for i in range(int(h)):
                draw.circle(screen, drawCol, (int(omx + x), int(omy + y)), sz)  # draw cilce at the point
                omx += x  # change the point's value
                omy += y


def use_chineseBrush(mx, my, omx, omy, sz, col):
    '''this requires start,end positionssize and color to draw Chinese brush lines. Because the distance between two positions is a line, so this function draws
    circles on each point on the line to make a line with flexible sizes and colors.As Chinese brush,its size changes as the speed of drawing changes'''

    if pressdown:  # draw a dot/circle when the mouse got pressed.
        draw.circle(screen, col, (mx, my), sz)
    if mb[0] == 1:
        h = hypot((mx - omx), (my - omy))  # the distance between two postions
        if h != 0:
            # the if/else statement changes the circle size based on the speed defined by the distance. The initial size influnces the size change.
            for r in range(2, 23, 2):  # this loop change the width of the line according to the speed of mouse moving
                if h / 5 < r:
                    if sz - r / 2 + 3 >= (sz + 2) / 2:
                        nsz = int(sz - r / 2 + 3)
                    else:
                        nsz = int((sz + 2) / 2)
                    break
            else:
                nsz = int((sz + 2) / 2)
            x = (mx - omx) / h  # find the ratio comparing to the distation
            y = (my - omy) / h
            for i in range(int(h)):
                draw.circle(screen, col, (int(omx + x), int(omy + y)), nsz)  # draw cilce at the point
                omx += x  # change the point's value
                omy += y


def use_spray(mx, my, omx, omy, sz, col):
    '''this requires start,end positions,and color to draw spray circles.Spray circles comprises lots of random circle in the particular ranges. The outer range will be sparser than the
    inner range.'''

    if mb[0] == 1:
        for n in range(16 + sz):  # change the drawing speed and range when size varies.
            a = randint(-sz - 5, sz + 5)  # randomly get values in the certain range
            b = randint(-sz - 5, sz + 5)
            if hypot(a, b) <= sz + 5:  # check if the value is out of te particular range.
                draw.circle(screen, col, (mx + a, my + b), 4)
            c = randint(-sz - 10, sz + 10)
            d = randint(-sz - 10, sz + 10)
            if hypot(c, d) <= sz + 10:
                draw.circle(screen, col, (mx + c, my + d), 3)
            e = randint(-sz - 15, sz + 15)
            f = randint(-sz - 15, sz + 15)
            if hypot(e, f) <= sz + 15:
                draw.circle(screen, col, (mx + e, my + f), 2)
            g = randint(-sz - 20, sz + 20)
            h = randint(-sz - 20, sz + 20)
            if hypot(g, h) <= sz + 20:
                draw.circle(screen, col, (mx + g, my + h), 1)


def use_highlighter(mx, my, omx, omy, sz, col):
    '''this requires start,end positions,and color to draw highlighter lines. Because the distance between two positions is a line, so this function blit translucent circles on
    each point on the line to make a line with flexible sizes and translucent colors.'''

    if mb[0] == 1:
        highlighterS = Surface((2 * sz, 2 * sz), SRCALPHA)  # creat a subsurface.
        draw.circle(highlighterS, (col[0], col[1], col[2], 21), (sz, sz), sz)  # add the color circle to the subsurface
        screen.blit(highlighterS, (mx, my))  # draw one circle when press the mouse
        h = hypot((mx - omx), (my - omy))
        if h != 0:
            x = (mx - omx) / h  # find the ratio comparing to the distation
            y = (my - omy) / h
            for i in range(int(h)):
                screen.blit(highlighterS, (int(omx + x), int(omy + y)))  # draw translucent cilce at the point
                omx += x  # change the point's value
                omy += y


col_list = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130),
            (139, 0, 255)]  # rainbow color prepared for mixed-color pen.


def use_mixedColpen(mx, my, omx, omy, sz, col_list):
    '''this requires start,end positions,size,and color list to draw mixed-color lines. Because the distance between two positions is a line, so this function draws circles on
    each point on the line to make a line with flexible sizes.Its color changes randomly while graphing.'''

    if mb[0] == 1:
        draw.circle(screen, col_list[randint(0, 6)], (mx, my), sz)  # draw one circle when press the mouse
        h = hypot((mx - omx), (my - omy))  # the distance between two postions
        if h != 0:
            x = (mx - omx) / h  # find the ratio comparing to the distation
            y = (my - omy) / h
            for i in range(int(h)):
                draw.circle(screen, col_list[randint(0, 6)], (int(omx + x), int(omy + y)),
                            sz)  # draw cilce at the point
                omx += x  # change the point's value
                omy += y


def use_eraser(mx, my, omx, omy, sz, canvasCol):
    '''this requires start,end positions,and color to draw eraser lines. Because the distance between two positions is a line, so this function draws circles on each point on the
    line to make a line with flexible sizes. Its color keeps to be the same as canvas color.'''

    if mb[0] == 1:
        draw.circle(screen, canvasCol, (mx, my), 19 + sz)  # draw one circle when press the mouse
        h = hypot((mx - omx), (my - omy))  # the distance between two postions
        if h != 0:
            x = (mx - omx) / h  # find the ratio comparing to the distation
            y = (my - omy) / h
            for i in range(int(h)):
                draw.circle(screen, canvasCol, (int(omx + x), int(omy + y)), 19 + sz)  # draw cilce at the point
                omx += x  # change the point's value
                omy += y


# specified tools: 3 catologues of tools, including selecting colors, stamps, and shapes
stool = 'colorTool'
# colors tools
mixedColR = Rect(10, 590, 80, 50)  # set button rectangles
pic_mixedCol = transform.scale(image.load("pictures/mixedCol.jpg"), (77, 47))  # load and transform pictures
paletteR = Rect(110, 590, 340, 170)
pic_palette = transform.scale(image.load("pictures/color_palette.png"), (340, 170))
moreR = Rect(480, 590, 200, 85)
pic_more = transform.scale(image.load("pictures/more_color.jpeg"), (200, 85))
flood_fillR = Rect(480, 675, 200, 85)
pic_flood_fill = transform.scale(image.load("pictures/flood_fill.png"), (200, 85))


def use_flood_fill(mx, my, drawCol):
    '''this requires mouse position,and color to do flood. It works by changing the pixels, that surround the clicked pixels with the same color.  pxarray[x, y]'''

    if one_press:
        drawCol = screen.map_rgb(drawCol)
        pxarray = PixelArray(screen)
        pixel_list = [(mx, my)]  # to find more pixels with the same color
        changeCol = pxarray[mx, my]  # get the color need to be changed
        if changeCol != drawCol:
            while len(pixel_list) > 0:  # ends when no more pixel need to add
                x, y = pixel_list.pop()
                if x < 196 or x > 1196 or y < 50 or y > 550 or pxarray[
                    x, y] == drawCol:  # prevents from affecting background and logic error
                    continue
                pxarray[x, y] = drawCol  # change the pixel's color
                if pxarray[x + 1, y] == changeCol and pxarray[
                    x + 1, y] != drawCol:  # find the pixels nearby the oringinal pixel with the color need to be changed.
                    pixel_list.append((x + 1, y))
                if pxarray[x - 1, y] == changeCol and pxarray[x - 1, y] != drawCol:
                    pixel_list.append((x - 1, y))
                if pxarray[x, y + 1] == changeCol and pxarray[x, y + 1] != drawCol:
                    pixel_list.append((x, y + 1))
                if pxarray[x, y - 1] == changeCol and pxarray[x, y - 1] != drawCol:
                    pixel_list.append((x, y - 1))


# stamp tools
sz2 = 1
stamp0R = Rect(10, 650, 80, 50)  # set button rectangles
pic_stamp0 = transform.scale(image.load("stamp/stamp0.gif"), (77, 47))
stamp1R = Rect(120, 600, 100, 70)
spic_stamp1 = image.load("stamp/stamp1.png")  # load stamp pictures
stamp2R = Rect(120, 680, 100, 70)
spic_stamp2 = image.load("stamp/stamp2.png")
stamp3R = Rect(240, 600, 100, 70)
spic_stamp3 = image.load("stamp/stamp3.png")
stamp4R = Rect(240, 680, 100, 70)
spic_stamp4 = image.load("stamp/stamp4.png")
stamp5R = Rect(360, 600, 100, 70)
spic_stamp5 = image.load("stamp/stamp5.png")
stamp6R = Rect(360, 680, 100, 70)
spic_stamp6 = image.load("stamp/stamp6.png")
stamp7R = Rect(480, 600, 100, 70)
spic_stamp7 = image.load("stamp/stamp7.png")
stamp8R = Rect(480, 680, 100, 70)
spic_stamp8 = image.load("stamp/stamp8.png")
stamp9R = Rect(600, 600, 100, 70)
spic_stamp9 = image.load("stamp/stamp9.png")
stamp10R = Rect(600, 680, 100, 70)
spic_stamp10 = image.load("stamp/stamp10.png")
stamp = spic_stamp1  # a flage for switch different stamps to blit.


def use_stamp(mx, my, stamp, sz):
    '''this requires press position, stamp picture and size to blit the stamps'''

    if mb[0] == 1:
        screen.blit(screen_cop, (0, 0))  # if the the user didn't lift the mouse button the graph won't be drawn.
        s = 90 + int(sz * 20)  # renew the size of the stamps
        screen.blit(transform.scale(stamp, (s, s)), (mx - int(s / 2), my - int(s / 2)))


# shape tools
sz3 = 1  # size for shape tools
shapeR = Rect(10, 710, 80, 50)  # set button rectangles
pic_shape = transform.scale(image.load("pictures/shapes.jpg"), (77, 47))  # load and transform shape pictures.
line_fR = Rect(120, 600, 100, 70)
pic_lineF = transform.scale(image.load("pictures/line_filled.png"), (97, 67))
line_uR = Rect(120, 680, 100, 70)
pic_lineU = transform.scale(image.load("pictures/dashline.png"), (97, 67))
rectangelFR = Rect(240, 600, 100, 70)
pic_rectF = transform.scale(image.load("pictures/rectF.png"), (97, 67))
rectangelUR = Rect(240, 680, 100, 70)
pic_rectU = transform.scale(image.load("pictures/rectU.png"), (97, 67))
oval_fR = Rect(360, 600, 100, 70)
pic_ovalF = transform.scale(image.load("pictures/ovalF.jpg"), (97, 67))
oval_uR = Rect(360, 680, 100, 70)
pic_ovalU = transform.scale(image.load("pictures/ovalU.png"), (97, 67))
polygonFR = Rect(480, 600, 100, 70)
pic_polygonF = transform.scale(image.load("pictures/polygonF.png"), (97, 67))
polygonUR = Rect(480, 680, 100, 70)
pic_polygonU = transform.scale(image.load("pictures/polygonU.png"), (97, 67))
starFR = Rect(600, 600, 100, 70)
pic_starF = transform.scale(image.load("pictures/starF.png"), (97, 67))
starUR = Rect(600, 680, 100, 70)
pic_starU = transform.scale(image.load("pictures/starU.gif"), (97, 67))


def use_lineF(start, mx, my, drawCol, sz):
    '''this requires start,end positions,color and size to draw straight line'''

    if mb[0] == 1:
        screen.blit(screen_cop, (0, 0))  # if the the user didn't lift the mouse button the graph won't be drawn.
        draw.line(screen, drawCol, start, (mx, my), sz)


def use_lineU(start, mx, my, drawCol, sz):
    '''this requires start,end positions,color and size to draw dash line'''

    if mb[0] == 1:
        screen.blit(screen_cop, (0, 0))  # if the the user didn't lift the mouse button the graph won't be drawn.
        lmx, lmy = start
        h = hypot((mx - lmx), (my - lmy)) / 2  # the distance between two postions
        if h != 0:
            x = (mx - lmx) / h  # find the ratio comparing to the distation
            y = (my - lmy) / h
            for i in range(int(h / 4)):
                draw.line(screen, drawCol, (int(lmx), int(lmy)), (int(lmx + 2 * x), int(lmy + 2 * y)), sz)
                lmx += 4 * x  # change the point's value
                lmy += 4 * y


def use_rect(filled, start, mx, my, drawCol, sz):
    '''this requires start,end positions,color and size to draw rectangle.Variable "filled" is to determine if the shape is filled or not'''

    if mb[0] == 1:
        screen.blit(screen_cop, (0, 0))  # if the the user didn't lift the mouse button the graph won't be drawn.
        lmx, lmy = start
        if mx < lmx:  # to ensure the end position's value is larger than start position's.
            x1 = mx
            mx = lmx
            lmx = x1
        if my < lmy:
            y1 = my
            my = lmy
            lmy = y1
        if filled:  # if/else statement determine if the shape has size value value restriction
            draw.rect(screen, drawCol, (lmx, lmy, mx - lmx, my - lmy))
        else:
            draw.rect(screen, drawCol, (lmx, lmy, mx - lmx, my - lmy), sz)
            draw.rect(screen, drawCol, (int(lmx - sz / 2 + 1), int(lmy - sz / 2 + 1), sz, sz))  # fix the cornors
            draw.rect(screen, drawCol, (int(lmx - sz / 2 + 1), int(my - sz / 2), sz, sz))
            draw.rect(screen, drawCol, (int(mx - sz / 2), int(lmy - sz / 2 + 1), sz, sz))
            draw.rect(screen, drawCol, (int(mx - sz / 2), int(my - sz / 2), sz, sz))


def use_oval(filled, start, mx, my, drawCol, sz):
    '''this requires start,end positions,color and size to draw oval.Variable "filled" is to determine if the shape is filled or not.'''

    if mb[0] == 1:
        screen.blit(screen_cop, (0, 0))  # if the the user didn't lift the mouse button the graph won't be drawn.
        lmx, lmy = start
        if mx < lmx:  # to ensure the end position's value is larger than start position's so that value error won't occur
            x1 = mx
            mx = lmx
            lmx = x1
        if my < lmy:
            y1 = my
            my = lmy
            lmy = y1
        if filled:  # if/else statement determine if the shape has size value value restriction
            if mx - lmx >= 4 and abs(my - lmy) >= 4:  # ensure the code won't crash
                draw.ellipse(screen, drawCol, (lmx, lmy, mx - lmx, my - lmy))
        else:
            if mx - lmx - 2 * sz >= 4 and my - lmy - 2 * sz >= 4 and mx - lmx > sz * 2 and my - lmy > sz * 2:
                r = drawCol[0]  # unpack colors
                g = drawCol[1]
                b = drawCol[2]
                fixgap = Surface((mx - lmx, my - lmy),
                                 SRCALPHA)  # use subsurface to draw the circle so that there is no gap on the unfilled circle
                draw.ellipse(fixgap, (r, g, b, 255), (0, 0, mx - lmx, my - lmy))
                draw.ellipse(fixgap, (r, g, b, 0), (sz, sz, mx - lmx - 2 * sz, my - lmy - 2 * sz))
                screen.blit(fixgap, (lmx, lmy))


polygonlist = []


def use_polygon(filled, mx, my, polygonlist, drawCol, sz, press1, press2):
    '''this requires mouse position,color,size left/right MOUSEBUTTONUP event to draw polygon.Variable "filled" is to determine if the shape is filled or not.The polygon is drawn by use
    left mouse button to select polygon's point and right button to draw the final polygon.'''

    if press1:  # left mouse button to select points
        screen.set_at((mx, my), drawCol)  # exhibites this point is selected
        polygonlist.append((mx, my))
        if len(polygonlist) > 1:
            draw.line(screen, drawCol, polygonlist[len(polygonlist) - 2], polygonlist[len(polygonlist) - 1],
                      sz)  # indicate a line of the polygon is difined
    if press2:  # right mouse button to draw the polygon.
        if len(polygonlist) > 2:  # ensure enought points to draw a polygon
            if filled == True:  # if/else statement determine if the shape has size value restriction
                draw.polygon(screen, drawCol, polygonlist)
            else:
                draw.polygon(screen, drawCol, polygonlist, sz)


def use_star(filled, mx, my, start, drawCol, sz):
    '''this requires mouse position,color and size to draw stars.Variable "filled" is to determine if the shape is filled or not'''

    if mb[0] == 1:
        screen.blit(screen_cop, (0, 0))  # if the the user didn't lift the mouse button the graph won't be drawn.
        x, y = start
        if mx < x:  # to ensure the end position's value is larger than start position's so that value error won't occur
            x1 = mx
            mx = x
            x = x1
        if my < y:
            y1 = my
            my = y
            y = y1
        hx = mx - x  # find position values's difference.
        hy = my - y
        if hx >= 10 and hy >= 10:
            if filled:  # if/else statement determine if the shape has size value restriction
                draw.polygon(screen, drawCol, (
                (x + int(hx / 2), y), (x + int(hx / 5 * 3), y + int(hy / 5 * 2)), (mx, y + int(hy / 2)),
                (x + int(hx / 5 * 3), y + int(hy / 5 * 3)), (x + int(hx / 2), my),
                (x + int(hx / 5 * 2), y + int(hy / 5 * 3)), (x, y + int(hy / 2)),
                (x + int(hx / 5 * 2), y + int(hy / 5 * 2))))
            else:
                draw.polygon(screen, drawCol, (
                (x + int(hx / 2), y), (x + int(hx / 5 * 3), y + int(hy / 5 * 2)), (mx, y + int(hy / 2)),
                (x + int(hx / 5 * 3), y + int(hy / 5 * 3)), (x + int(hx / 2), my),
                (x + int(hx / 5 * 2), y + int(hy / 5 * 3)), (x, y + int(hy / 2)),
                (x + int(hx / 5 * 2), y + int(hy / 5 * 2))), sz)


# other features including cleaning canvas, changing background, writing text, settings, saving image, and loading image.
cleanR = Rect(840, 600, 100, 70)  # set button rectangles
pic_clean = transform.scale(image.load("pictures/clean.jpeg"), (97, 67))  # load and resize the pictures of buttons
change_backgroundR = Rect(840, 680, 100, 70)
pic_change_background = transform.scale(image.load("pictures/change_background.jpg"), (97, 67))
nslide = 0  # a flag used to change background for this interface 0
textR = Rect(960, 600, 100, 70)
pic_text = transform.scale(image.load("pictures/text.png"), (97, 67))
settingsR = Rect(960, 680, 100, 70)
pic_settings = transform.scale(image.load("pictures/settings.png"), (97, 67))
saveR = Rect(1080, 600, 100, 70)
pic_save = transform.scale(image.load("pictures/save.png"), (97, 67))
pic_saveBack = transform.scale(image.load("pictures/save_asknameBack.jpg"), (300, 30))
loadR = Rect(1080, 680, 100, 70)
pic_load = transform.scale(image.load("pictures/load.png"), (97, 67))
pic_loadBack = transform.scale(image.load("pictures/load_asknameBack.jpeg"), (300, 30))
##get name function is used for get text from the user so that the program can load, save, or blit text,
sz4 = 1  # size for texts
font.init()


def getName(screen, showFiles, sz):
    '''this is created by Mr.McKenzie.I add size varieble so that users can change the size of text while typing.I also changed some colors and add a reminder'''

    ans = ""
    arialFont = font.SysFont("Times New Roman", 21 + sz)  # change size of the text
    back = screen.copy()
    textArea = Rect(296, 300, 800, 30 + sz)  # change size of the text area

    if showFiles:
        draw.rect(screen, (0, 255, 0), (296, 270, 800, 30))
        draw.rect(screen, (0, 0, 255), (296, 270, 800, 30), 2)
        comicFont = font.SysFont("Comic Sans MS", 28)
        txtPic = comicFont.render("Press enter to continue(don't forget adding extentions!)", True,
                                  (255, 0, 0))  # add reminder
        screen.blit(txtPic, (297, 266))
        pics = glob("*.bmp") + glob("*.jpg") + glob("*.png")
        n = len(pics)
        choiceArea = Rect(textArea.x, textArea.y + textArea.height, textArea.width, n * textArea.height)
        draw.rect(screen, (153, 0, 76), choiceArea)
        draw.rect(screen, (0, 0, 0), choiceArea, 1)
        for i in range(n):
            txtPic = arialFont.render(pics[i], True, (229, 255, 204))
            screen.blit(txtPic, (textArea.x + 3, textArea.height * i + choiceArea.y))
    cursorShow = 0
    myclock = time.Clock()
    typing = True
    while typing:
        cursorShow += 1
        for e in event.get():
            if e.type == QUIT:
                event.post(e)
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:
                    if len(ans) > 0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN:
                    typing = False
                elif e.key < 256:
                    ans += e.unicode

        txtPic = arialFont.render(ans, True, (0, 0, 0))
        draw.rect(screen, (220, 255, 220), textArea)
        draw.rect(screen, (0, 0, 0), textArea, 2)
        screen.blit(txtPic, (textArea.x + 3, textArea.y + 2))
        if cursorShow // 50 % 2 == 1:
            cx = textArea.x + txtPic.get_width() + 3
            cy = textArea.y + 3
            draw.rect(screen, (255, 0, 0), (cx, cy, 2, textArea.height - 6))
        myclock.tick(100)
        display.flip()

    screen.blit(back, (0, 0))
    return ans


def use_text(mx, my, sz, col):
    '''this requires mouse position,size and color to add text into the graph. '''

    if one_press:
        comicFont = font.SysFont("Comic Sans MS", 20 + sz)  # setup the font
        txt = getName(screen, False, sz)
        if txt != '':
            txtPic = comicFont.render(txt, True, col)  # convert the text to a picture
            screen.blit(txtPic, (mx - int(txtPic.get_width() / 2), my - int(
                txtPic.get_height() / 2)))  # with the mouse button as the center, blit the picture.


# interface1: intro screen
virtuoso = transform.scale(image.load("pictures/virtuoso.png"),
                           (1200, 800))  # load and transform the picture for intro screen's background
pic_welcome = transform.scale(image.load("pictures/WelcomeTo.gif"),
                              (400, 100))  # load and transform the pictures for title
pic_name1 = transform.scale(image.load("pictures/name1.png"), (300, 100))
pic_name2 = transform.scale(image.load("pictures/name2.png"), (300, 100))
go_to_drawR = Rect(850, 550, 200, 200)  # set button rectangles
go_to_draw = transform.scale(image.load("pictures/go_to_draw.png"),
                             (197, 197))  # load and transform the pictures for buttons
settings2R = Rect(150, 550, 200, 200)
pic_settings2 = transform.scale(image.load("pictures/settings.png"), (197, 197))

# interface2: time out screen
slideshow = 0  # is used to determine when it's the time to change the background picture
nslide2 = 0  # a flag used to change background of this infterface 2.
interface2end = False
useTimeOut = True  # is used to block/unlock screen timeout

# interface3: color screen
pic_paletteBack = transform.scale(image.load("pictures/paletteBack.jpg"), (1200, 800))
palette2R = Rect(50, 50, 500, 400)  # set color palette rectangle
pic_palette2 = transform.scale(image.load("pictures/color_palette.png"), (497, 397))
redSection = Rect(50, 500, 500, 50)  # set rectangles for user to press on the sections to edit colors.
greenSection = Rect(50, 575, 500, 50)
blueSection = Rect(50, 650, 500, 50)
pic_wood = transform.scale(image.load("pictures/wood.jpg"),
                           (20, 60))  # a picture shows where the user colicked on the color section.
colorBarR = Rect(650, 50, 500, 100)  # a rectangle shows color.
testingCanvasR = Rect(650, 200, 500, 300)
testingCanvasBack = False  # make sure testing canvas works
testingPencilandCleanR = Rect(660, 550, 150, 150)  # set button rectangles
pic_testingPencil = transform.scale(image.load("pictures/pencil.png"),
                                    (147, 147))  # load and transform the pictures for buttons
pic_testingClean = transform.scale(image.load("pictures/clean.jpeg"), (147, 147))
testingPencilANDclean_switch = 1  # for switching between the tesing pencil and clean
canvasColR = Rect(820, 550, 150, 150)  # set button rectangles
pic_canvasCol = transform.scale(image.load("pictures/canvasCol.png"),
                                (147, 147))  # load and transform the pictures for buttons
go_to_draw2R = Rect(980, 550, 150, 150)
go_to_draw2 = transform.scale(image.load("pictures/go_to_draw.png"), (147, 147))

# interface4: settings screen
pic_settingsBack = transform.scale(image.load("pictures/settingsBack.jpg"),
                                   (1200, 800))  # load and transform background picture.
theme1R = Rect(100, 100, 1000, 70)  # set button rectangles
theme2R = Rect(100, 180, 1000, 70)
musicSwordR = Rect(100, 300, 200, 200)
pic_sword = transform.scale(image.load("settings/sword.jpg"), (197, 197))  # load and transform the pictures for buttons
musicPianoR = Rect(300, 300, 200, 200)
pic_piano = transform.scale(image.load("settings/piano.jpg"), (197, 197))
musicViolinR = Rect(500, 300, 200, 200)
pic_violin = transform.scale(image.load("settings/violin.jpg"), (197, 197))
musicBambooFluteR = Rect(700, 300, 200, 200)
pic_BambooFlute = transform.scale(image.load("settings/bambooFlute.jpeg"), (197, 197))
musicErhuR = Rect(900, 300, 200, 200)
pic_Erhu = transform.scale(image.load("settings/ErHu.jpg"), (197, 197))
currentMusic = 'sword'  # a flag to determine which music
volumeButtonR = Rect(250, 510, 80, 80)
pic_volumeButtonPa = transform.scale(image.load("settings/pause.png"), (77, 77))
pic_volumeButtonPl = transform.scale(image.load("settings/play.png"), (77, 77))
volumeBarR = Rect(350, 540, 600, 20)
timeOutR = Rect(100, 650, 200, 100)
pic_timeOut1 = transform.scale(image.load("settings/timeOutY.png"), (197, 97))
pic_timeOut2 = transform.scale(image.load("settings/timeOutN.png"), (197, 97))
live_mirrorR = Rect(500, 650, 200, 100)
pic_live_mirror1 = transform.scale(image.load("settings/live_mirror.jpg"), (197, 97))
pic_live_mirror2 = transform.scale(transform.rotate(image.load("settings/live_mirror.jpg"), 90),
                                   (197, 97))  # rotate the picture to make it represent up/down mirror
pic_live_mirror3 = transform.scale(image.load("settings/live_mirror2.jpg"), (197, 97))
live_mirror = 0  # flag for enable,disable and switch live mirror
go_to_draw3R = Rect(900, 650, 200, 100)
go_to_draw3 = transform.scale(image.load("pictures/go_to_draw.png"), (197, 97))


def use_mirror(live_mirror, mx, my, omx, omy, sz, drawCol, tool):
    '''this requires type of mirror,start/end positions,color,size and tool type to do live mirro graphing.It consists of three types of live mirror.It only works for drawing tools.'''

    if live_mirror == 1:
        sx = 1196 - mx + 196  # convert x values to make it left/right mirror.
        osx = 1196 - omx + 196
        tool(sx, my, osx, omy, sz, drawCol)  # draw with opposite x value
    elif live_mirror == 2:
        sy = 550 - my + 50  # convert y values to make it up/down mirror.
        osy = 550 - omy + 50
        tool(mx, sy, omx, osy, sz, drawCol)  # draw with opposite y value
    elif live_mirror == 3:
        sx = 1196 - mx + 196  # convert both x and y values to make it opposite mirror.
        osx = 1196 - omx + 196
        sy = 550 - my + 50
        osy = 550 - omy + 50
        tool(sx, sy, osx, osy, sz, drawCol)  # draw with opposite x,y values


# use loop to run the program
running = True
while running:
    one_press = False  # press values only work once when the relevant event happens once
    right_press = False
    pressdown = False
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            out = 0  # stop the counting for screen time out
            pressdown = True
            screen_cop = screen.copy()  # copy the screen for some particular graphing
            if e.button == 1:
                start = e.pos
                if canvas.collidepoint(
                        mouse.get_pos()) and interface == 0 and tool != True and tool != 'undo' and tool != 'redo':  # this guarantees user drawed something on the canvas.
                    if len(can_list) < 31:  # this if/else statement adds copied canvas to the undo list.
                        can_list.append(screen.subsurface(canvas).copy())
                    else:
                        del can_list[0]
                        can_list.append(screen.subsurface(canvas).copy())
            # Users can use the mouse scroll-wheel to resize the tool being used.
            if e.button == 4:
                if sz == 'sz1' and sz1 < 20:
                    sz1 += 1
                elif sz == 'sz2' and sz2 < 20:
                    sz2 += 1
                elif sz == 'sz3' and sz3 < 20:
                    sz3 += 1
                elif sz == 'sz4' and sz4 < 20:
                    sz4 += 1
                if interface == 4 and volume < 1.0:  # in interface 4(settings), mouse scroll-wheel changes volume
                    volume += 0.1
                    mixer.music.set_volume(volume)
            elif e.button == 5:
                if sz == 'sz1' and sz1 > 1:
                    sz1 -= 1
                elif sz == 'sz2' and sz2 > 1:
                    sz2 -= 1
                elif sz == 'sz3' and sz3 > 1:
                    sz3 -= 1
                elif sz == 'sz4' and sz4 > 1:
                    sz4 -= 1
                if interface == 4 and volume > 0.1:
                    volume -= 0.1
                    mixer.music.set_volume(volume)
        if e.type == MOUSEBUTTONUP:
            if e.button == 1:
                one_press = True  # works after click mouse button. It works for pressing buttons, selecting color and etc.
            if e.button == 3:
                right_press = True
        if e.type == KEYDOWN:
            interface2end = True
            out = 0
            # Users can use the left and right key to to resize the tool being used.
            if e.key == K_RIGHT:
                if sz == 'sz1' and sz1 < 20:
                    sz1 += 1
                elif sz == 'sz2' and sz2 < 20:
                    sz2 += 1
                elif sz == 'sz3' and sz3 < 20:
                    sz3 += 1
                elif sz == 'sz4' and sz4 < 20:
                    sz4 += 1
                if interface == 4 and volume < 1.0:  # in interface 4(settings), left and right key changes volume
                    volume += 0.1
                    mixer.music.set_volume(volume)
            if e.key == K_LEFT:
                if sz == 'sz1' and sz1 > 1:
                    sz1 -= 1
                elif sz == 'sz2' and sz2 > 1:
                    sz2 -= 1
                elif sz == 'sz3' and sz3 > 1:
                    sz3 -= 1
                elif sz == 'sz4' and sz4 > 1:
                    sz4 -= 1
                if interface == 4 and volume > 0.1:
                    volume -= 0.1
                    mixer.music.set_volume(volume)

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    # interfaces. They works respectively to give more features to users.
    if interface == 0:
        # set up background
        screen.blit(current_pic_lis[pic_numb + nslide], (0, 0))

        # set up the canvas
        draw.rect(screen, (224, 224, 224), frameR)
        if canvasSet == 0:
            screen.blit(can1, (196, 50))  # blit the saved canvas picture since we graphed something on the blink canvas
        elif canvasSet == 2:
            screen.blit(can1, (196, 50))
            for x in range(196, 1197):  # change canvas's color
                for y in range(50, 551):
                    pixelCol = screen.get_at((x, y))
                    if pixelCol == lastCanCol:
                        screen.set_at((x, y), canvasCol)
        else:
            draw.rect(screen, canvasCol, canvas)  # draw the blink canvas

        # frame of undo, redo, and drawing tools.
        draw.rect(screen, (224, 224, 224), (0, 48, 120, 500))
        draw.rect(screen, (212, 175, 55), (0, 48, 120, 500), 2)
        for x in range(102, 475, 74):
            draw.line(screen, (212, 175, 55), (0, x), (120, x))

        # undo & redo
        screen.blit(pic_undo, (12, 52))  # set out button pictures
        screen.blit(pic_redo, (62, 52))
        if undoR.collidepoint(mx, my):
            draw.rect(screen, 0, undoR, 2)
            if one_press:
                if tool != 'undo':  # clean redo list as starting a new serious of undo
                    can_list2 = []
                tool = 'undo'
                if len(can_list) > 0:
                    if len(can_list2) < 31:  # this if/else statement adds copied canvas to the redo list.
                        can_list2.append(screen.subsurface(canvas).copy())
                    else:
                        del can_list2[0]
                        can_list2.append(screen.subsurface(canvas).copy())
                    screen.blit(can_list.pop(), (196, 50))  # undo the current action by blitting last screen copy
        if redoR.collidepoint(mx, my):  # need to make redo list = [] when we draw any thing.
            draw.rect(screen, 0, redoR, 2)
            if one_press and len(can_list2) > 0 and tool == "undo":  # ensure it only work right after undo
                if len(can_list) < 31:  # this if/else statement adds copied canvas to the undo list.
                    can_list.append(screen.subsurface(canvas).copy())
                else:
                    del can_list[0]
                    can_list.append(screen.subsurface(canvas).copy())
                screen.blit(can_list2.pop(), (196, 50))  # redo action by blitting last screen copy before undo

        # Proving tools
        if tool != "pencil":  # pens' picture will be blit rightwards if they are being used
            screen.blit(pic_pencil, (2, 104))  # set out button pictures
        else:
            screen.blit(pic_pencil, (22, 104))  # set out button pictures rightwards
        if tool != "chineseBrush":
            screen.blit(pic_chineseBrush, (2, 178))
        else:
            screen.blit(pic_chineseBrush, (22, 178))
        if tool != "spray":
            screen.blit(pic_spray, (2, 252))
        else:
            screen.blit(pic_spray, (22, 252))
        if tool != "highlighter":
            screen.blit(pic_highlighter, (2, 326))
        else:
            screen.blit(pic_highlighter, (22, 326))
        if tool != "mixedColpen":
            screen.blit(pic_mixedColpen, (2, 400))
        else:
            screen.blit(pic_mixedColpen, (22, 400))
        if tool != "eraser":
            screen.blit(pic_eraser, (2, 476))
        else:
            screen.blit(pic_eraser, (22, 476))

        if pencilR.collidepoint(mx,
                                my) and one_press:  # this is for selecting tools. size variable also changes if the type of the tools changes
            tool = 'pencil'
            sz = 'sz1'
        elif chineseBrushR.collidepoint(mx, my) and one_press:
            tool = 'chineseBrush'
            sz = 'sz1'
        elif sprayR.collidepoint(mx, my) and one_press:
            tool = 'spray'
            sz = 'sz1'
        elif highlighterR.collidepoint(mx, my) and one_press:
            tool = 'highlighter'
            sz = 'sz1'
        elif mixedColpenR.collidepoint(mx, my) and one_press:
            tool = 'mixedColpen'
            sz = 'sz1'
        elif eraserR.collidepoint(mx, my) and one_press:
            tool = 'eraser'
            sz = 'sz1'

        # sizeBar. User can roll the mouse, click on left/right, or press on the bar to resize it. It also shows the currently used color
        comicFont = font.SysFont("Comic Sans MS", 30)
        rightPic = comicFont.render('->', True, (255, 0, 0))  # instructs users about whih buttons they should click
        leftPic = comicFont.render('<-', True, (255, 0, 0))
        screen.blit(rightPic, (130, 20))  # set out button pictures
        screen.blit(leftPic, (130, 530))

        draw.rect(screen, (212, 175, 55), (130, 51, 20, 498))
        if drawCol != (255, 255, 255):
            draw.rect(screen, (255, 255, 255), (132, 53, 16, 494))
        else:
            draw.rect(screen, (221, 221, 221), (132, 53, 16, 494))

        if sz == 'sz1':
            draw.rect(screen, drawCol, (133, 514 - 23 * sz1, 14, 32 + 23 * sz1))  # the color is current used color
        elif sz == 'sz2':
            draw.rect(screen, drawCol, (133, 514 - 23 * sz2, 14, 32 + 23 * sz2))
        elif sz == 'sz3':
            draw.rect(screen, drawCol, (133, 514 - 23 * sz3, 14, 32 + 23 * sz3))
        elif sz == 'sz4':
            draw.rect(screen, drawCol, (133, 514 - 23 * sz4, 14, 32 + 23 * sz4))

        if sizeBarR.collidepoint(mx, my) and sizeBarR.collidepoint(start) and mb[
            0] == 1 and my < 503:  # Change the current size by click on the size bar
            if sz == 'sz1':
                sz1 = 1 + int((503 - my) / 23)
            elif sz == 'sz2':
                sz2 = 1 + int((503 - my) / 23)
            elif sz == 'sz3':
                sz3 = 1 + int((503 - my) / 23)
            elif sz == 'sz4':
                sz4 = 1 + int((503 - my) / 23)

        # frame of specified tools inluding color tools, stamp tools, and shape tools
        draw.rect(screen, (224, 224, 224), (0, 585, 700, 180))
        draw.rect(screen, (212, 175, 55), (0, 585, 700, 180), 2)
        draw.line(screen, (212, 175, 55), (0, 645), (100, 645), 2)
        draw.line(screen, (212, 175, 55), (0, 705), (100, 705), 2)
        draw.line(screen, (212, 175, 55), (100, 585), (100, 765), 2)

        # selecting a type of specified tools inluding color tools, stamp tools, and shape tools
        screen.blit(pic_mixedCol, (12, 592))  # set out button pictures
        screen.blit(pic_stamp0, (12, 652))
        screen.blit(pic_shape, (12, 712))
        if mixedColR.collidepoint(mx, my):
            draw.rect(screen, 0, mixedColR, 2)  # highlight button
            if one_press:
                stool = 'colorTool'
        elif stamp0R.collidepoint(mx, my):
            draw.rect(screen, 0, stamp0R, 2)
            if one_press:
                stool = 'stampTool'
        elif shapeR.collidepoint(mx, my):
            draw.rect(screen, 0, shapeR, 2)
            if one_press:
                stool = 'shapeTool'

        # special tools work respectively as are sorted by if/else statement.
        # Color-choosing tool
        if stool == 'colorTool':
            draw.line(screen, (224, 224, 224), (100, 587), (100, 644),
                      2)  # to show the present special tools are color-choosing tools
            screen.blit(pic_palette, (112, 592))  # set out button pictures
            screen.blit(pic_more, (480, 590))
            screen.blit(pic_flood_fill, (480, 675))
            if paletteR.collidepoint(mx, my):
                draw.rect(screen, 0, paletteR, 2)  # highlight button
                if one_press:
                    drawCol = screen.get_at((mx, my))  # get the drawing color
            elif moreR.collidepoint(mx, my):
                draw.rect(screen, 0, moreR, 2)
                if one_press:
                    interface = 3  # open interface 3--color interface to do more with color
                    testingANDclean_switch = 1  # use testing pencil
                    testingCanvasBack = False  # clean the testing convas on color interface
            elif flood_fillR.collidepoint(mx, my):
                draw.rect(screen, 0, flood_fillR, 2)
                if one_press:
                    tool = 'flood fill'

        # stamp tools
        elif stool == 'stampTool':
            draw.line(screen, (224, 224, 224), (100, 646), (100, 704),
                      2)  # to show the present special tools are color-choosing tools
            screen.blit(transform.scale(spic_stamp1, (97, 67)),
                        (122, 602))  # resize stamps and then set out them as button pictures
            screen.blit(transform.scale(spic_stamp2, (97, 67)), (122, 682))
            screen.blit(transform.scale(spic_stamp3, (97, 67)), (242, 602))
            screen.blit(transform.scale(spic_stamp4, (97, 67)), (242, 682))
            screen.blit(transform.scale(spic_stamp5, (97, 67)), (362, 602))
            screen.blit(transform.scale(spic_stamp6, (97, 67)), (362, 682))
            screen.blit(transform.scale(spic_stamp7, (97, 67)), (482, 602))
            screen.blit(transform.scale(spic_stamp8, (97, 67)), (482, 682))
            screen.blit(transform.scale(spic_stamp9, (97, 67)), (602, 602))
            screen.blit(transform.scale(spic_stamp10, (97, 67)), (602, 682))
            if stamp1R.collidepoint(mx, my):
                draw.rect(screen, 0, stamp1R, 2)  # highlight button
                if one_press:
                    tool = 'stamp'
                    stamp = spic_stamp1
                    sz = 'sz2'
            elif stamp2R.collidepoint(mx, my):
                draw.rect(screen, 0, stamp2R, 2)
                if one_press:
                    tool = 'stamp'
                    stamp = spic_stamp2
                    sz = 'sz2'
            elif stamp3R.collidepoint(mx, my):
                draw.rect(screen, 0, stamp3R, 2)
                if one_press:
                    tool = 'stamp'
                    stamp = spic_stamp3
                    sz = 'sz2'
            elif stamp4R.collidepoint(mx, my):
                draw.rect(screen, 0, stamp4R, 2)
                if one_press:
                    tool = 'stamp'
                    stamp = spic_stamp4
                    sz = 'sz2'
            elif stamp5R.collidepoint(mx, my):
                draw.rect(screen, 0, stamp5R, 2)
                if one_press:
                    tool = 'stamp'
                    stamp = spic_stamp5
                    sz = 'sz2'
            elif stamp6R.collidepoint(mx, my):
                draw.rect(screen, 0, stamp6R, 2)
                if one_press:
                    tool = 'stamp'
                    stamp = spic_stamp6
                    sz = 'sz2'
            elif stamp7R.collidepoint(mx, my):
                draw.rect(screen, 0, stamp7R, 2)
                if one_press:
                    tool = 'stamp'
                    stamp = spic_stamp7
                    sz = 'sz2'
            elif stamp8R.collidepoint(mx, my):
                draw.rect(screen, 0, stamp8R, 2)
                if one_press:
                    tool = 'stamp'
                    stamp = spic_stamp8
                    sz = 'sz2'
            elif stamp9R.collidepoint(mx, my):
                draw.rect(screen, 0, stamp9R, 2)
                if one_press:
                    tool = 'stamp'
                    stamp = spic_stamp9
                    sz = 'sz2'
            elif stamp10R.collidepoint(mx, my):
                draw.rect(screen, 0, stamp10R, 2)
                if one_press:
                    tool = 'stamp'
                    stamp = spic_stamp10
                    sz = 'sz2'
        # shape tools
        elif stool == 'shapeTool':
            draw.line(screen, (224, 224, 224), (100, 706), (100, 763), 2)
            screen.blit(pic_lineF, (122, 602))  # set out button pictures
            draw.rect(screen, (255, 255, 255), line_uR)  # background for button pictures
            screen.blit(pic_lineU, (122, 682))
            draw.rect(screen, (255, 255, 255), rectangelFR)
            screen.blit(pic_rectF, (242, 602))
            draw.rect(screen, (255, 255, 255), rectangelUR)
            screen.blit(pic_rectU, (242, 682))
            screen.blit(pic_ovalF, (362, 602))
            screen.blit(pic_ovalU, (362, 682))
            screen.blit(pic_polygonF, (482, 602))
            screen.blit(pic_polygonU, (482, 682))
            draw.rect(screen, (255, 255, 255), starFR)
            screen.blit(pic_starF, (602, 602))
            screen.blit(pic_starU, (602, 682))
            if line_fR.collidepoint(mx, my):
                draw.rect(screen, 0, line_fR, 2)  # highlight button
                if one_press:
                    tool = 'lineF'
                    sz = 'sz3'
            elif line_uR.collidepoint(mx, my):
                draw.rect(screen, 0, line_uR, 2)
                if one_press:
                    tool = 'lineU'
                    sz = 'sz3'
            elif rectangelFR.collidepoint(mx, my):
                draw.rect(screen, 0, rectangelFR, 2)
                if one_press:
                    tool = 'rectF'
                    sz = 'sz3'
            elif rectangelUR.collidepoint(mx, my):
                draw.rect(screen, 0, rectangelUR, 2)
                if one_press:
                    tool = 'rectU'
                    sz = 'sz3'
            elif oval_fR.collidepoint(mx, my):
                draw.rect(screen, 0, oval_fR, 2)
                if one_press:
                    tool = 'ovalF'
                    sz = 'sz3'
            elif oval_uR.collidepoint(mx, my):
                draw.rect(screen, 0, oval_uR, 2)
                if one_press:
                    tool = 'ovalU'
                    sz = 'sz3'
            elif polygonFR.collidepoint(mx, my):
                draw.rect(screen, 0, polygonFR, 2)
                if one_press:
                    tool = 'polygonF'
                    sz = 'sz3'
            elif polygonUR.collidepoint(mx, my):
                draw.rect(screen, 0, polygonUR, 2)
                if one_press:
                    tool = 'polygonU'
                    sz = 'sz3'
            elif starFR.collidepoint(mx, my):
                draw.rect(screen, 0, starFR, 2)
                if one_press:
                    tool = 'starF'
                    sz = 'sz3'
            elif starUR.collidepoint(mx, my):
                draw.rect(screen, 0, starUR, 2)
                if one_press:
                    tool = 'starU'
                    sz = 'sz3'

        # other features frame.
        draw.rect(screen, (224, 224, 224), (840, 585, 360, 180))
        draw.rect(screen, (212, 175, 55), (840, 585, 360, 180), 2)
        # other features
        screen.blit(pic_clean, (842, 602))  # set out button pictures
        screen.blit(pic_change_background, (842, 682))
        screen.blit(pic_text, (962, 602))
        screen.blit(pic_settings, (962, 682))
        draw.rect(screen, (255, 255, 255), saveR)
        screen.blit(pic_save, (1082, 602))
        draw.rect(screen, (255, 255, 255), loadR)
        screen.blit(pic_load, (1082, 682))
        if cleanR.collidepoint(mx, my):  # clean the canvas
            draw.rect(screen, 0, cleanR, 2)  # highlight button
            if one_press:
                if len(can_list) < 31:  # save the canvas graph to undo list before cleaning.
                    can_list.append(screen.subsurface(canvas).copy())
                else:
                    del can_list[0]
                    can_list.append(screen.subsurface(canvas).copy())
                draw.rect(screen, canvasCol, canvas)
        elif change_backgroundR.collidepoint(mx, my):  # change background picture
            draw.rect(screen, 0, change_backgroundR, 2)
            if one_press:
                if pic_numb + nslide < 9:
                    nslide += 1
                else:
                    nslide = pic_numb * (-1)
        elif textR.collidepoint(mx, my):
            draw.rect(screen, 0, textR, 2)
            if one_press:
                tool = 'text'
                sz = 'sz4'
        elif settingsR.collidepoint(mx, my):
            draw.rect(screen, 0, settingsR, 2)
            if one_press:
                interface = 4
        elif saveR.collidepoint(mx, my):
            draw.rect(screen, 0, saveR, 2)
            if one_press:
                sz = 'sz4'
                name = getName(screen, True, sz4)  # use getName function to let user enter the name of the file
                if name != '':  # ensure there is no error with the file name and then save it
                    if '/' in name:
                        try:
                            image.save(screen.subsurface(canvas), name)
                        except:
                            # remind users about the error with the name
                            draw.rect(screen, (0, 255, 0), (296, 270, 800, 30))
                            draw.rect(screen, (0, 0, 255), (296, 270, 800, 30), 2)
                            comicFont = font.SysFont("Comic Sans MS", 28)
                            remind = comicFont.render('The folder name does not exit!', True, (155, 0, 0))
                            screen.blit(remind, (426, 266))
                            display.update()
                            time.wait(3000)  # show user for 3 seconds
                            screen.blit(can1, (196, 50))  # clear the reminding
                    elif len(name) > 4 and (name[-4] == ".jpg" or name[-4] == ".bmp" or name[-4] == ".png"):
                        image.save(screen.subsurface(canvas), name)
                    else:
                        name = name + ".jpg"
                        image.save(screen.subsurface(canvas), name)
        elif loadR.collidepoint(mx, my):
            draw.rect(screen, 0, loadR, 2)
            if one_press:
                sz = 'sz4'
                name = getName(screen, True, sz4)  # use getName function to let user enter the name of the file
                try:  # try/except statement can ensure the program won't crash
                    if len(can_list) < 31:  # save the canvas graph to undo list before loading other graphs
                        can_list.append(screen.subsurface(canvas).copy())
                    else:
                        del can_list[0]
                        can_list.append(screen.subsurface(canvas).copy())
                    screen.blit(transform.scale(image.load(name), (1000, 500)), (196, 50))
                except:
                    # remind users about the error with the name
                    draw.rect(screen, (0, 255, 0), (296, 270, 800, 30))
                    draw.rect(screen, (0, 0, 255), (296, 270, 800, 30), 2)
                    comicFont = font.SysFont("Comic Sans MS", 28)
                    remind = comicFont.render('The name is wrong or it does not exist!', True, (155, 0, 0))
                    screen.blit(remind, (426, 266))
                    display.update()
                    time.wait(3000)  # show user for 3 seconds
                    screen.blit(can1, (196, 50))  # clear the reminding

        # drawing with functions
        if canvas.collidepoint(mx, my) and canvas.collidepoint(omx, omy):
            screen.set_clip(canvas)  # ensure the graphs won't be drawn out of the canvas
            if tool == 'pencil':
                use_pencil(mx, my, omx, omy, sz1, drawCol)  # draw with functions
                use_mirror(live_mirror, mx, my, omx, omy, sz1, drawCol, use_pencil)  # live mirror drawing
            elif tool == 'chineseBrush':
                use_chineseBrush(mx, my, omx, omy, sz1, drawCol)
                use_mirror(live_mirror, mx, my, omx, omy, sz1, drawCol, use_chineseBrush)
            elif tool == 'spray':
                use_spray(mx, my, omx, omy, sz1, drawCol)
                use_mirror(live_mirror, mx, my, omx, omy, sz1, drawCol, use_spray)
            elif tool == 'highlighter':
                use_highlighter(mx, my, omx, omy, sz1, drawCol)
                use_mirror(live_mirror, mx, my, omx, omy, sz1, drawCol, use_highlighter)
            elif tool == 'mixedColpen':
                use_mixedColpen(mx, my, omx, omy, sz1, col_list)
                use_mirror(live_mirror, mx, my, omx, omy, sz1, col_list, use_mixedColpen)
            elif tool == 'eraser':
                use_eraser(mx, my, omx, omy, sz1, canvasCol)
                use_mirror(live_mirror, mx, my, omx, omy, sz1, canvasCol, use_eraser)
            elif tool == 'flood fill':
                use_flood_fill(mx, my, drawCol)
            elif tool == 'stamp':
                use_stamp(mx, my, stamp, sz2)
            elif tool == 'lineF':
                use_lineF(start, mx, my, drawCol, sz3)
            elif tool == 'lineU':
                use_lineU(start, mx, my, drawCol, sz3)
            elif tool == "rectF":
                use_rect(True, start, mx, my, drawCol, sz3)  # true determine the shape is filled
            elif tool == "rectU":
                use_rect(False, start, mx, my, drawCol, sz3)
            elif tool == 'ovalF':
                use_oval(True, start, mx, my, drawCol, sz3)
            elif tool == 'ovalU':
                use_oval(False, start, mx, my, drawCol, sz3)
            elif tool == 'polygonF':
                use_polygon(True, mx, my, polygonlist, drawCol, sz3, one_press, right_press)
                if right_press:
                    polygonlist = []  # clear the polygonlist for the next polygon to use
            elif tool == 'polygonU':
                use_polygon(False, mx, my, polygonlist, drawCol, sz3, one_press, right_press)
                if right_press:
                    polygonlist = []
            elif tool == 'starF':
                use_star(True, mx, my, start, drawCol, sz3)
            elif tool == 'starU':
                use_star(False, mx, my, start, drawCol, sz3)
            elif tool == 'text':
                use_text(mx, my, sz4, drawCol)
            screen.set_clip(None)

        # screen time out
        if mx == omx and my == omy and useTimeOut:  # count time for starting screen time out if no input
            out += 1
        else:
            out = 0  # input clears all the time counted
        if out > 900:  # is a period for approximately 30 seconds
            interface = 2  # go to screen time out interface
            out = 0
            sideshow = 0

        can1 = screen.subsurface(canvas).copy()  # for canvas to occur.
        canvasSet = 0  # for canvas to be recorded and shown


    elif interface == 3:
        screen.blit(pic_paletteBack, (0, 0))  # background

        # selecting colors by clicking color palette
        draw.rect(screen, 0, palette2R, 2)
        screen.blit(pic_palette2, (52, 52))
        if palette2R.collidepoint(mx, my):
            draw.rect(screen, (255, 255, 255), palette2R, 2)  # highlight button
            if one_press:
                drawCol = screen.get_at((mx, my))

        # selecting colors by dragging wooden rectangles.This sector uses rgb logic to change colors. Techincally users can use 255**3 kinds of colors.
        for x in range(0, 256):  # set rgb ramps.
            draw.line(screen, (x, 0, 0), (50 + 2 * x, 500), (50 + 2 * x, 550), 2)
            draw.line(screen, (0, x, 0), (50 + 2 * x, 575), (50 + 2 * x, 625), 2)
            draw.line(screen, (0, 0, x), (50 + 2 * x, 650), (50 + 2 * x, 700), 2)
        draw.rect(screen, (224, 224, 224), (50, 500, 510, 50), 2)  # set frames for the ramps
        draw.rect(screen, (224, 224, 224), (50, 575, 510, 50), 2)
        draw.rect(screen, (224, 224, 224), (50, 650, 510, 50), 2)
        r = drawCol[0]  # slice rgb values
        g = drawCol[1]
        b = drawCol[2]
        screen.blit(pic_wood, (50 + 2 * r, 495))  # blit wook chanks based on the rgb values.
        screen.blit(pic_wood, (50 + 2 * g, 570))
        screen.blit(pic_wood, (50 + 2 * b, 645))
        if redSection.collidepoint(mx, my) and redSection.collidepoint(start) and mb[
            0] == 1:  # click on the ramps or dragging chanks to change rgb values.
            r = int((mx - 50) / 2)
        elif greenSection.collidepoint(mx, my) and greenSection.collidepoint(start) and mb[0] == 1:
            g = int((mx - 50) / 2)
        elif blueSection.collidepoint(mx, my) and blueSection.collidepoint(start) and mb[0] == 1:
            b = int((mx - 50) / 2)
        drawCol = (r, g, b)  # new color

        # showing the chosed color on colorBar and setup testing canvas
        draw.rect(screen, drawCol, colorBarR)
        if testingCanvasBack:
            screen.blit(can2, (650, 200))
        else:
            draw.rect(screen, (255, 255, 255), testingCanvasR)

        # set up pencil for testing color and clean for cleaning the testing canvas.
        draw.rect(screen, 0, testingPencilandCleanR)
        if testingPencilANDclean_switch == 1:  # blit picture based on the testing tool being used
            screen.blit(pic_testingClean, (662, 552))
        else:
            draw.rect(screen, (255, 255, 255), (662, 552, 147, 147))
            screen.blit(pic_testingPencil, (662, 552))
        if testingPencilandCleanR.collidepoint(mx, my):
            draw.rect(screen, (255, 255, 255), testingPencilandCleanR, 2)
            if one_press:
                if testingPencilANDclean_switch == 1:
                    draw.rect(screen, (255, 255, 255), testingCanvasR)
                    can2 = screen.subsurface(
                        testingCanvasR).copy()  # Otherwise, even we cleaned the canvas, when the loop works for the next time, it will only show the canvas with graph.
                    testingCanvasBack = True
                testingPencilANDclean_switch *= -1
        # use the testing tools
        if canvas.collidepoint(mx, my) and canvas.collidepoint(start) and mb[
            0] == 1 and testingPencilANDclean_switch == 1:
            screen.set_clip(testingCanvasR)
            use_pencil(mx, my, omx, omy, sz1, drawCol)
            can2 = screen.subsurface(testingCanvasR).copy()
            testingCanvasBack = True
            screen.set_clip(None)

        # canvas color button adapts the canvas color to the color showned on the color bar.It effects eraser and clean button.
        draw.rect(screen, canvasCol, canvasColR)  # current canvas color is shown via the background of the button
        draw.rect(screen, 0, canvasColR, 2)
        screen.blit(pic_canvasCol, (822, 552))  # set out button pictures
        if canvasColR.collidepoint(mx, my):
            draw.rect(screen, (255, 255, 255), canvasColR, 2)  # highlight button
            if one_press:
                lastCanCol = canvasCol
                canvasCol = drawCol
                canvasSet = 2  # once being back to graphing interface, this variable will cause the change of the canvas color

        # back to graphing interface
        draw.rect(screen, 0, go_to_draw2R)
        screen.blit(go_to_draw2, (982, 552))  # set out button pictures
        if go_to_draw2R.collidepoint(mx, my):
            draw.rect(screen, (255, 255, 255), go_to_draw2R, 2)  # highlight button
            if one_press:
                interface = 0  # go back to graphing interface


    elif interface == 4:
        screen.blit(pic_settingsBack, (0, 0))  # background

        # change theme
        for x in range(10):  # background pictures
            screen.blit(transform.scale(pic_lis1[x], (100, 70)), (100 + 100 * x, 100))
            screen.blit(transform.scale(pic_lis2[x], (100, 70)), (100 + 100 * x, 180))
        alphaa = Surface((1000, 70), SRCALPHA)
        draw.rect(alphaa, (0, 0, 0, 130), (0, 0, 1000, 70))
        if current_pic_lis == pic_lis2:  # the previously unused theme bar is conver by alpha surface to be gloomy
            screen.blit(alphaa, (100, 100))
        else:
            screen.blit(alphaa, (100, 180))
        draw.rect(screen, (204, 255, 153), theme1R, 2)  # frame for themes
        draw.rect(screen, (204, 255, 153), theme2R, 2)
        if theme1R.collidepoint(mx, my):  # choose theme
            draw.rect(screen, (255, 0, 0), theme1R, 2)  # highlight button
            if one_press:
                current_pic_lis = pic_lis1
        elif theme2R.collidepoint(mx, my):
            draw.rect(screen, (255, 0, 0), theme2R, 2)
            if one_press:
                current_pic_lis = pic_lis2

        # change music
        alpha = Surface((197, 197), SRCALPHA)
        draw.rect(alpha, (0, 0, 0, 130), (0, 0, 197, 197))
        draw.rect(screen, (204, 255, 153), (musicSwordR))
        screen.blit(pic_sword, (102, 302))
        if currentMusic != 'sword':
            screen.blit(alpha, (102, 302))  # blit to show the music is not current music
        draw.rect(screen, (204, 255, 153), (musicPianoR))  # background for button pictures
        screen.blit(pic_piano, (302, 302))  # set out button pictures
        if currentMusic != 'piano':
            screen.blit(alpha, (302, 302))
        draw.rect(screen, (204, 255, 153), (musicViolinR))
        screen.blit(pic_violin, (502, 302))
        if currentMusic != 'violin':
            screen.blit(alpha, (502, 302))
        draw.rect(screen, (204, 255, 153), (musicBambooFluteR))
        screen.blit(pic_BambooFlute, (702, 302))
        if currentMusic != 'bambooFlute':
            screen.blit(alpha, (702, 302))
        draw.rect(screen, (204, 255, 153), (musicErhuR))
        screen.blit(pic_Erhu, (902, 302))
        if currentMusic != 'erhu':
            screen.blit(alpha, (902, 302))
        if musicSwordR.collidepoint(mx, my):
            draw.rect(screen, (255, 0, 0), musicSwordR, 2)
            if one_press:
                currentMusic = 'sword'
                music = True
                mixer.music.stop()  # reset music
                mixer.music.load("settings/sword.mp3")
                mixer.music.play(-1)
        elif musicPianoR.collidepoint(mx, my):
            draw.rect(screen, (255, 0, 0), musicPianoR, 2)
            if one_press:
                currentMusic = 'piano'
                music = True
                mixer.music.stop()
                mixer.music.load("settings/piano.mp3")
                mixer.music.play(-1)
        elif musicViolinR.collidepoint(mx, my):
            draw.rect(screen, (255, 0, 0), musicViolinR, 2)
            if one_press:
                currentMusic = 'violin'
                music = True
                mixer.music.stop()
                mixer.music.load("settings/violin.mp3")
                mixer.music.play(-1)
        elif musicBambooFluteR.collidepoint(mx, my):
            draw.rect(screen, (255, 0, 0), musicBambooFluteR, 2)
            if one_press:
                currentMusic = 'bambooFlute'
                music = True
                mixer.music.stop()
                mixer.music.load("settings/Bamboo Flute.mp3")
                mixer.music.play(-1)
        elif musicErhuR.collidepoint(mx, my):
            draw.rect(screen, (255, 0, 0), musicErhuR, 2)
            if one_press:
                currentMusic = 'erhu'
                music = True
                mixer.music.stop()
                mixer.music.load("settings/erhu.mp3")
                mixer.music.play(-1)

        # Control volume.It can be done via rolling the mouse, clicking on left/right, or press on the bar
        draw.rect(screen, (204, 255, 153), (100, 500, 1000, 100))  # volume frame
        draw.rect(screen, (224, 224, 224), (102, 502, 997, 97))
        if music:  # blit different pictures depending on if the music is playing
            screen.blit(pic_volumeButtonPa, (250, 510))
        else:
            screen.blit(pic_volumeButtonPl, (250, 510))
        if volumeButtonR.collidepoint(mx, my):
            draw.rect(screen, (255, 0, 0), volumeButtonR, 2)  # highlight button
            if one_press:
                if music:  # this if/else statement pause/unpause music
                    mixer.music.pause()
                    music = False
                else:
                    mixer.music.unpause()
                    music = True
        draw.rect(screen, (154, 0, 0), (348, 538, 604, 24))  # background to show the volume
        draw.rect(screen, (255, 255, 255), volumeBarR)
        draw.rect(screen, (255, 0, 0), (349, 540, 1 + volume * 600, 20))  # show volume
        if volumeBarR.collidepoint(mx, my) and volumeBarR.collidepoint(start) and mb[
            0] == 1:  # Change the volume by click on the volume bar
            volume = 0.1 * int((mx - 320) / 60)
            mixer.music.set_volume(0.1 * int((mx - 320) / 60))

        # timeout button
        draw.rect(screen, (204, 255, 153), timeOutR)  # button background
        if useTimeOut == True:  # different picture show if screen time out is blocked
            screen.blit(pic_timeOut1, (102, 652))
        else:
            screen.blit(pic_timeOut2, (102, 652))
        if timeOutR.collidepoint(mx, my):
            draw.rect(screen, (255, 0, 0), timeOutR, 2)  # highlight button
            if one_press:  # enable/disable screen time out
                if useTimeOut:
                    useTimeOut = False
                else:
                    useTimeOut = True

        # Live mirror button
        draw.rect(screen, (204, 255, 153), live_mirrorR)
        if live_mirror == 0:  # this if/else statement draw differet live mirror pictures basing on which live mirror is being used
            screen.blit(pic_live_mirror1, (502, 652))
            alpha = Surface((197, 97), SRCALPHA)
            draw.rect(alpha, (0, 0, 0, 130), (0, 0, 197, 197))
            screen.blit(alpha, (502, 652))
        elif live_mirror == 1:
            screen.blit(pic_live_mirror1, (502, 652))
        elif live_mirror == 2:
            screen.blit(pic_live_mirror2, (502, 652))
        else:
            screen.blit(pic_live_mirror3, (502, 652))
        if live_mirrorR.collidepoint(mx, my):
            draw.rect(screen, (255, 0, 0), live_mirrorR, 2)  # highlight button
            if one_press:  # press to change live mirrors or disable live mirror
                live_mirror += 1
                if live_mirror > 3:
                    live_mirror = 0
        # go to draw
        draw.rect(screen, (204, 255, 153), go_to_draw3R)  # button background
        screen.blit(go_to_draw3, (902, 652))
        if go_to_draw3R.collidepoint(mx, my):
            draw.rect(screen, (255, 0, 0), go_to_draw3R, 2)  # highlight button
            if one_press:
                interface = 0  # go back to graphing interface


    elif interface == 1:
        # background.
        screen.blit(virtuoso, (0, 0))

        # name of the program.Blit pictures and use alpha surfaces to make them look nicer
        screen.blit(pic_welcome, (100, 50))
        screen.blit(pic_name1, (500, 50))
        screen.blit(pic_name2, (800, 50))
        draw.rect(screen, (255, 0, 0), (500, 50, 600, 100), 2)
        alpha = Surface((600, 100), SRCALPHA)
        draw.rect(alpha, (255, 0, 0, 30), (0, 0, 300, 50))
        draw.rect(alpha, (0, 255, 0, 30), (300, 50, 300, 50))
        draw.rect(alpha, (255, 255, 0, 30), (0, 50, 300, 50))
        draw.rect(alpha, (0, 0, 255, 30), (300, 0, 300, 50))
        screen.blit(alpha, (500, 50))

        # switch to other interfaces.
        draw.rect(screen, (255, 0, 0), go_to_drawR, 2)  # button background
        screen.blit(go_to_draw, (852, 552))  # button picture
        draw.rect(screen, (255, 0, 0), settings2R, 2)
        screen.blit(pic_settings2, (152, 552))
        if go_to_drawR.collidepoint(mx, my):
            draw.rect(screen, (0, 255, 0), go_to_drawR, 2)  # highlight button
            if one_press:
                interface = 0  # switch to the graphing interface
        elif settings2R.collidepoint(mx, my):
            draw.rect(screen, (0, 255, 0), settings2R, 2)
            if one_press:
                interface = 4  # switch to the graphing interface


    elif interface == 2:
        slideshow += 1  # count time for changing background
        if slideshow < 250:  # about 5 second
            screen.blit(current_pic_lis[pic_numb + nslide2], (0, 0))
        else:
            if pic_numb + nslide2 < 9:  # change background
                nslide2 += 1
            else:
                nslide2 = pic_numb * (-1)
            screen.blit(current_pic_lis[pic_numb + nslide2], (0, 0))
            slideshow = 0
        if pressdown or mx != omx or my != omy:
            interface = 0  # input to switch to the graphing interface
    omx, omy = mx, my  # get last point position for the tools
    display.flip()

font.quit()
quit()
