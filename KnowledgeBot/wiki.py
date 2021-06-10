import wikipedia as wiki
import wikipediaapi

print(wiki.search('Bangla'))
wikiapi = wikipediaapi.Wikipedia('en')
page_py = wikiapi.page('Bangla')
print("Page - Exists: %s" % page_py.exists())
print("Page - Summary: %s" % page_py.summary)
# print(type(z))
# if z==True:
#     print('yes')
# else:
#     print('no')
# z= z.split('.')
# z= z[:5]
# z= ".".join(z)
# print(type(z))
# print(z)
# print(type(z))

# print(wiki.search("barrak"))