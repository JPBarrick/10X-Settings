# 10X-Settings
Custom color themes for the [C language](https://en.wikipedia.org/wiki/C_(programming_language)), misc. settings, Python scripts, and keybindings for the [10X Editor](https://10xeditor.com).
<br>Improved support for C++ specifics will be added later.
<br>\- *Contributions are welcome to better support languages other than C.*

**BE SURE TO READ ALL OF THE INFO. BELOW.**

🎨 Themes:
- ```QuadTone``` : A theme which limits the syntax highlighting tones (i.e. not a fruit salad bowl). Only tested with **.c**, **.h**, and **.py** files.
- ```QuadTone2``` : A more refined theme which is designed for a focus/zen like mode. Only tested with **.c**, **.h**, and **.py** files.. *(Preview screens below)*

⌨ Keybindings:

- ```[Ctrl] + [2] ``` : Open/close current file in pane to the right.
- ```[Ctrl] + [Shift] + [2]``` : Open/close the counterpart file to the current file in a pane to the right.
- ```[Ctrl] + [Shift] + [P]``` : Insert a preporcessed output of a currently selected macro call.

---

🧾 Python functions:

- ```DuplicatePreprocessedLine()``` : This will take a line from a C macro and write out the parsed line underneath. This helps with complex macros to see synax highlighting, arguments, and parenthsis balance.
- ```ToggleColumn2()``` : When in single-pane mode, this will open a second pane to the right with the current file with the code centered.
- ```ToggleColumn2Header()``` : When in single-pane mode, this will open the counterpart file in a new pane to the right with the code centered.
  
   The constants: `MARGIN_SINGLE_COLUMN_RATIO` and `MARGIN_DUAL_COLUMN_RATIO` can be modified to better fit your display or personal preference for the margin adjustments between modes.

---

⚙️ Settings:

The settings files include keybindsing and preferences for aspects of the 10X GUI. 

---

:floppy_disk: Installation *(be sure to backup your existing files first)*:

Begin by applying just the QuadTone2 theme before continuing with settings and Python scripts.
- Copy the theme files to ```%HOMEDRIVE%%HOMEPATH%\AppData\Roaming\10x\Settings\ColorSchemes```
- Copy the Python script(s) to ```%HOMEDRIVE%%HOMEPATH%\AppData\Roaming\10x\PythonScripts```
- Install the ***Roboto Mono Light*** font.
- **Option 1**:
  - Add the add/replace the following into your files:
    - ***Settings.10x_settings***
      - `EditorFont:` RobotoMono Nerd Font Light
      - `EditorFontSize:` 10
      - `StatusBarFontSize:` 12
    - ***KeyMappings.10x_settings***
      - `Control 2:`				   ToggleColumn2
      - `Control Shift 2:`		   ToggleColumn2Header
      - `Control Shift P:`	       DuplicatePreprocessedLine
- **Option 2**
  - Or copy the setting files to ```%HOMEDRIVE%%HOMEPATH%\AppData\Roaming\10x\Settings```
  


---

**QuadTone2** focus/zen single-pane theme preview *(4K plus 3:2 display)*:
<img width="1920" alt="quadtone2_single_pane_preview" src="https://github.com/user-attachments/assets/119eff79-79ab-44a2-bb9c-23eb86784cb7" />

**QuadTone2** focus/zen dual-pane theme preview *(4K plus 3:2 display)*:
<img width="1920" alt="quadtone2_dual_pane_preview" src="https://github.com/user-attachments/assets/475dea81-23e4-431c-bd09-e919d4f0c1cb" />

---

**QuadTone** single-pane theme preview *(4K plus 3:2 display)*:
<img width="1920" alt="quadtone_single_pane_preview" src="https://github.com/user-attachments/assets/5b07995a-7590-468c-ba4e-df863c9e16a1" />

**QuadTone** dual-pane theme preview *(4K plus 3:2 display)*:
<img width="1920" alt="quadtone_dual_pane_preview" src="https://github.com/user-attachments/assets/00485a59-bc7d-4a52-b740-78b60a51e6dc" />

**Notes:** Both themes are not fully complete, as they are covering only the features I use. Contribution are welcome... just make a pull request for review. Neither theme modifies the Workspace Tree (yet). The colors and contrast I see will be different to what you see, because I use a custom color profile on my operating system. 
