import base64
import ast  # To safely evaluate a string representation of a Python list

# Base64 encoded string (the one you provided)
base64_string = """
W1sxLCA2OV0sIFs2MiwgNDI3OF0sIFs0NCwgNjU1NV0sIFs3OSwgNTUyXSwgWzg2LCAzMzEyXSwgWzMzLCA0NDE2XSwgWzY2LCAyMDddLCBbNjQsIDIyNzddLCBbNjUsIDQ5NjhdLCBbNzIsIDIyMDhdLCBbNTMsIDEzOF0sIFs0MywgMzcyNl0sIFszLCAyMTM5XSwgWzMyLCAxNzI1XSwgWzU0LCAyOTY3XSwgWzkxLCA2Mjc5XSwgWzk1LCAyMjI2MF0sIFs3NSwgMzE1MDBdLCBbNDMsIDIyNjgwXSwgWzExLCAyMDU4MF0sIFs2NiwgMTI2MF0sIFs4OCwgMzc4MF0sIFsxOCwgMzczODBdLCBbMjQsIDMwNjYwXSwgWzMzLCAyNjg4MF0sIFszLCAxMzAyMF0sIFs4NiwgMjAxNjBdLCBbODYsIDIwMTYwXSwgWzQ0LCAzOTkwMF0sIFs4OCwgMzc4MF0sIFs5NSwgMjIyNjBdLCBbNTMsIDg0MF0sIFsyNCwgMzA2NjBdLCBbMTYsIDY3MjBdLCBbOSwgMzY5NjBdLCBbODUsIDExMzQwXSwgWzgsIDc1NjBdLCBbMjUsIDI3MzAwXSwgWzUwLCAxOTc0MF0sIFs4NSwgMTEzNDBdLCBbNjIsIDI2MDQwXSwgWzg4LCAzNzgwXSwgWzc5LCAzMzYwXSwgWzUzLCA4NDBdLCBbNTMsIDg0MF0sIFsxOCwgMzczODBdLCBbNCwgMzkwNjBdLCBbOTQsIDI3NzIwXSwgWzE2LCA2NzIwXSwgWzIsIDE4NDgwXSwgWzg4LCAzNzgwXSwgWzIyLCA5MjQwXSwgWzE4LCAzNzM4MF0sIFsyMiwgOTI0MF0sIFsxMSwgMjA1ODBdLCBbMTEsIDIwNTgwXSwgWzMsIDEzMDIwXSwgWzg4LCAzNzgwXSwgWzg4LCAzNzgwXSwgWzQzLCAyMjY4MF0sIFs3MiwgMTM0NDBdLCBbMzIsIDEwNTAwXSwgWzQ4LCA0NjIwXSwgWzM1LCAxNDcwMF0sIFs4LCA3NTYwXSwgWzc5LCAzMzYwXSwgWzUwLCAxOTc0MF0sIFsyMiwgOTI0MF0sIFs4OCwgMzc4MF0sIFs4LCA3NTYwXSwgWzUzLCA4NDBdLCBbMiwgMTg0ODBdLCBbODEsIDM0MDIwXSwgWzQ0LCAzOTkwMF0sIFs2MSwgMjU2MjBdLCBbMjIsIDkyNDBdLCBbMjUsIDI3MzAwXSwgWzMyLCAxMDUwMF0sIFs4MSwgMzQwMjBdLCBbNCwgMzkwNjBdLCBbNjUsIDMwMjQwXSwgWzcwLCAzNTcwMF0sIFs5NiwgNDAzMjBdLCBbNDMsIDIyNjgwXSwgWzgsIDc1NjBdLCBbNCwgMzkwNjBdLCBbNTQsIDE4MDYwXSwgWzEyLCAyOTQwMF0sIFs1MywgODQwXSwgWzMsIDEzMDIwXSwgWzUzLCA4NDBdLCBbNjYsIDEyNjBdLCBbODYsIDIwMTYwXSwgWzMzLCAyNjg4MF0sIFs5MywgMTY4MF0sIFs1MCwgMTk3NDBdLCBbMjIsIDkyNDBdLCBbOCwgNzU2MF0sIFszNiwgMTUxMjBdLCBbNTQsIDE4MDYwXV0==
"""

# Decode the Base64 string
decoded_bytes = base64.b64decode(base64_string)

# Convert the decoded bytes to a string (assumed to be a valid Python list in string form)
decoded_string = decoded_bytes.decode('utf-8')

# Convert the string to an actual Python list using ast.literal_eval for safety
# `literal_eval` will safely evaluate the string as a Python literal expression
li = ast.literal_eval(decoded_string)

# Now, let's print the result
print(li)  # This will print the list structure

# If you need to check the length of the list or access an item at a specific index
print(len(li))  # Prints the length of the list
print(li[15])  # Access the item at index 63
