import json
data = '{ "glossary": { "title": "example glossary", "GlossDiv": { "title": "S", "GlossList": { "GlossEntry": { "ID": "SGML", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language", "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": { "para": "A meta-markup language, used to create markup languages such as DocBook.", "GlossSeeAlso": ["GML", "XML"] }, "GlossSee": "markup" } } } } }'

lst = [1,[4,6,3],[93,89,'fdf'],[743,35.6,36]]
dic = {
"user":{
"name":"Rejaul Karin",
"password": "792jf",
"body":{
"height":5.9,
'eye' : 'Black'
}
}
}

for items in lst:
    print('Level 1:')
    if type(items) is list:
        for item in items:
            print("    ",item)
    else:
        print("    ",items)
