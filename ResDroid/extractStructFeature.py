#!/usr/bin/env python
# coding=utf-8
'''
@ author   : chicho
@ data     : 2015-03-04
@ version  : 1.2
@ function : parse GuiHierarchy file and get the AS and ES 
              1. get AS 
              2. get Eseq
              3. insert into Database layout_event
@ running  : python extractStructFeature.py
'''



import os
import conf
import sys
import MySQLdb
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


if (len(sys.argv)<2):

    # print tip info

    print'''
    =========================================================
    You can use the default GuiHierarchy files' path or input the path you like!
    usage : python extractStructFeature.py 
    you need to input <GuiHierarchy_path> or employ the default path
    e.g. sootAndroidOut
    Input : 0 -> default path
    Input : 1 -> your personal path
    =========================================================
    '''


    input = raw_input("you choice? 0 or 1:\n")

    while (input != '0') and (input != '1'):
        print "you input is wrong!"
        input = raw_input("you choice? 0 or 1:\n")


    if ( input == "0" ):
        print "you choose the default path! ...processing...\n" 
        path = "/home/chicho/result/sootAndroidOut_1_ARC/"
    else:
        path = raw_input("you GUI file path:\n")
        if not os.path.exists(path):
            print "Cannot find the path, please check you input path!:p\n"
            sys.exit(1)

#end if


# this file is temp file to store the method signature (event handler)
filePath = "/home/chicho/Workspace/ResDroid/event"

if not os.path.exists(filePath):
    os.makedirs(filePath)


structOutPath="/home/chicho/Workspace/ResDroid/structout.txt"


itemDict = {
    'AnalogClock' : 'a1',
    'ImageView' : 'a2',
    'KeyboardView' : 'a3',
    'MediaRouteButton' : 'a4',
    'ProgressBar' : 'a5',
    'Space' : 'a6',
    'SurfaceView' : 'a7',
    'TextView' : 'a8',
    'TextureView' : 'a9',
    'ViewGroup' : 'a0',
    'ViewStub' : 'b1',
    'AbsListView' : 'b2',
    'AbsSeekBar' : 'b3',
    'AbsSpinner' : 'b4',
    'AbsoluteLayout' : 'b5',
    'ActionMenuView' : 'b6',
    'AdapterView' : 'b7',
    'AdapterViewAnimator' : 'b8',
    'AdapterViewFlipper' : 'b9',
    'AppWidgetHostView' : 'b0',
    'AutoCompleteTextView' : 'c1',
    'BaseCardView' : 'c2',
    'Button' : 'c3',
    'CalendarView' : 'c4',
    'CardView' : 'c5',
    'CheckBox' : 'c6',
    'CheckedTextView' : 'c7',
    'Chronometer' : 'c8',
    'CompoundButton' : 'c9',
    'ContentLoadingProgressBar' : 'c0',
    'DatePicker' : 'd1',
    'DialerFilter' : 'd2',
    'DigitalClock' : 'd3',
    'DrawerLayout' : 'd4',
    'EditText' : 'd5',
    'ExpandableListView' : 'd6',
    'ExtractEditText' : 'd7',
    'FragmentBreadCrumbs' : 'd8',
    'FragmentTabHost' : 'd9',
    'FrameLayout' : 'd0',
    'GLSurfaceView' : 'e1',
    'Gallery' : 'e2',
    'GestureOverlayView' : 'e3',
    'GridLayout' : 'e4',
    'GridView' : 'e5',
    'HorizontalGridView' : 'e6',
    'HorizontalScrollView' : 'e7',
    'ImageButton' : 'e8',
    'ImageCardView' : 'e9',
    'ImageSwitcher' : 'e0',
    'LinearLayout' : 'f1',
    'LinearLayoutCompat' : 'f2',
    'ListRowHoverCardView' : 'f3',
    'ListRowView' : 'f4',
    'ListView' : 'f5',
    'MediaController' : 'f6',
    'MultiAutoCompleteTextView' : 'f7',
    'NumberPicker' : 'f8',
    'PagerTabStrip' : 'f9',
    'PagerTitleStrip' : 'f0',
    'QuickContactBadge' : 'g0',
    'RadioButton' : 'g1',
    'RadioGroup' : 'g2',
    'RatingBar' : 'g3',
    'RecyclerView' : 'g4',
    'RelativeLayout' : 'g5',
    'RowHeaderView' : 'g6',
    'ScrollView' : 'g7',
    'SearchBar' : 'g8',
    'SearchEditText' : 'g9',
    'SearchOrbView' : 'g0',
    'SearchView' : 'h1',
    'SeekBar' : 'h2',
    'ShadowOverlayContainer' : 'h3',
    'SlidingDrawer' : 'h4',
    'SlidingPaneLayout' :'h5',
    'SpeechOrbView' : 'h6',
    'Spinner' : 'h7',
    'StackView' : 'h8',
    'SwipeRefreshLayout' : 'h9',
    'Switch' : 'h0',
    'SwitchCompat' : 'i1',
    'TabHost' : 'i2',
    'TabWidget' : 'i3',
    'TableLayout' : 'i4',
    'TableRow' : 'i5',
    'TextClock' : 'i6',
    'TextSwitcher' : 'i7',
    'TimePicker' : 'i8',
    'ToggleButton' : 'i9',
    'Toolbar' : 'i0',
    'TvView' : 'j1',
    'TwoLineListItem' : 'j2',
    'VerticalGridView' : 'j3',
    'VideoView' : 'j4',
    'ViewAnimator' : 'j5',
    'ViewFlipper' : 'j6',
    'ViewPager' : 'j7',
    'ViewSwitcher' : 'j8',
    'WebView' : 'j9',
    'ZoomButton' : 'j0',
    'ZoomControls' : 'k1',
    'Menu' : 'k2',
    'MenuItem' : 'k3',
    'Unknown' : 'X'
}




#
#-------------------------
# Database connection
#-------------------------
#
def connect_db():
    con = MySQLdb.connect(
        host = conf.DB_HOST,
        user = conf.DB_USER,
        passwd = conf.DB_PASSWD,
        db = conf.DB_NAME,
        charset = 'utf8')
    return con 



conn = connect_db()
curs = conn.cursor()


def read_guihierarchy():
    pass 


#-----------------------
# traverse the xmlfile
#-----------------------


def traverse(xmlfile):
    dict = {}

    try:
        tree = ET.parse(xmlfile)
        root = tree.getroot()


        for child in root:
            viewSeq = []
            viewtrSeq = []
            viewStr = ""
            
            if (child.tag == 'Activity'):
                ActivityName = child.get('name')
               
                if ActivityName not in dict:
                    viewtrSeq = do_traverse(child,viewSeq)
                    viewStr = seq2str(viewtrSeq)
    

                    if (viewStr != ''):
                        dict[ActivityName] = viewStr
                
          
        return dict

    except Exception as e:
        print "cannot parse the GuiHierarchy file!"
        cmd = "echo {0} >> structWongLog.txt".format(xmlfile) # xmlfile == guifile
        os.system(cmd)
        return dict 


def do_traverse(element, seq):
    if element is None:
        return seq 

    for child in element:
        if (child.attrib.has_key('type')):

            viewType = child.get('type')
            viewName = viewType.split('.')[-1]
            seq.append(viewName)


        do_traverse(child, seq)

    return seq
            



def seq2str(seq):
    str = ""

    if len(seq) is 0:
        return str



    for s in seq:
        
        if s in itemDict:
            str += itemDict[s]
        else:
            str += itemDict['Unknown']
        
    return str 



def getActivitySeq(dict):
    ASeq = ""

    if len(dict) is 0:
        return ASeq
    

    for i in dict:
        ASeq += dict[i]


    return ASeq



#------------------------------
# Eventhandler extraction
#------------------------------
'''
The output result stores in filePath, the file is eventHandler.txt 
'''
def getEventHandler(guifile):
    
    eventname = os.path.basename(guifile)

    eventfile = eventname.split("-")[-2] + ".txt"

    eventOutPath = os.path.join(filePath,eventfile)
    
    cmd = "touch {0}".format(eventOutPath)
    os.system(cmd)

    
    try:
        tree = ET.parse(guifile)
        for elem in tree.iter():
            if ( elem.tag == 'EventAndHandler' ):
                event = elem.get('event')

                if( elem.attrib.has_key('realHandler') ):
                    realHandler = elem.get('realHandler')
                    cmd = "./handlerExtract.sh '{0}' {1}".format(realHandler,eventOutPath)
                    os.system(cmd)
                else:
                    handler = elem.get('handler')
                    cmd = "./handlerExtract.sh '{0}' {1}".format(handler,eventOutPath)
                    os.system(cmd)

                
                '''
                if( elem.attrib.has_key('realHandler') ):
                    realHandler = elem.get('realHandler')
                    cmd = "./handlerExtract.sh '{0}'".format(realHandler)
                    os.system(cmd)
                '''
    except:
        print "cannot parse the GuiHierarchy file!\n"

        


    return eventOutPath



def parseEventHandlerfile(eventfile):
    signature = ""

    f = open(eventfile, 'r')

    for line in f.readlines():
        try:
            line = line.replace("\n","")
            signature += line 
        except ValueError:
            print "cannot parse file!"


    f.close()

    cmd = "rm {0}".format(eventfile)
    os.system(cmd)

    return signature


#-----------end ------------------




def get_Category():

    category = "other"

    plist = path.split("/")

    cateName = plist.pop()


    if cateName == "sootAndroidOut_1_ARC":
        category = "1_ARCADE"

    elif cateName == "sootAndroidOut_2_DEMO":
        category = "2_DEMO"
        
    elif cateName == "sootAndroidOut_3_ENT":
        category = "3_ENTERTANMENT"

    elif cateName == "sootAndroidOut_4_FIN":
        category = "4_FINANCE"

    elif cateName == "sootAndroidOut_5_HEA":
        category == "5_HEALTH"

    elif cateName == "sootAndroidOut_6_LIB":
        category = "6_LIBRARIES"

    elif cateName == "sootAndroidOut_7_LIF":
        category = "7_LIFESTYLE"

    elif cateName == "sootAndroidOut_8_MUL":
        category = "8_MULTIMEDIA"

    elif cateName == "sootAndroidOut_9_NEWS":
        category = "9_NEWS"

    elif cateName == "sootAndroidOut_10_REF":
        category = "10_REFERENCE"

    elif cateName == "sootAndroidOut_11_THE":
        category = "11_THEMES"

    elif cateName == "sootAndroidOut_12_TRA":
        category = "12_TRAVEL"

    elif cateName == "sootAndroidOut_13_BRA":
        category = "13_BRAIN"

    elif cateName == "sootAndroidOut_14_CARDS":
        category = "14_CARDS"

    elif cateName == "sootAndroidOut_15_CAS":
        category = "15_CASUAL"

    elif cateName == "sootAndroidOut_16_COMICS":
        category = "16_COMICS"

    elif cateName == "sootAndroidOut_17_COMM":
        category = "17_COMMUNICATION"

    elif cateName == "sootAndroidOut_18_PRO":
        category = "18_PRODUCTIVITY"

    elif cateName == "sootAndroidOut_19_SHOP":
        category = "19_SHOPPING"

    elif cateName == "sootAndroidOut_20_SOC":
        category = "20_SOCIAL"

    elif cateName == "sootAndroidOut_21_SPO":
        category = "21_SPORTS"

    elif cateName == "sootAndroidOut_22_TOOLS":
        category = "22_TOOLS"

    elif cateName == "sootAndroidOut_23_BUS":
        category = "23_BUSINESS"

    elif cateName == "sootAndroidOut_24_PER":
        category = "24_PERSONALIZATION"

    elif cateName == "sootAndroidOut_25_WALL":
        category = "25_APP_WALLPAPER"

    elif cateName == "sootAndroidOut_26_SPORT":
        category = "26_SPORTS_GAME"

    elif cateName == "sootAndroidOut_27_GAME":
        category = "27_GAMW_WALLPAPER"
    
    elif cateName == "sootAndroidOut_28_RAC":
        category = "28_RACING"

    elif cateName == "sootAndroidOut_29_GAME":
        category = "29_GAME_WIDGETS"

    elif cateName == "sootAndroidOut_30_WID":
        category = "30_APP_WIDGETS"

    elif cateName == "sootAndroidOut_31_EDU":
        category = "31_EDUCATION"

    elif cateName == "sootAndroidOut_32_MED":
        category = "32_MEDICAL"

    elif cateName == "sootAndroidOut_33_MUS":
        category = "33_MUSIC"

    elif cateName == "sootAndroidOut_34_PHO":
        category = "34_PHOTOGRAPHY"

    elif cateName == "sootAndroidOut_35_TRANS":
        category = "35_TRANSPORTATION"

    elif cateName == "sootAndroidOut_36_WEATHER":
        category = "36_WEATHER"

    elif cateName == "origapps":
        category = "gt_original"

    elif cateName == "repackaged":
        category = "gt_repackaged"

    else:
        category = "other"

    return category


#****************************

if __name__ == "__main__":
    
    GuiHierarchyList = os.listdir(path)
    dict = {}


    f = open(structOutPath,'r') # structOutPath = "structout.txt"
    processedGUIList = []
    for guifile in f.readlines():
        guifile = guifile.replace("\n","")
        processedGUIList.append(guifile)


    # id is app_id

    for guifile in GuiHierarchyList:
        if (guifile.endswith(".xml")):
            guifilePath = os.path.join(path,guifile)
           
              
            # judge if the file has already exists
            if guifilePath in processedGUIList:
                tips = "{0} has already processed!".format(guifilePath)
                print tips
                continue 

            dict = traverse(guifilePath) #{"act1":"abscd","act2":"sdags"}
            
            Aseq = getActivitySeq(dict) # get the Activity gui sequences of App

            
            # get the Event handler 
            '''
            There are two steps : 1. getEventHandler 2. parse the eventHandler.txt file and get the signature 
            '''
            eventfile=getEventHandler(guifilePath)
            
            signature = parseEventHandlerfile(eventfile) # get method signature 
            

            ''' 
            try:
                appname = guifile.splite("-")
                appname.pop()

                appname = "-".join(appname) + ".apk"
                #appname = guifile 
            except:
                pass 
            '''
            
            appname = guifile.split("-")
            appname.pop()
            appname = '-'.join(appname) + ".apk"
            
            category = get_Category()

            #conn = connect_db()
            #curs = conn.cursor()
            
            
            sql_tmp = "insert into layout_event(app_name, app_path, category, Lseq, Eseq)  VALUES('{0}', '{1}', '{2}','{3}','{4}')"
            sql = sql_tmp.format(appname, guifilePath, category, Aseq, signature)
        
            
            try:
                curs.execute(sql)
                conn.commit()            
            
                tips = "now insert {0} into the table layout_event".format(guifilePath) 
                print tips
 
                cmd = "echo {0} >> structout.txt".format(guifilePath)
                os.system(cmd)

            except:
                cmd = "echo {0}* Cannot insert into Database >> structWongLog.txt".format(guifilePath)
                os.system(cmd)
                continue

    
    curs.close()
    conn.close()


    cmd = "rm -r {0}".format(filePath)
    os.system(cmd)
    

    print "all work done!"     

