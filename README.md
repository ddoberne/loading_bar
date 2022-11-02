# loading_bar

Simple loading bar code.

For a loading bar out of 1000 iterations:

~~~
import loading_bar
lb = loading_bar.LoadingBar(1000)

for i in range(1000):
  ### Do something
  lb.display()
~~~
