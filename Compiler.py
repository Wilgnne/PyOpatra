def split_block (string:str, seps:(str, str)) -> str:
    _, content = string.split (seps[0])
    block, _ = content.split (seps[1])
    return block

def is_not_empty (value):
    return value != ''

def contens_colons (value:str) -> bool:
    return value.count(":") == 0

content = ""

with open ("examples/add.asm") as f:
    content = f.read()

code, data = [*map (lambda x: split_block (content, x), [(".code", ".endcode"), (".data", ".enddata")])]

code = [*filter (is_not_empty, code.split ('\n'))]
data = [*filter (is_not_empty, data.split ('\n'))]
print (code)
print (data)

instructions = [*filter (contens_colons, code)]
markings = [*filter (lambda x: not contens_colons (x), code)]

there_is_instruction = [*map ( lambda x: len (x.split (":")[1].replace (" ", "")) != 0, markings)]

print (instructions)
print (markings)

print (there_is_instruction)