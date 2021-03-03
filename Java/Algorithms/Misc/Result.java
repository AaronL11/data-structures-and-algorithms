package Java.Algorithms.Misc;


public class Result<T,E extends Throwable> {
    private T result;
    private E err;

    public Result() {

    }

    public Result(T good) {
        this.result = good;
    }

    public Result(E bad) {
        this.err = bad;
    }

    public T unwrap() throws E {
        if (this.err == null) { return this.result; } else { throw this.err; }
    }
}
