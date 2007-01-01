import GemRB

StartWindow = 0
TutorialWindow = 0
QuitWindow = 0
ExitButton = 0
SinglePlayerButton = 0
OptionsButton = 0
MultiPlayerButton = 0
MoviesButton = 0

def OnLoad():
	global StartWindow, TutorialWindow, QuitWindow
	global ExitButton, OptionsButton, MultiPlayerButton, MoviesButton

	skip_videos = GemRB.GetVar ("SkipIntroVideos")
	if not skip_videos:
		GemRB.PlayMovie ("BISLOGO")
		GemRB.PlayMovie ("BWDRAGON")
		GemRB.PlayMovie ("WOTC")
		GemRB.PlayMovie ("INTRO15F")

	# Find proper window border for higher resolutions
	screen_width = GemRB.GetSystemVariable (SV_WIDTH)
	screen_height = GemRB.GetSystemVariable (SV_HEIGHT)
	if screen_width == 800:
		GemRB.LoadWindowFrame("STON08L", "STON08R", "STON08T", "STON08B")
	elif screen_width == 1024:
		GemRB.LoadWindowFrame("STON10L", "STON10R", "STON10T", "STON10B")
		
	GemRB.LoadWindowPack("START", 640, 480)
#tutorial subwindow
	TutorialWindow = GemRB.LoadWindow(5)
	TextAreaControl = GemRB.GetControl(TutorialWindow, 1)
	CancelButton = GemRB.GetControl(TutorialWindow, 11)
	PlayButton = GemRB.GetControl(TutorialWindow, 10)
	GemRB.SetText(TutorialWindow, TextAreaControl, 44200)
	GemRB.SetText(TutorialWindow, CancelButton, 13727)
	GemRB.SetText(TutorialWindow, PlayButton, 33093)
	GemRB.SetEvent(TutorialWindow, PlayButton, IE_GUI_BUTTON_ON_PRESS, "PlayPress")
	GemRB.SetEvent(TutorialWindow, CancelButton, IE_GUI_BUTTON_ON_PRESS, "CancelTut")
#quit subwindow
	QuitWindow = GemRB.LoadWindow(3)
	QuitTextArea = GemRB.GetControl(QuitWindow,0)
	CancelButton = GemRB.GetControl(QuitWindow, 2)
	ConfirmButton = GemRB.GetControl(QuitWindow, 1)
	GemRB.SetText(QuitWindow, QuitTextArea, 19532)
	GemRB.SetText(QuitWindow, CancelButton, 13727)
	GemRB.SetText(QuitWindow, ConfirmButton, 15417)
	GemRB.SetEvent(QuitWindow, ConfirmButton, 0, "ExitConfirmed")
	GemRB.SetEvent(QuitWindow, CancelButton, 0, "ExitCancelled")
#main window
	StartWindow = GemRB.LoadWindow(0)
	GemRB.SetWindowFrame (StartWindow)
	
	SinglePlayerButton = GemRB.GetControl(StartWindow, 0)
	ExitButton = GemRB.GetControl(StartWindow, 3)
	OptionsButton = GemRB.GetControl(StartWindow, 4)
	MultiPlayerButton = GemRB.GetControl(StartWindow, 1)
	MoviesButton = GemRB.GetControl(StartWindow, 2)
	DisabledButton = GemRB.GetControl(StartWindow, 5)
	GemRB.CreateLabel(StartWindow, 0x0fff0000, 0,450,640,30, "REALMS", "", 1)
	Label=GemRB.GetControl(StartWindow, 0x0fff0000)
	GemRB.SetText(StartWindow, Label,GEMRB_VERSION)
	GemRB.SetButtonState(StartWindow, DisabledButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetButtonState(StartWindow, SinglePlayerButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonState(StartWindow, ExitButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonState(StartWindow, OptionsButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonState(StartWindow, MultiPlayerButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonState(StartWindow, MoviesButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetText(StartWindow, SinglePlayerButton, 15413)
	GemRB.SetText(StartWindow, ExitButton, 15417)
	GemRB.SetText(StartWindow, OptionsButton, 13905)
	GemRB.SetText(StartWindow, MultiPlayerButton, 15414)
	GemRB.SetText(StartWindow, MoviesButton, 15415)
	GemRB.SetText(StartWindow, DisabledButton, "")
	GemRB.SetEvent(StartWindow, SinglePlayerButton, IE_GUI_BUTTON_ON_PRESS, "SinglePlayerPress")
	GemRB.SetEvent(StartWindow, ExitButton, IE_GUI_BUTTON_ON_PRESS, "ExitPress")
	GemRB.SetEvent(StartWindow, OptionsButton, IE_GUI_BUTTON_ON_PRESS, "OptionsPress")
	GemRB.SetEvent(StartWindow, MultiPlayerButton, IE_GUI_BUTTON_ON_PRESS, "MultiPlayerPress")
	GemRB.SetEvent(StartWindow, MoviesButton, IE_GUI_BUTTON_ON_PRESS, "MoviesPress")
	GemRB.SetEvent(StartWindow, DisabledButton, IE_GUI_BUTTON_ON_PRESS, "")
	GemRB.SetVisible(QuitWindow, 0)
	GemRB.SetVisible(TutorialWindow, 0)
	GemRB.SetVisible(StartWindow, 1)
	GemRB.LoadMusicPL("Theme.mus")
	return
	
def SinglePlayerPress():
	
	GemRB.SetText(StartWindow, OptionsButton, "")
	GemRB.SetText(StartWindow, SinglePlayerButton, 13728)
	GemRB.SetText(StartWindow, ExitButton, 15416)
	GemRB.SetText(StartWindow, MultiPlayerButton, 13729)
	GemRB.SetText(StartWindow, MoviesButton, 33093)
	GemRB.SetEvent(StartWindow, MultiPlayerButton, 0, "LoadSingle")
	GemRB.SetEvent(StartWindow, SinglePlayerButton, 0, "NewSingle")
	GemRB.SetEvent(StartWindow, MoviesButton, 0, "Tutorial")
	GemRB.SetEvent(StartWindow, ExitButton, 0, "BackToMain")
	GemRB.SetButtonState(StartWindow, OptionsButton, IE_GUI_BUTTON_DISABLED)
	return

def MultiPlayerPress():
	
	GemRB.SetText(StartWindow, OptionsButton, "")
	GemRB.SetText(StartWindow, SinglePlayerButton, 20642)
	GemRB.SetText(StartWindow, ExitButton, 15416)
	GemRB.SetText(StartWindow, MultiPlayerButton, "")
	GemRB.SetText(StartWindow, MoviesButton, 11825)
	GemRB.SetEvent(StartWindow, MultiPlayerButton, 0, "")
	GemRB.SetEvent(StartWindow, SinglePlayerButton, 0, "ConnectPress")
	GemRB.SetEvent(StartWindow, MoviesButton, 0, "PregenPress")
	GemRB.SetEvent(StartWindow, ExitButton, 0, "BackToMain")
	GemRB.SetButtonState(StartWindow, MultiPlayerButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetButtonState(StartWindow, OptionsButton, IE_GUI_BUTTON_DISABLED)
	return

def ConnectPress():
#well...
	#GemRB.SetVar("PlayMode",2)
	return

def PregenPress():
	GemRB.UnloadWindow(StartWindow)
	GemRB.UnloadWindow(QuitWindow)
	GemRB.UnloadWindow(TutorialWindow)
	#do not start game after chargen
	GemRB.SetVar("PlayMode",-1) #will return to pregen screen
	GemRB.SetVar("Slot",0)
	GemRB.SetNextScript("CharGen") #should be pregen screen
	return

def LoadSingle():
	GemRB.UnloadWindow(StartWindow)
	GemRB.UnloadWindow(QuitWindow)
	GemRB.UnloadWindow(TutorialWindow)
	GemRB.SetVar("PlayMode",0)
	GemRB.SetNextScript("GUILOAD")
	return

def NewSingle():
	GemRB.UnloadWindow(StartWindow)
	GemRB.UnloadWindow(QuitWindow)
	GemRB.UnloadWindow(TutorialWindow)
	GemRB.SetVar("PlayMode",0) 
	GemRB.SetVar("Slot",1)
	GemRB.LoadGame(-1)
	GemRB.SetNextScript("CharGen")
	return

def Tutorial():
	GemRB.SetVisible(StartWindow,0)
	GemRB.SetVisible(TutorialWindow,1)
	return

def PlayPress():
	GemRB.UnloadWindow(StartWindow)
	GemRB.UnloadWindow(QuitWindow)
	GemRB.UnloadWindow(TutorialWindow)
	GemRB.SetVar("PlayMode",1) #tutorial
	GemRB.SetVar("Slot",1)
	GemRB.LoadGame(-1)
	GemRB.SetNextScript("CharGen")
	return

def CancelTut():
	GemRB.SetVisible(TutorialWindow,0)
	GemRB.SetVisible(StartWindow,1)
	return

def ExitPress():
	GemRB.SetVisible(StartWindow,0)
	GemRB.SetVisible(QuitWindow,1)
	return
	
def ExitConfirmed():
	GemRB.Quit()
	return

def OptionsPress():
#apparently the order is important
	GemRB.UnloadWindow(StartWindow)
	GemRB.UnloadWindow(QuitWindow)
	GemRB.UnloadWindow(TutorialWindow)
	GemRB.SetNextScript("StartOpt")
	return
	
def MoviesPress():
#apparently the order is important
	GemRB.UnloadWindow(StartWindow)
	GemRB.UnloadWindow(QuitWindow)
	GemRB.UnloadWindow(TutorialWindow)
	GemRB.SetNextScript("GUIMOVIE")
	return

def ExitCancelled():
	GemRB.SetVisible(QuitWindow, 0)
	GemRB.SetVisible(StartWindow, 1)
	return
	
def BackToMain():
	GemRB.SetButtonState(StartWindow, SinglePlayerButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonState(StartWindow, OptionsButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonState(StartWindow, MultiPlayerButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetText(StartWindow, SinglePlayerButton, 15413)
	GemRB.SetText(StartWindow, ExitButton, 15417)
	GemRB.SetText(StartWindow, OptionsButton, 13905)
	GemRB.SetText(StartWindow, MultiPlayerButton, 15414)
	GemRB.SetText(StartWindow, MoviesButton, 15415)
	GemRB.SetEvent(StartWindow, SinglePlayerButton, IE_GUI_BUTTON_ON_PRESS, "SinglePlayerPress")
	GemRB.SetEvent(StartWindow, ExitButton, IE_GUI_BUTTON_ON_PRESS, "ExitPress")
	GemRB.SetEvent(StartWindow, OptionsButton, IE_GUI_BUTTON_ON_PRESS, "OptionsPress")
	GemRB.SetEvent(StartWindow, MultiPlayerButton, IE_GUI_BUTTON_ON_PRESS, "MultiPlayerPress")
	GemRB.SetEvent(StartWindow, MoviesButton, IE_GUI_BUTTON_ON_PRESS, "MoviesPress")
	GemRB.SetVisible(QuitWindow, 0)
	GemRB.SetVisible(StartWindow, 1)
	return
