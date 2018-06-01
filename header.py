#module to print required header
def printHeader (g):
    with open(g, 'w') as the_file:
        the_file.write('0 HEAD\n')
        the_file.write('1 SOUR 0\n')
        the_file.write('1 SUBM @U@\n')
        the_file.write('1 GEDC\n')
        the_file.write('2 VERS 5.5.1\n')
        the_file.write('2 FORM LINEAGE-LINKED\n')
        the_file.write('1 CHAR UTF-8\n')
        the_file.write('0 @U@ SUBM\n')
        the_file.write('1 NAME X\n')
