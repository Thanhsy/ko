#Đối tượng Lớp đất chứa thuộc tính về lớp đất đó
class LopDat:
	def __init__(self, vitri, dosau, gama, gama_dn):
		self.vitri = vitri
		self.dosau = dosau
		self.gama = gama
		self.gama_dn = gama_dn

#Hàm tính độ lún của 1 phân tố
def element(i):
	Zi = hm + (i - 0.5)*dz  #Tính độ sâu của lớp phân tố thứ i
	#Xác định vị trí của phân tố i thuộc lớp đất nào
	#Tính gama tính toán
	for i in Z:  
		if Zi<=i.dosau and Zi <= MNG:
			gama_tt = i.gama;
			break; 
		if Zi<=i.dosau and Zi > MNG:
			gama_tt = i.gama_dn;
			break; 
		if Zi<= MNG:	
			gama_tt = i.gama
		else:
			gama_tt = i.gama_dn

	Pbt = Pbt + gama_tt*dz
	Ko = NoisuyKo(2z/b,a/b)
	Pgl = Ko*xichma_gl
	e1i = Noisuy(Pbt)
	e2i = Noisuy(Pbt+Pgl)
	Si = (e1i-e2i)/(1+e1i)*dz
	S = S+Si



# hàm tính lún cho cả móng
def Tinh lun():
	i = 1
	#Điều kiện lặp của bài toán
	while Pgl > 0.2*Pbt: 
		element(i)
		i++  #tiến đến phần tử tiếp theo


#Số liệu ví dụ
Z = [LopDat(1,5,1.85,2),LopDat(2,9,1.95,3),LopDat(3,10,2,4)]
hm = 3 						  #Độ sâu móng
dz = 1          			  #Chiều dày từng lớp phân tố
MNG = 4 					  # Mực nước ngầm
gama1 = 1.85 				  #Trong lượng riêng lớp đất từ đáy móng trở lên
Pbt = hm*gama1	 			  #Áp suất do trọng lượng bản thân tới lớp (i-1)
a,b = 3,4 					  #Kích thước móng
P = 100        				  #tải trọng đặt xuống móng
xichma_gl = P/(a*b)-gama1*hm  #xích ma gây lún
S = 0            			  #Độ lún
