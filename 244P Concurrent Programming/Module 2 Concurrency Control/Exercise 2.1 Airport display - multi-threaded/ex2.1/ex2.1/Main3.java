import java.util.Arrays;
import java.util.Random;
import java.util.concurrent.*;
import java.util.List;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Main3 {

    private static List<String> cityList = List.of(
            "New York", "Los Angeles", "Chicago", "Houston", "Philadelphia",
            "Phoenix", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin",
            "Indianapolis", "Jacksonville", "San Francisco", "Columbus", "Charlotte",
            "Fort Worth", "Detroit", "El Paso", "Memphis", "Seattle", "Denver",
            "Washington", "Boston");

    private static void nap(int millisecs) {
        try {
            Thread.sleep(millisecs);
        } catch (InterruptedException e) {
            System.err.println(e.getMessage());
        }
    }

    private static void addProc(HighLevelDisplay d) {
    // Add a sequence of addRow operations with short random naps.
        try {
            Random randomGen = new Random();
            for (int i = 0; i < 50; i++) {
                String cityName = cityList.get(randomGen.nextInt(cityList.size()));

                d.addRow(cityName + " " + i);

                float randomSeconds = randomGen.nextFloat() * 5; //random number from 0 to 5
                int randomMillis = (int) (randomSeconds * 1000); //convert to milliseconds for Thread.sleep
                Thread.sleep(randomMillis); //you need to provide the function w something to do when interrupted
            }
        } catch (InterruptedException e) {
            System.err.println(e.getMessage());
        }
    }

    private static void deleteProc(HighLevelDisplay d) {
	// Add a sequence of deletions of row 0 with short random naps.
        try {
            Random randomGen = new Random();
            for (int i = 0; i < 50; i++) {

                d.deleteRow(0);

                float randomSeconds = randomGen.nextFloat() * 5; //random number from 0 to 5
                int randomMillis = (int) (randomSeconds * 1000); //convert to milliseconds for Thread.sleep
                Thread.sleep(randomMillis); //you need to provide the function w something to do when interrupted
            }
        } catch (InterruptedException e) {
            System.err.println(e.getMessage());
        }
    }

    public static void main(String [] args) {
	final HighLevelDisplay d = new JDisplay2();

	new Thread () {
	    public void run() {
		addProc(d);
	    }
	}.start();


	new Thread () {
	    public void run() {
		deleteProc(d);
	    }
	}.start();

    }
}