package quicksort;
import java.util.Random;

import org.omg.CORBA.PUBLIC_MEMBER;

public class QuickSort {
	public static void main(String[] args) {
		int list[]=new int[100];
		Random ran=new Random();
		
		for (int i = 0; i < list.length; i++) {//初始化
			list[i]=ran.nextInt(100);
		}
		System.out.println();
		QuickSort smain=new QuickSort();
		smain.show(list, 0, 99);
		smain.Sort(list, 0, 99);
		smain.show(list, 0, 99);
	}
	public void Sort(int[] list,int p,int r){//递归
		if (p<r) {
			int q=Part(list,p,r);
			Sort(list, p, q-1);
			Sort(list, q+1, r);
		}
	}
	public int Part(int[] list,int p,int r){//重要代码
		int key=list[r];
		int i=p-1;						//i指向小于目标数的第一个数，当前没有比较，所以不存在。
		for (int j = p; j < r; j++) {
			if (list[j]<=key) {
				i+=1;
				int mid=list[i];					//i始终指向小于目标数的最后一个数，即就是i+1指向大于目标的第一个数
				list[i]=list[j];					//若list[j]小于目标数，则将其与第一个最大数交换
				list[j]=mid;
			}
		}
		int mid=list[i+1];		//交换目标和大于目标数的第一个数
		list[i+1]=list[r];
		list[r]=mid;
		
		return i+1;									//i+1即就是目标数所在位置
	}

	private void show(int[] list,int p,int r) {//测试使用，用于显示数组
		for (int i = p; i < r+1; i++) {
			if (i%10==0) {
				System.out.println();
			}
			System.out.print(list[i]+"\t");
		}
	}
}
