import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.ConnectException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class UDPClient {
    static final int PORT_NUMBER = 6868; //initialize the port number
    static final int BUFFER_SIZE = 1000;
    static final String HOST_NAME = "localhost";
    static final int TIME_OUT = 1000000;

        public static void main(String[] args) {
            DatagramSocket socket = null;
            try {
                byte[] buf = new byte[BUFFER_SIZE];
                InetAddress inetAdd = InetAddress.getByName(HOST_NAME);
                int arb_port = 0 + (int) (Math.random() * (8000));

                socket = new DatagramSocket(arb_port, inetAdd);
                System.out.println("Socket at port " + socket.getLocalPort());
                socket.setSoTimeout(TIME_OUT);
                DatagramPacket packet = new DatagramPacket(buf, BUFFER_SIZE, inetAdd, PORT_NUMBER);
                BufferedReader keyboardIn = new BufferedReader(new InputStreamReader(System.in));// from keyboard

                while (true) {
                    System.out.print("Please enter your input: ");
                    String userInput = keyboardIn.readLine();
                    if (userInput.equals("index") || userInput.startsWith("get ")) {
                        packet.setData(userInput.getBytes(), 0, userInput.getBytes().length);
                        socket.send(packet);
                        packet.setData(buf, 0, buf.length); //reset
                        socket.receive(packet);

                        int packetCount = 1;
                        //int receiveSize = 0;

                        StringBuilder message_builder = new StringBuilder();

                        if (userInput.equals("index")) {
                            System.out.println("List of files in server directory:");
                            String response = new String(buf);
                            response = response.replace("\0", "");
                            message_builder.append(response);
                        } else {
                            while ((packet.getLength()) != 0) {
                                //while ((receiveSize = packet.getLength()) != 0) {
                                // if exit signal is received
                                String response = new String(buf);
                                response = response.replace("\0", "");
                                if (response.equals("exit")) {
                                    System.out.println("End");
                                    packet.setData("exit".getBytes(), 0, "exit".getBytes().length);
                                    socket.send(packet);
                                    break;
                                }
                                message_builder.append(response);
                                packet.setData("succ".getBytes(), 0, "succ".getBytes().length);
                                socket.send(packet);
                                buf = new byte[BUFFER_SIZE];
                                packet.setData(buf, 0, buf.length);
                                System.out.println("# " + (packetCount++) + " packet received successfully.");
                                socket.receive(packet);
                            }
                        }
                        message_builder.append("\n");
                        String res = message_builder.toString();
                        System.out.print(res);

                        if (userInput.startsWith("get ") && !res.startsWith("error")) {
                            break;
                        }
                    } else {
                        System.err.println("Invalid command.");
                    }
                }
            } catch (ConnectException e) {
                System.err.println("Timeout.");
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                try {
                    if (socket != null)
                        socket.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }

    //reference: https://github.com/Zeyuuuuuu/UCI-MSWE-FALL2019/tree/master/242P/ex3