figure = 1
sum_of_figures = 0
square = 0
sum_of_squares = 0
while 1==1:
    figure = int(input())
    sum_of_figures += figure
    square = figure ** 2
    sum_of_squares += square
    if sum_of_figures == 0:
        print (sum_of_squares)
        break
