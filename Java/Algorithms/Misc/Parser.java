package Java.Algorithms.Misc;

class Parser {
    private char character;
    private Function parser;

    public <R> Parser(Function<String, R> parser,char character) {
        this.character = character;
    }


    public static String[] parseChar(char chr, String str) throws ParserError {
        if (chr==str.charAt(0)){
            return new String[] {(String) chr, str.substring(1)};
        } else {
            throw new ParserError("Welcome to the end of it all");
        } 
    }


    public R run(String str) {
        return this.parser(str);
    }


    // public Result<String[], ParserError> run(String string) {
    //     if (string.isEmpty()) {
    //         return new Result<>(new ParserError("Tried to parse Empty String"));
    //     } else if (this.character == string.charAt(0)) {
    //         return new Result<>(new String[]{String.format("%s", this.character), string.substring(1)});
    //     } else {
    //         return new Result<>(
    //             new ParserError(
    //                 String.format(
    //                     "Expected: \"%s\", got: \"%s\"",
    //                     this.character, string.charAt(0)
    //                     )
    //                 )
    //             );
    //     }
    // }

    public static void main(String[] args) {
        Parser parser = new Parser('a');
        var parsed = parser.run("abc");
        System.out.println(parsed);
    }
}

