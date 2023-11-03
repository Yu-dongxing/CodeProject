import java.util.Scanner;

public class prog2 {

    public static void code1(){
         // 初始化
         Scanner in = new Scanner(System.in);
         int b=0;
         while(true){
             System.out.print("请输入：");
             int a = in.nextInt();
             if(a >= 10){
                 // 打印车票
                 System.out.println("*************");
                 System.out.println("*java 铁路线路*");
                 System.out.println("* 323232职位票*");
                 System.out.println("* 10       余*");
                 System.out.println("**************");
                 // 计算
                 System.out.println("找一个钱："+(a-10));
             }
         }

    }
    public static void  code2 (){
        Scanner put = new Scanner(System.in);
        System.out.println("输入数值：");
        int a = put.nextInt();
        
    }
    public static void  code3(){
        // 初始化
        // 计算输入的整数中有几位数
        Scanner in = new Scanner(System.in);
        System.out.print("请输入整数：");
        int a= in.nextInt();
        int c = 0;
       do{
        a = a /10;
        c = c +1;
        System.out.println("a="+a+"c="+c);
        }while(a>0);
        System.out.println(c);
    }
    public static void  code4(){
        // 初始化
        Scanner in = new Scanner(System.in);
        int c = 100;
        while(c >= 0){
            
            System.out.println(c);
            c-=1;//c=c-1
        }
        System.out.println(c);
        System.out.println("输出");
    }
    public static void  code5(){
        // 计算平均数
        Scanner in = new Scanner(System.in);
        int n=0;
        int s=0;
        int c=0;
        double b=0;
        // n= in.nextInt();
        // while(n!=-1){
        //     s+=n;
        //     c+=1;
        //     n=in.nextInt();
        // }
        do{
            n = in.nextInt();
            if(n!=-1){
                s+=n;
                c+=1;
            }
        }while(n!=-1);
        if(c>0){
            b=(double)s/c;
        System.out.println("平均数="+b);
        }
    } 
    public static void  code6(){
        Scanner in = new Scanner(System.in);
        int n =(int) (Math.random()*100+1);//[0,1)--->[0,100)-->[1,100)
        int a;
        int c = 0;
        System.out.print("输入数值：");
        do{
            System.out.print("再次输入数值：");
            a=in.nextInt();
            c+=1;
            if(a>n){
                System.out.println("大了");
            }else if(a<n){
                System.out.println("小了");
            }
        }while(a!=n);
        System.out.println("恭喜你对了，过了"+c+"参");

    }
    public static void code7(){
        Scanner in = new Scanner(System.in);
        int n;
        n=in.nextInt();
        int r=0;
        do {
            int d=n%10;
            r=r*10+d;//如果a>b
            System.out.println(d);
            n=n/10;
        }while(n>0);
        System.out.println();
        System.out.println(r);
    }
    //以上为do-while/while循环
    public static void code8(){
        //阶乘 n!=1*2*3*----*n
        Scanner in = new Scanner(System.in);
        System.out.print("输入n：");
        int n=in.nextInt();
        int f =1;
        if(n<20){
            for(int i=1;i<=n;i++){
                f*=i;
             }
             System.out.println(f);
        }
        else 
            System.out.println("Error：数值过大");
    }
    //素数 只能被1和自己整除的数，不包括1 2，3，5，7(code9 错误代码)
    public static void code9(){
        Scanner in = new Scanner(System.in);
            System.out.print("输入一个整数：");
            int n=in.nextInt();
            int is= 1;
            for(int i=2;i<n;i++){
                if(n%i==0){
                    is=0;
                    //System.out.println(n+"不是素数");
                    //break;
                }
            }
            if (is==1){
                System.out.println(n+"是素数");
            }else {
                System.out.println(n+"不是素数");
            }
        }
    //样板
    public static void code10(){
        Scanner in=new Scanner(System.in);
        int a=in.nextInt();
        OUT:
        for(int o=0;o<=a;++o){
            for (int f=0;f<=a/5;++f){
                for(int t=0;t<=a/10;++t){
                    for(int te=0;te<=a/20;++te){
                        if(o+f*5+t*10+te*20 == a){
                            System.out.println(o+"个一元"+f+"个5元"+t+"个10元"+te+"个20元>>"+a);
                            break OUT;
                        }
                    }
                }
            }
        }
    }
    //求和
    //n=1/2+1/3----
    public static void code11(){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        double sum=0.0;
        for (int i=1;i<=n;i++){
            sum+=1.0/i;
        }
        System.out.printf("%.2f",sum);
    
    }
    //求差
    //n=1-1/2-1/3----
    public static void code12(){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        double sum=0.0;
        int sign= 1;
        for (int i=1;i<=n;i++,sign=-sign){
            sum+=sign*1.0/i;
            
            // if(i%2==1){
            //     sum+=1.0/i;
            // }else{
            //     sum-=1.0/i;
            // }
        }
        System.out.printf("%.2f",sum);
    
    }
    //最大公约数-枚举法
    public static void code13(){
        Scanner in = new Scanner(System.in);
        System.out.printf("请输入a：");
        int a= in.nextInt();
        System.out.printf("请输入b：");
        int b= in.nextInt();
        int gcd=1;
        for(int i=2;i<=a && i<=b;i++){
            if(a%i==0&&b%i==0){
                gcd=i;
            }
        } 
        System.out.println(a+"和"+b+"的公约数为"+gcd);
    }

        //最大公约数-辗转相除法
        public static void code14(){
            Scanner in =new Scanner(System.in);
            System.out.printf("请输入a：");
            int a= in.nextInt();
            System.out.printf("请输入b：");
            int b=in.nextInt();
            int oa=a;
            int ob=b;
            while(b!=0){
                int r=a%b;
                System.out.printf("%d,%d,%d\n",a,b,r);
                a=b;
                b=r;
            }
            System.out.printf("%d和%d的最大公约数为%d",oa,ob,a);
        }
        //数组
        public static void code15(){
            Scanner in = new Scanner(System.in);
            int x;
            int [] n=new int [100];
            double sum=0;
            int cut =0;
            x=in.nextInt();
            while(x!=-1){
                n[cut]=x;
                sum=sum+x;
                cut++;
                x=in.nextInt();
            }
            if(cut>0){
                double age =sum/cut;
                for(int i=0;i<cut;i++){
                    if(n[i]>age){
                        System.out.println(n[i]);
                    }
                }
                // System.out.println(sum/cut);
                System.out.printf("%lf",sum/cut);
            }
        }







    public static void main(String[] args) {
        System.out.print("请输入代码数值：");
        Scanner in=new Scanner(System.in);
        int a=in.nextInt();
        switch(a){
            case 1:code1();break;
            case 2:code3();break;
            case 3:code15();break;
            default: System.out.printf("error\n");
        }
    }
}