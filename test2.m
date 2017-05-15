function [] = test2()



graphics_toolkit gnuplot  #sets option to use gnuplot instead of fltk

x = 1:100;
y = x.^2;
figure(1,"visible","off");
hold on;
plot(x,y);
print -dpng "figure1.jpg";
print('figure1.jpg')


value = 202
data = value;
#save tmp.txt data
