#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_abacus(value):
       #
       # ## Add you code here 
       #
       i = len(str(value))
       sv = str(value)
       j = 10 - i
       n = 10 - j
       x = 0
       while j > 0:
           print "|00000*****   |"
           j = j - 1
       while x < n:
           num = int(sv[x])
           drawLine(num)
           x = x + 1
           
       
           
def drawLine(n):
    if n == 0:
        print "|00000*****   |" 
    if n == 1:
        print "|00000****   *|"
    if n == 2:
        print "|00000***   **|"
    if n == 3:
        print "|00000**   ***|"
    if n == 4:
        print "|00000*   ****|"
    if n == 5:
        print "|00000   *****|"
    if n == 6:
        print "|0000   0*****|"
    if n == 7:
        print "|000   00*****|"
    if n == 8:
        print "|00   000*****|"
    if n == 9:
        print "|0   0000*****|"
            
       
       

# ##  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
# >>>|00000*****   |
# >>>|00000*****   |
# >>>|00000*****   |
# >>>|00000*****   |
# >>>|00000*****   |
# >>>|00000*****   |
# >>>|00000*****   |
# >>>|00000*****   |
# >>>|00000*****   |
# >>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
# >>>|00000*****   |
# >>>|00000*****   |
# >>>|00000****   *|
# >>>|00000***   **|
# >>>|00000**   ***|
# >>>|00000*   ****|
# >>>|00000   *****|
# >>>|0000   0*****|
# >>>|000   00*****|
# >>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
# >>>|00000*****   |
# >>>|00000*****   |
# >>>|00000*****   |
# >>>|00000*****   |
# >>>|00000*****   |
# >>>|00000*****   |
# >>>|00000****   *|
# >>>|00000**   ***|
# >>>|00000**   ***|
# >>>|000   00*****|
