import java.applet.Applet;
import java.awt.Graphics;
/*
<applet code="HelloWorld3.class" width="500" height="500">
</applet>
*/

public class HelloWorld3 extends Applet {
    public void paint(Graphics g) {
        g.drawString("Hello world!", 50, 25);
    }
}