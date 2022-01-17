import java.io.IOException;
import java.io.RandomAccessFile;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;


public class UDPServer {
    static final int PORT_NUMBER = 6868;
    static final int BUFFER_SIZE = 1024;
    static final String HOST_NAME = "localhost";
    static final int TIME_OUT = 1000000;

    private static DatagramSocket socket = null;
    private static String folderPathString = "";
    private static Path folderPath = null;

    private static class Task implements Callable<Void> {

        private DatagramPacket packet;
        private byte[] buf; //to break into smaller chunks
        private byte[] signalBuf; //to break into smaller chunks
        private RandomAccessFile file;
        private String host_name;

        Task(DatagramPacket packet, byte[] buf) {
            this.packet = packet;
            this.buf = buf;
            this.signalBuf = new byte[7]; //break data into smaller chunks
            this.host_name = this.packet.getAddress().getHostAddress() + ":" + this.packet.getPort();
        }

        public Void call() throws Exception {
            Thread.currentThread().setPriority(10);

            try {
                String userInput = new String(buf);
                userInput = userInput.replace("\0", "");
                System.out.println("Input received: " + userInput + " from " + host_name);
                if (userInput.equals("index")) {
                    StringBuilder message_builder = new StringBuilder();
                    //message_builder.append("Folder Path: " + folderPath.toAbsolutePath().toString() + "\n");
                    try (DirectoryStream<Path> stream = Files.newDirectoryStream(folderPath)) {
                        for (Path p : stream) {
                            message_builder.append(p.getFileName() + "\n");
                        }
                        String message = message_builder.toString();
                        System.out.print(message);
                        packet.setData(message.getBytes(), 0, message.getBytes().length);
                        socket.send(packet);

                    } catch (IOException e) {
                        System.err.println("Invalid folder path.");
                        e.printStackTrace();
                    }
                } else if (userInput.startsWith("get ")) {
                    String filePathString = userInput.split(" ")[1];
                    Path filePath = Paths.get(folderPathString + "/" + filePathString);
                    if (Files.notExists(filePath)) {
                        packet.setData("error\nInvalid file name.".getBytes(), 0,
                                "error\nInvalid file name.".getBytes().length);
                        socket.send(packet);
                        System.err.println("Invalid file name.");
                    } else {
                        file = new RandomAccessFile(folderPathString + "/" + filePathString, "r");

                        int packetCount = 1;
                        int fileSize;

                        while ((fileSize = file.read(buf)) != -1) {
                            packet.setData(buf, 0, fileSize);
                            socket.send(packet);
                            // wait for succ response
                            while (true) {
                                packet.setData(signalBuf, 0, signalBuf.length);
                                socket.receive(packet);
                                String response = new String(signalBuf);
                                response = response.replace("\0", "");
                                if (response.equals("succ")) {
                                    break;
                                } else {
                                    System.out.println("resent packet " + packetCount);
                                    packet.setData(buf, 0, fileSize);
                                    socket.send(packet);
                                }
                            }
                            System.out.println("#" + (packetCount++) + " packets sent successfully.");
                        }
                        while (true) {
                            System.out.println("Send exit sign");
                            packet.setData("exit".getBytes(), 0, "exit".getBytes().length);
                            socket.send(packet);

                            packet.setData(signalBuf, 0, signalBuf.length);
                            socket.receive(packet);
                            // exit
                            String response = new String(signalBuf);
                            response = response.replace("\0", "");

                            if (response.equals("exit")) {
                                break;
                            } else {
                                System.out.println("Resent exit sign");
                                packet.setData("exit".getBytes(), 0, "exit".getBytes().length);
                                socket.send(packet);
                            }
                        }

                    }
                } else {
                    packet.setData("error\nInvalid file name.".getBytes(), 0,
                            "error\nInvalid file name.".getBytes().length);
                    socket.send(packet);
                    System.err.println("Invalid command.");
                }

            } catch (Exception e) {
                e.printStackTrace();
            }
            return null;
        }
    }

    public static void main(String[] args) {
        folderPathString = "\\Users\\Jennifer\\Documents\\masters\\242P Network Programming\\M4\\src\\ServerDirectory";
        folderPath = Paths.get(folderPathString);
        if (!Files.isDirectory(folderPath)) {
            System.err.println("Invalid folder path.");
            return;
        }

        ExecutorService pool = Executors.newFixedThreadPool(50);

        try {
            // UDP server socket has to be exposed to threads
            InetAddress inetAd = InetAddress.getByName(HOST_NAME);
            socket = new DatagramSocket(PORT_NUMBER, inetAd);
            System.out.println("Listening at port " + socket.getLocalPort());
            socket.setSoTimeout(TIME_OUT);

            while (true) {
                try {
                    byte[] buf = new byte[BUFFER_SIZE];
                    DatagramPacket packet = new DatagramPacket(buf, BUFFER_SIZE);
                    Thread.sleep(2000);
                    socket.receive(packet);
                    String userInput = new String(buf);
                    userInput = userInput.replace("\0", "");
                    System.out.println(userInput);
                    if (userInput.equals("index") || userInput.startsWith("get ")) {
                        System.out.println("Packet received from " + packet.getAddress().getHostAddress() + ":"
                                + packet.getPort());
                        pool.submit(new Task(packet, buf));
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (socket != null) {
                    socket.close();
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}

//reference: https://github.com/Zeyuuuuuu/UCI-MSWE-FALL2019/tree/master/242P/ex3