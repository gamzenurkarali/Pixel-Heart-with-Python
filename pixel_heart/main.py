import turtle 
import pixel_art 
import time
turtle.bgcolor('whitesmoke')#python turtle graphics penceresinin arkaplan rengini ayarlar

#ızgara çizen fonksiyon
#pixel_art.draw_grid()
#eksenleri çizen fonksiyon
#pixel_art.draw_axis()

time.sleep(3)#python turtle graphics açıldıktan sonra kalbi çizmesi için parametre kadar bekler

#kutucuklar için koordinatlar ve kutunun dolgu rengini ayarlama
pixel_art.pixel(1,-2,'black')
pixel_art.pixel(2,-1,'black')
pixel_art.pixel(3,1,'black')
pixel_art.pixel(4,2,'black')
pixel_art.pixel(5,3,'black')
pixel_art.pixel(5,4,'black')
pixel_art.pixel(5,5,'black')
pixel_art.pixel(4,6,'black')
pixel_art.pixel(3,7,'black')
pixel_art.pixel(2,6,'black')
pixel_art.pixel(1,5,'black')
pixel_art.pixel(-1,6,'black')
pixel_art.pixel(-2,7,'black')
pixel_art.pixel(-3,6,'black')
pixel_art.pixel(-4,5,'black')
pixel_art.pixel(-4,4,'black')
pixel_art.pixel(-4,3,'black')
pixel_art.pixel(-3,2,'black')
pixel_art.pixel(-2,1,'black')
pixel_art.pixel(-1,-1,'black')

pixel_art.pixel(1,-1,'red')
pixel_art.pixel(2,1,'red')
pixel_art.pixel(3,2,'red')
pixel_art.pixel(4,3,'red')
pixel_art.pixel(4,4,'red')
pixel_art.pixel(4,5,'red')
pixel_art.pixel(3,6,'red')
pixel_art.pixel(2,5,'red')
pixel_art.pixel(1,4,'red')
pixel_art.pixel(-1,5,'red')
pixel_art.pixel(-2,6,'red')
pixel_art.pixel(-3,5,'red')
pixel_art.pixel(-3,4,'red')
pixel_art.pixel(-3,3,'red')
pixel_art.pixel(-2,2,'red')
pixel_art.pixel(-1,1,'red')
pixel_art.pixel(1,1,'red')
pixel_art.pixel(2,2,'red')
pixel_art.pixel(3,3,'white')
pixel_art.pixel(3,4,'white')
pixel_art.pixel(3,5,'red')
pixel_art.pixel(2,4,'white')
pixel_art.pixel(1,3,'red')
pixel_art.pixel(-1,4,'red')
pixel_art.pixel(-2,5,'red')
pixel_art.pixel(-2,4,'red')
pixel_art.pixel(-2,3,'red')
pixel_art.pixel(-1,2,'red')
pixel_art.pixel(1,2,'red')
pixel_art.pixel(2,3,'red')
pixel_art.pixel(-1,3,'red')

turtle.Screen().exitonclick()#python turtle graphics penceresinin işlem tamamlandıktan sonra direkt kapanmasını önler