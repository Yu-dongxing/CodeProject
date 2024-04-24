public class prog1 {
    /* 第一个Java程序
     * 它将输出字符串 Hello World
     */
    public static void main(String[] args) {
        System.out.println("Hello World"); // 输出 Hello World
        sull(args);
    }
    public static void  sull(String[] args){
        int rows = 5;
        for(int i = 1; i <= rows; i++){
         for(int j = 1; j <= i; j++){
          System.out.print(j);
         }
         System.out.print("\n");
        }
        
    }
}