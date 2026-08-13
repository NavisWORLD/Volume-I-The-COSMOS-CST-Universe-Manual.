from cosmic_memory import RecursiveMemory
m=RecursiveMemory('demo.db',namespace='my-model')
m.remember('My favorite observatory is on the north ridge.',importance=.9)
print(m.context_for('Where is my favorite observatory?'))
m.close()
