import java.io.*;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Client implements Runnable {
    private Socket socket;
    private String fileName;
    public Client(int port, String fileName)  {
        try {
            socket = new Socket("localhost", port);
            this.fileName = fileName;
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    @Override
    public void run() {
        try (DataOutputStream dos = new DataOutputStream(socket.getOutputStream());FileInputStream fis = new FileInputStream(fileName)) {

            //send file size
            File file = new File(fileName);
            int sizeInBytes = (int)file.length();
            dos.writeInt(sizeInBytes);

            //send the file itself
            byte[] buffer = new byte[64];
            while(fis.read(buffer) > 0) {
                dos.write(buffer);
            }
            socket.close();
        } catch(IOException ex) {
            ex.printStackTrace();
        }
    }
}
