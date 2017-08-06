import java.util.Scanner;
import java.util.Date;
import java.util.GregorianCalendar;
import java.text.SimpleDateFormat;

public class Solution {
    public static String getDay(String day, String month, String year) {
        int dd = Integer.parseInt(day);
        int mm = Integer.parseInt(month);
        int yy = Integer.parseInt(year);
        
        Date date = (new GregorianCalendar(yy,mm-1,dd)).getTime();
        SimpleDateFormat f = new SimpleDateFormat("EEEE");
        String stringDay = f.format(date);
        return stringDay.toUpperCase();   
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();
        
        System.out.println(getDay(day, month, year));
    }
}
