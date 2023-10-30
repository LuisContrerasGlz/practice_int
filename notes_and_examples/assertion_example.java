import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.junit.jupiter.api.*;

public class GoogleTitleTest {

    WebDriver driver;

    @BeforeEach
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "path_to_chromedriver"); // Set the path to your chromedriver
        driver = new ChromeDriver();
    }

    @Test
    public void testGooglePageTitle() {
        driver.get("https://www.google.com");
        String expectedTitle = "Google";
        String actualTitle = driver.getTitle();
        // Assert whether the expected title matches the actual title
        Assertions.assertEquals(expectedTitle, actualTitle, "Expected title '" + expectedTitle + "' but got '" + actualTitle + "'");
    }

    @AfterEach
    public void tearDown() {
        driver.quit();
    }
}
