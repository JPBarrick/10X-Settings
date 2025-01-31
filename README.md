# 10X-Settings
Custom color theme, settings, and keybindings for the [10X Editor](https://10xeditor.com).

⌨ Keybindings:

- ```[Ctrl] + [2] ``` : Open/close current file in pane to the right.
- ```[Ctrl] + [Shift] + [2]``` : Open/close the counterpart file to the current file in a pane to the right.
- ```[Ctrl] + [Shift] + [P]``` : Insert a preporcessed output of a currently selected macro call.

---

🧾 Python functions:

- ```DuplicatePreprocessedLine()``` : this will take a line from a C macro and write out the parsed line underneath. This helps with complex macros to see synax highlighting, arguments, and parenthsis balance.
- ```ToggleColumn2()``` : when in single-pane mode, this will open a second pane to the right with the current file.
- ```ToggleColumn2Header()``` : when in single-pane mode, this will open the counterpart file in a new pane to the right.

---

⚙️ Settings:

The settings file includes various customizations, including the use of RobotoMono font, and a margin for single pane on my 4K+ 3:2 monitor.
Unfortunately, I haven't yet found a way to dymamically set the margin when a column width changes, such as when in dual-pane mode.

---

QuadTone2 single-pane theme preview *(4K plus 3:2 display)*:

<img width="1920" alt="quadtone2_single_pane_preview" src="https://github.com/user-attachments/assets/119eff79-79ab-44a2-bb9c-23eb86784cb7" />

QuadTone2 dual-pane theme preview *(4K plus 3:2 display)*:
<img width="1920" alt="quadtone2_dual_pane_preview" src="https://github.com/user-attachments/assets/475dea81-23e4-431c-bd09-e919d4f0c1cb" />
