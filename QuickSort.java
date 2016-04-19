package quicksort;
import java.util.Random;

import org.omg.CORBA.PUBLIC_MEMBER;

public class QuickSort {
	public static void main(String[] args) {
		int list[]=new int[100];
		Random ran=new Random();
		
		for (int i = 0; i < list.length; i++) {//��ʼ��
			list[i]=ran.nextInt(100);
		}
		System.out.println();
		QuickSort smain=new QuickSort();
		smain.show(list, 0, 99);
		smain.Sort(list, 0, 99);
		smain.show(list, 0, 99);
	}
	public void Sort(int[] list,int p,int r){//�ݹ�
		if (p<r) {
			int q=Part(list,p,r);
			Sort(list, p, q-1);
			Sort(list, q+1, r);
		}
	}
	public int Part(int[] list,int p,int r){//��Ҫ����
		int key=list[r];
		int i=p-1;						//iָ��С��Ŀ�����ĵ�һ��������ǰû�бȽϣ����Բ����ڡ�
		for (int j = p; j < r; j++) {
			if (list[j]<=key) {
				i+=1;
				int mid=list[i];					//iʼ��ָ��С��Ŀ���������һ������������i+1ָ�����Ŀ��ĵ�һ����
				list[i]=list[j];					//��list[j]С��Ŀ�������������һ�����������
				list[j]=mid;
			}
		}
		int mid=list[i+1];		//����Ŀ��ʹ���Ŀ�����ĵ�һ����
		list[i+1]=list[r];
		list[r]=mid;
		
		return i+1;									//i+1������Ŀ��������λ��
	}

	private void show(int[] list,int p,int r) {//����ʹ�ã�������ʾ����
		for (int i = p; i < r+1; i++) {
			if (i%10==0) {
				System.out.println();
			}
			System.out.print(list[i]+"\t");
		}
	}
}
