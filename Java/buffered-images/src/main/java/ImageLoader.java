import org.apache.commons.lang3.tuple.Pair;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ForkJoinPool;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class ImageLoader {
    private Path source;
    private Path destination;
    private int threadsCount;

    public ImageLoader(String source, String destination, int threadsCount) {
        this.source = Path.of(source);
        this.destination = Path.of(destination);
        this.threadsCount = threadsCount;
    }

    private List<Path> imagesPathList() {
        List<Path> paths = null;

        try (Stream<Path> stream = Files.list(source)) {
            paths = stream.collect(Collectors.toList());
        } catch (IOException e) {
            e.printStackTrace();
        }

        return paths;
    }

    public void execute() {
        ForkJoinPool pool = new ForkJoinPool(threadsCount);
        List<Path> files = imagesPathList();
        try{
            pool.submit(() -> {
                Stream<Pair<Path, BufferedImage>> pairStream = files.stream().parallel().map(this::convertToPair);
                pairStream.map(pair -> Pair.of(pair.getLeft(), changeColors(pair.getRight()))).forEach(this::saveImage);
            }).get();
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }

    private Pair<Path, BufferedImage> convertToPair(Path path) {
        Pair<Path, BufferedImage> pair = null;

        try {
            pair = Pair.of(path.getFileName(), ImageIO.read(path.toFile()));
        } catch (IOException e) {
            e.printStackTrace();
        }

        return pair;
    }

    private BufferedImage changeColors(BufferedImage original) {
        BufferedImage modified = new BufferedImage(original.getWidth(), original.getHeight(), original.getType());

        for (int i=0; i<original.getWidth(); i++) {
            for (int j=0; j< original.getHeight(); j++) {
                int rgb = original.getRGB(i, j);
                Color originalColor = new Color(rgb);

                int r = (int)Math.round(originalColor.getRed() * 0.299);
                int g = (int)Math.round(originalColor.getGreen() * 0.587);
                int b = (int)Math.round(originalColor.getBlue() * 0.114);

                Color modifiedColor = new Color(r, g, b);

                modified.setRGB(i, j, modifiedColor.getRGB());
            }
        }

        return modified;
    }

    private void saveImage(Pair<Path, BufferedImage> pair){
        try {
            File file = new File(destination.toString() + "\\" + pair.getLeft().toString());
            ImageIO.write(pair.getRight(), "jpg", file);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
