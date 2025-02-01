import N10X

#------------------------------------------------------------------------ Show parsed macro
def DuplicatePreprocessedLine():
    (x, y) = N10X.Editor.GetCursorPos()
    N10X.Editor.ExecuteCommand("MoveToLineEnd")
    PreprocessedLine = N10X.Editor.GetPreprocessedLine()
    N10X.Editor.InsertText("\r\n" + PreprocessedLine)
    N10X.Editor.SetCursorPos((x, y))

#------------------------------------------------------------------------ Toggle single or dual panes
# Heuristic for margins thanks for .daniel.w on 10X Editor Discord server.
# Modify the following two ratios for your display resolution:
MARGIN_SINGLE_COLUMN_RATIO = 0.26
MARGIN_DUAL_COLUMN_RATIO = 0.026
WindowWidth = 3840

def OnWorkspaceOpened():
    WindowSize = N10X.Editor.GetWindowRect()
    Left = WindowSize[0]
    Right = WindowSize[2]
    WindowWidth = Right - Left

def CalculatePaneMargins(NumPanes=1):
    """
    Calculate margins for 1 or 2 panes based on window width
    Returns target width for each pane
    """
    WindowSize = N10X.Editor.GetWindowRect()
    WindowWidth = WindowSize[2] - WindowSize[0]

    if NumPanes == 1:
        MarginWidth = int(WindowWidth * MARGIN_SINGLE_COLUMN_RATIO)
        print(f"Setting editor margins to {MarginWidth}")
        return MarginWidth
    else:
        MarginWidth = int(WindowWidth * MARGIN_DUAL_COLUMN_RATIO)
        print(f"Setting editor margins to {MarginWidth}")
        return MarginWidth

def ToggleColumn2():
    if N10X.Editor.GetColumnCount() == 1:
        N10X.Editor.SetColumnCount(2)
        N10X.Editor.ExecuteCommand("DuplicatePanelRight")
        N10X.Editor.OverrideSetting("MarginWidth", str(CalculatePaneMargins(2)))
    else:
        N10X.Editor.SetColumnCount(1)
        N10X.Editor.OverrideSetting("MarginWidth", str(CalculatePaneMargins(1)))
        N10X.Editor.CloseFile()

def ToggleColumn2Header():
    if N10X.Editor.GetColumnCount() == 1:
        N10X.Editor.SetColumnCount(2)
        N10X.Editor.ExecuteCommand("CppParser.ToggleSourceHeader")
        N10X.Editor.OverrideSetting("MarginWidth", str(CalculatePaneMargins(2)))
    else:
        N10X.Editor.SetColumnCount(1)
        N10X.Editor.OverrideSetting("MarginWidth", str(CalculatePaneMargins(1)))
        N10X.Editor.CloseFile()
