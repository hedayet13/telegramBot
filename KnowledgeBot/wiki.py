import wikipedia as wiki

z=wiki.summary("atn bangla")
if type(z)==str:
    print('yes')
else:
    print('no')
# z= z.split('.')
# z= z[:5]
# z= ".".join(z)
print(type(z))
print(z)
# print(type(z))

# print(wiki.search("barrak"))