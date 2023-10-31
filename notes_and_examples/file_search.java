import java.io.IOException;
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.ArrayList;
import java.util.List;

public class FileSearch {
    public static void main(String[] args) {
        String directoryToSearch = "path/to/directory"; // Replace with the directory you want to search
        String fileExtensionToFind = ".txt"; // Replace with the file extension you want to search for

        List<String> foundFiles = searchFiles(directoryToSearch, fileExtensionToFind);

        if (foundFiles.isEmpty()) {
            System.out.println("No files found with the extension '" + fileExtensionToFind + "' in the directory.");
        } else {
            System.out.println("Found " + foundFiles.size() + " files with the extension '" + fileExtensionToFind + "':");
            for (String filePath : foundFiles) {
                System.out.println(filePath);
            }
        }
    }

    public static List<String> searchFiles(String directory, String fileExtension) {
        List<String> foundFiles = new ArrayList<>();
        Path startingDir = Paths.get(directory);
        try {
            Files.walkFileTree(startingDir, new SimpleFileVisitor<Path>() {
                @Override
                public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) {
                    if (file.toString().endsWith(fileExtension)) {
                        foundFiles.add(file.toString());
                    }
                    return FileVisitResult.CONTINUE;
                }

                @Override
                public FileVisitResult visitFileFailed(Path file, IOException exc) {
                    return FileVisitResult.CONTINUE;
                }
            });
        } catch (IOException e) {
            e.printStackTrace();
        }
        return foundFiles;
    }
}
