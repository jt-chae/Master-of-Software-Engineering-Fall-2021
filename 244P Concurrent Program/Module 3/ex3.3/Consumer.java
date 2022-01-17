import java.util.concurrent.ArrayBlockingQueue;

public class Consumer implements Runnable {
    private ArrayBlockingQueue queue;
    private int id;

    public Consumer(ArrayBlockingQueue q, int n) { //pass the ArrayBlockingQueue q to the thread as an args
	queue = q;
	id = n;
    }
    
    public void run() {
	Message msg = null;
	int count = 0;
	do {
	    try {
			msg = (Message) queue.take(); // Get a message from the queue with queue.get()
			count++;
			RandomUtils.print("Consumed " + msg.get(), id);
			Thread.sleep(RandomUtils.randomInteger());
	    } catch (InterruptedException e) {
			e.printStackTrace();
	    }
	} while (msg.get() != "stop");
	// Don't count the "stop" message
	count--;
	//Add this line, after the consumer stops, add another stop message to the queue
	queue.offer(new Message("stop"));
	RandomUtils.print("Messages received: " + count, id);
    }
}
