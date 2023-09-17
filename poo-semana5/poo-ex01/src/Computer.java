import java.util.Date;

public class Computer {
    private String brandName;
    private int speed;
    private Date manufactureYear;
    private boolean isNew;

    public Computer() {
    }

    public Computer(String brandName, int speed, Date manufactureYear, boolean isNew) {
        this.brandName = brandName;
        this.speed = speed;
        this.manufactureYear = manufactureYear;
        this.isNew = isNew;
    }
}
