# 10X-Settings
Custom color theme, settings, and keybindings for the 10X editor.


Keybindings:
<ul>
<li>[Ctrl] + [2] : Open/close current file in pane to the right.</li>
<li>[Ctrl] + [Shift] + [2] : Open/close the counterpart file to the current file in a pane to the right.</li>
<li>[Ctrl] + [Shift] + [P] : Insert a preporcessed output of a currently selected macro call.</li>
</ul>

Python functions:
<ul>
<li> **DuplicatePreprocessedLine()** : this will take a line from a C macro and write out the parsed line underneath. This helps with complex macros to see synax highlighting, arguments, and parenthsis balance.</li>
<li>**ToggleColumn2()** : when in single-pane mode, this will open a second pane to the right with the current file.</li>
<li>**ToggleColumn2Header()** : when in single-pane mode, this will open the counterpart file in a new pane to the right.</li>
</ul>

Settings:
The settings file includes various customizations, including the use of RobotoMono font, and a margin for single pane on my 4K+ 3:2 monitor.
Unfortunately, I haven't yet found a way to dymamically set the margin when a column width changes, such as when in dual-pane mode.

QuadTone2:
<img width="1920" alt="quadtone2_single_pane_preview" src="https://github.com/user-attachments/assets/119eff79-79ab-44a2-bb9c-23eb86784cb7" />
<img width="1920" alt="quadtone2_dual_pane_preview" src="https://github.com/user-attachments/assets/475dea81-23e4-431c-bd09-e919d4f0c1cb" />
