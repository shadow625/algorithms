/*Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
it's an algorithm problem from the leetcode 155.
and here is the blog about this problem.
*/

import java.util.Random;


public class minstack {
	private entry head;
	public minstack() {
		// TODO Auto-generated constructor stub
		head=new entry();
	}
	public void push(int x) {
        head=new entry(x,head);
    }

    public void pop() {
    	if (head.next!=null) {
    		head=head.next;	
		}
    }

    public int top() {
    	 if (head.next!=null) {
         	return head.num;
 		}
         return 0;
    }

    public int getMin() {
        if (head.next!=null) {
        	return head.min;
		}
        return 0;
    }
	class entry {//每个栈元素的类，具有3个属性 ：min最小值、num栈元素所存的数值、next 栈顶第二个元素的对象索引。
		private int min; 
 		private int num=-1;
		public entry next=null;

		public entry(int num,entry next){
			this.next=next;
			this.num=num;	
			if(next.next!=null&&next.min<=num){
				this.min=next.min;
			}
			else{
				this.min=num;
			}//此处进行
		}
		public entry(){
			
		}
	}
	public static void main(String[] args) {
		//System.err.println(1);
		minstack minstack = new minstack();
		Random random=new Random();
		for (int i = 0; i < 10; i++) {
			int x=random.nextInt(100);
			System.out.println(x);
			minstack.push(x);
		}
		entry head=minstack.head;
		while (head.next!=null) {
			System.out.println("num "+head.num+"\t "+head.min);
			head=head.next;
		}
	}
}
