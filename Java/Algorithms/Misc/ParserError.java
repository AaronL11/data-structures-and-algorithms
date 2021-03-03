package Java.Algorithms.Misc;


public class ParserError extends Exception {
    private String msg;

    public ParserError(String msg) {
        this.msg = msg;
    }
}
