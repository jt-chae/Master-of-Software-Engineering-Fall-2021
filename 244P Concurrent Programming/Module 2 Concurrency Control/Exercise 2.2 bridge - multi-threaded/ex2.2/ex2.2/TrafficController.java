public class TrafficController {

    private boolean bridgeIsBusy = false; //variable to keep track if the bridge is in use

    public synchronized void enterLeft() { //function for the left car, "synchronized" means one function
        // cannot start before one is finished
        while (bridgeIsBusy) { //if bridge is busy, call the function wait()
            try { //calling wait() forces the current thread to wait until some
                // other thread invokes notify() or notifyAll() on the same object.
                wait();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.err.println("EnterLeft interrupted " + e.getMessage());
            }
        }
        bridgeIsBusy = true;
    }
    public synchronized void enterRight() {
        while (bridgeIsBusy) {
            try {
                wait();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.err.println("EnterRight interrupted " + e.getMessage());
            }
        }
        bridgeIsBusy = true;
    }
    public synchronized void leaveLeft() { //when the car leaves the bridge on one side
        bridgeIsBusy = false; //set the variable to false
        notifyAll(); //invoke this on the object to tell the other thread to stop waiting
    }
    public synchronized void leaveRight() {
        bridgeIsBusy = false;
        notifyAll();
    }

}
//reference: https://www.baeldung.com/java-wait-notify