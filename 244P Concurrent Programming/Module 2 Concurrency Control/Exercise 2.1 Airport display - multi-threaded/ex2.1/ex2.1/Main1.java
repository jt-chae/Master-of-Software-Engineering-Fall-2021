public class Main1 {

    private static void nap(int millisecs) {
        try {
	    Thread.sleep(millisecs);
	} catch (InterruptedException e) {
	    System.err.println(e.getMessage());
	}
    }


    public static void main(String [] args) {

	HWDisplay d = new JDisplay(); //creating a display

        d.write(5,2,'A'); //write letter 'A' to row 5 column 2
        d.write(8,11,'B');
        nap(3000);
	d.write(5,2,' ');

    }
}