Trim Whitespace
=========

Sets user preference `trim_trailing_white_space_on_save` to true or false.

Installation
------------

1. Using Package Control, install "TrimWhitespace"

Or:

1. Open the Sublime Text Packages folder
    - OS X: ~/Library/Application Support/Sublime Text 3/Packages/
    - Windows: %APPDATA%/Sublime Text 3/Packages/
    - Linux: ~/.Sublime Text 3/Packages/ or ~/.config/sublime-text-3/Packages

2. clone this repo
3. Install keymaps for the commands (see Example.sublime-keymap for my preferred keys)

Commands
--------

    {
        "caption": "Trim whitespace: true/false",
        "command": "trim_whitespace",
        "args": {"value": true/false}
    }
