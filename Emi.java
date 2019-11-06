import javax.microedition.midlet.*;
import javax.microedition.lcdui.*;

public class Emi extends MIDlet implements CommandListener {

	private Command exit;
	private Command calculate;
	private Display display;
	private TextField princi,rate,year,ans;
	private Form form;	

	public Emi(){
	
		display = Display.getDisplay(this);
		exit = new Command("Exit",Command.EXIT,30);
	
	calculate = new Command("Calculate",Command.SCREEN,1);	

		form = new Form("");

		form.addCommand(calculate);
		form.addCommand(exit);

		princi = new TextField("Principle","",50,TextField.ANY);
		rate = new TextField("Rate of Interest","",50,TextField.ANY);
		year = new TextField("Duration","",50,TextField.ANY);
		ans = new TextField("EMI","",50,TextField.ANY);		
		form.append(princi);
		form.append(rate);
		form.append(year);
		form.append(ans);

        form.setCommandListener(this);
	
	}

	public void startApp(){
		display.setCurrent(form);
	}


	public void pauseApp(){
	}

	public void destroyApp(boolean unconditional){

	}
	
	public double pow(double a  ,double b){
	
	double ans = 1;
	
	while( b > 0 ){
	
        ans *= a;
        b -= 1;
	
	}
	
	return ans;
	
	}


	public void commandAction(Command c , Displayable s ){
		double emi;

		if (c == exit){
			destroyApp(false);
			notifyDestroyed();		
		}

		if(c == calculate){
			
			double p = Double.parseDouble((""+princi.getString()));
			double r = Double.parseDouble((""+rate.getString()));
			double y = Double.parseDouble((""+year.getString()));
			
			//Rate of Interest Per Month we want
			r = r/12; 

			double t1 =  p*r*( pow(1+r , y ) )  ;
			double t2 = pow(1+r , y ) - 1 ;

			emi = t1 / t2;
			
			ans.setString(""+emi);
		}
	}


}

