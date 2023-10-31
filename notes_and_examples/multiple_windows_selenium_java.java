import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.util.Set;

public class HandleMultipleWindows {

    public static void main(String[] args) {

        // Set the path to your ChromeDriver
        System.setProperty("webdriver.chrome.driver", "path_to_chromedriver");

        // Initialize the ChromeDriver
        WebDriver driver = new ChromeDriver();

        // Navigate to Google
        driver.get("https://www.google.com");

        // Store the parent window handle
        String parentWindowHandle = driver.getWindowHandle();

        // Clicking "News" to open a new window
        driver.findElement(By.linkText("News")).click();

        // Pause to allow the new window to open (you can replace with explicit wait)
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Get all window handles after the new window has opened
        Set<String> allWindowHandles = driver.getWindowHandles();

        // Loop through the window handles
        for (String handle : allWindowHandles) {
            if (!handle.equals(parentWindowHandle)) {
                // Switch to the new window
                driver.switchTo().window(handle);
                // Perform actions in the new window
                System.out.println("Switched to the new window");
                // Get the title of the new window
                System.out.println("New Window Title: " + driver.getTitle());
                // Get the URL of the new window
                System.out.println("New Window URL: " + driver.getCurrentUrl());
                // Pause for demonstration purposes
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                // Close the new window
                driver.close();
            }
        }

        // Switch back to the original window
        driver.switchTo().window(parentWindowHandle);
        // Perform actions in the original window
        System.out.println("Switched back to the parent window");
        // Get the title of the parent window
        System.out.println("Parent Window Title: " + driver.getTitle());

        // Close the browser
        driver.quit();
    }
}

/*

This Java code uses Selenium to open Google, click on the "News" link to open a new window, 
retrieves information such as the title and URL from the new window, switches back to the original window, 
and then prints the title of the original window before closing the browser. 

 */