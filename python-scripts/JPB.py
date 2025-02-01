import N10X

#------------------------------------------------------------------------
def DuplicatePreprocessedLine():
    (x, y) = N10X.Editor.GetCursorPos()
    N10X.Editor.ExecuteCommand("MoveToLineEnd")
    PreprocessedLine = N10X.Editor.GetPreprocessedLine()
    N10X.Editor.InsertText("\r\n" + PreprocessedLine)
    N10X.Editor.SetCursorPos((x, y))

#------------------------------------------------------------------------
MARGIN_SINGLE_COLUMN = "1000"
MARGIN_DUAL_COLUMN = "100"

def ToggleColumn2():
    if N10X.Editor.GetColumnCount() == 1:
        N10X.Editor.SetColumnCount(2)
        N10X.Editor.ExecuteCommand("DuplicatePanelRight")
        N10X.Editor.OverrideSetting("MarginWidth", MARGIN_DUAL_COLUMN)
    else:
        N10X.Editor.SetColumnCount(1)
        N10X.Editor.OverrideSetting("MarginWidth", MARGIN_SINGLE_COLUMN)
        N10X.Editor.CloseFile()

def ToggleColumn2Header():
    if N10X.Editor.GetColumnCount() == 1:
        N10X.Editor.SetColumnCount(2)
        N10X.Editor.ExecuteCommand("CppParser.ToggleSourceHeader")
        N10X.Editor.OverrideSetting("MarginWidth", MARGIN_DUAL_COLUMN)
    else:
        N10X.Editor.SetColumnCount(1)
        N10X.Editor.OverrideSetting("MarginWidth", MARGIN_SINGLE_COLUMN)
        N10X.Editor.CloseFile()
