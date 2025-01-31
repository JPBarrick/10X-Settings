import N10X

#------------------------------------------------------------------------
def DuplicatePreprocessedLine():
    (x, y) = N10X.Editor.GetCursorPos()
    N10X.Editor.ExecuteCommand("MoveToLineEnd")
    PreprocessedLine = N10X.Editor.GetPreprocessedLine()
    N10X.Editor.InsertText("\r\n" + PreprocessedLine)
    N10X.Editor.SetCursorPos((x, y))

#------------------------------------------------------------------------
def ToggleColumn2():
    if N10X.Editor.GetColumnCount() == 1:
        N10X.Editor.SetColumnCount(2)
        N10X.Editor.ExecuteCommand("DuplicatePanelRight")
    else:
        N10X.Editor.SetColumnCount(1)
        N10X.Editor.CloseFile()

def ToggleColumn2Header():
    if N10X.Editor.GetColumnCount() == 1:
        N10X.Editor.SetColumnCount(2)
        N10X.Editor.ExecuteCommand("CppParser.ToggleSourceHeader")
    else:
        N10X.Editor.SetColumnCount(1)
        N10X.Editor.CloseFile()
