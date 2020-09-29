round(1215,-1) #1220

#floating sum error 
a = 0.1
b = 0.2
c = a + b
c*10000


#formatting
x = 1234.56789
# Two decimal places of accuracy 
format(x, '0.2f') #'1234.57'
# Right justified in 10 chars, one-digit accuracy 
format(x, '>10.1f')#' 1234.6'
# Left justified 
format(x, '<10.1f') #'1234.6 '
# Centered
format(x, '^10.1f') #' 1234.6 '
# Inclusion of thousands separator f
format(x, ',') #'1,234.56789'
format(x, '0,.1f')


'%0.2f' % x