import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;
import java.util.ArrayList;

public class Server implements Runnable {
    private int port;
    private int id;
    private ArrayList<Thread> threads = new ArrayList<Thread>();
    private ServerSocket serverSocket;

    public Server(int port) {
        System.out.println("Created server on port: " + port);
        this.port = port;
    }

    @Override
    public void run() {

            try {
                serverSocket = new ServerSocket(port);
                System.out.println("Started server on port: " + port);
                while(!Thread.interrupted()) {
                    try {
                        Socket socket = serverSocket.accept();
                        System.out.println("Someone connected");
                        Thread clientHandlerThread = new Thread(new ClientHandler(socket, "receive" + id + ".txt"));
                        id++;
                        clientHandlerThread.start();
                        threads.add(clientHandlerThread);
                    } catch(SocketException e) {
                        System.out.println("Closed server thread");
                        Thread.currentThread().interrupt();
                        break;
                    }
                    catch (IOException ex) {
                        System.err.println(ex);
                    }
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
    }

    public void close() {
        try {
            for(Thread thread : threads) {
                if(thread.isAlive()) {
                    thread.join();
                }
            }
            System.out.println("Closed all ClientHandler threads");
            serverSocket.close();
        } catch(IOException e) {
            e.printStackTrace();
        }
        catch(InterruptedException e) {
            e.printStackTrace();
        }
    }
}
