import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class CountLinksOnGoogle {
    public static void main(String[] args) {

        // Set the path to your ChromeDriver executable
        System.setProperty("webdriver.chrome.driver", "path_to_chromedriver");

        // Initialize the Chrome WebDriver
        WebDriver driver = new ChromeDriver();

        // Open Google
        driver.get("https://www.google.com");

        // Find all the anchor elements (links)
        // You can modify this if needed to find elements in a different way
        java.util.List<WebElement> allLinks = driver.findElements(By.tagName("a"));

        // Get the count of the links
        int numberOfLinks = allLinks.size();
        System.out.println("Number of links on the Google homepage: " + numberOfLinks);

        // Close the browser
        driver.quit();
    }
}
