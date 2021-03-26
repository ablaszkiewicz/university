import java.io.*;
import java.net.Socket;

public class ClientHandler implements Runnable {
    private Socket socket;
    private String fileName;

    public ClientHandler(Socket socket, String fileName) {
        this.socket = socket;
        this.fileName = fileName;
    }

    @Override
    public void run() {
        System.out.println("[CLIENT HANDLER] Started");

        try (DataInputStream dis = new DataInputStream(socket.getInputStream()); FileOutputStream fos = new FileOutputStream(fileName)){

            //read file size
            int fileSize = dis.readInt();
            int read = 0;
            int totalRead = 0;

            byte[] buffer = new byte[64];
            int remaining = fileSize;

            while((read = dis.read(buffer, 0, Math.min(buffer.length, remaining))) > 0) {
                totalRead += read;
                int percent = (int)((float)totalRead/(float)fileSize*100);
                if (percent > 100) {
                    percent = 100;
                }
                System.out.print("\r");
                System.out.print("[CLIENT HANDLER] Downloading... | " + percent + " %");

                fos.write(buffer, 0, read);
            }
            System.out.println();
            System.out.print("[CLIENT HANDLER] Closing connection");
            socket.close();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
