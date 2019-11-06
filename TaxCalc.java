import javax.microedition.midlet.*;
import javax.microedition.lcdui.*;

public class TaxCalc extends MIDlet implements CommandListener {

    private Command exitCommand; // The exit command
    private Display display;     // The display for this MIDlet
    private Command calc;
    private TextField t1,t2;
    private Form form;

    public TaxCalc() {
        display = Display.getDisplay(this);
        exitCommand = new Command("Exit", Command.EXIT,30);
        calc = new Command("Calculate", Command.SCREEN, 1);
        form = new Form("");
        form.addCommand(calc);
        form.addCommand(exitCommand);
        t1 = new TextField("Amount","Enter value",30,TextField.ANY);
        t2 = new TextField("Amount with 18% Tax","Result",30,TextField.ANY);
        form.append(t1);
        form.append(t2);
        form.setCommandListener(this);
      }

    public void startApp() {
        TextBox t = new TextBox("Hello", "Hello, World!", 256, 0);
        display.setCurrent(form);
    }

    public void pauseApp() {
    }

    public void destroyApp(boolean unconditional) {
    }

    public void commandAction(Command c, Displayable s) {
        double sum;

        if (c == exitCommand) {
            destroyApp(false);
            notifyDestroyed();
        }

        if (c==calc)
        {
             double x = Double.parseDouble(("" + t1.getString()));
             double y = (x*18)/(100);
             sum = x+y;
             t2.setString(""+sum);
        }
    }

}
