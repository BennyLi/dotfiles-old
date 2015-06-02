#!/c/dev/GitTools/Python27/python

import os
import sys


boxFormatFull = '+-{:-^70}-+'
boxFormat = '| {:<70} |'

def sortFirstLast(elems):
  elemsCopy = elems[:]
  elemsCopy.reverse();
  return customSort(elemsCopy, elemsCopy.pop())

def sortLastFirst(elems):
  elemsCopy = elems[:]
  return customSort(elemsCopy, elemsCopy.pop())

def customSort(elems, elem):
  if len(elems) == 0:
    return [elem]
  elems.reverse()
  return [elem] + customSort(elems, elems.pop())

def flatten(elems):
  try:
    it = iter(elems)
  except TypeError:
    yield elems
  else:
    for elem in it:
      for flatElem in flatten(elem):
        yield flatElem

# Blank line on first
print ''

if len(sys.argv) != 2:
  print 'You have to give me the number of pages to print! Usage:'
  print '  python " + os.path.basename(__file__) + " <NumberOfPages>'
  sys.exit()

try:
  numberOfPages = int(sys.argv[1])
except ValueError:
  print '<NumberOfPages> must be an integer!'
  sys.exit()

if (numberOfPages % 2 != 0):
  print boxFormatFull.format(' W A R N I N G ! ')
  print boxFormat.format('Your document has {0} pages.'.format(numberOfPages))
  print boxFormat.format('For a proper book print it should have {0} pages.'.format(numberOfPages+1))
  print boxFormat.format('!! PLEASE add a (blank) page to your document !!')
  print boxFormat.format('')
  print boxFormat.format('Will proceed with {0} pages as argument...'.format(numberOfPages+1))
  print boxFormatFull.format('')
  print ''
  numberOfPages += 1
  raw_input('Press enter to continue...')
  print ''

if (numberOfPages / 2 % 2 != 0):
  print boxFormatFull.format(' W A R N I N G ! ')
  print boxFormat.format('Your document has {0} pages.'.format(numberOfPages))
  print boxFormat.format('Dived by 2 this give an odd number: {0}'.format(numberOfPages / 2))
  print boxFormat.format('If you print in duplex mode this will result in a blank page in the')
  print boxFormat.format('middle of the document!')
  print boxFormat.format('')
  print boxFormat.format('!! PLEASE add two pages to the end of your document to prevent this !!')
  print boxFormatFull.format('')
  print ''
  raw_input('Press enter to continue...')
  print ''

allPages = range(1, numberOfPages + 1)
evenPages = [even for even in allPages if even % 2 == 0]
oddPages = [odd for odd in allPages if odd % 2 != 0]

evenPagesSorted = sortLastFirst(evenPages)
oddPagesSorted = sortFirstLast(oddPages)

zipped = zip(evenPagesSorted, oddPagesSorted)

joinedStr = ';'.join(str(elem) for elem in list(flatten(zipped)))

print 'Add the following as "Pages" to your print screen:'
print joinedStr
